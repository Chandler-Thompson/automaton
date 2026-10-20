#!/usr/bin/env python3
"""safe-secret-scan -- inventory config keys without ever printing a value.

Usage (always under -I so nothing on the cwd can shadow stdlib):
    python3 -I scan.py <file> [<file> ...]
    python3 -I scan.py - --name appsettings.Production.json   < some-dump
    python3 -I scan.py --ref origin/main appsettings.json .env  [--repo DIR]
    python3 -I scan.py --json <file>
    python3 -I scan.py --self-test

Exit codes:
    0  clean
    1  self-test failed
    2  bad invocation, unreadable input, or git show failure
    3  one or more output lines were SUPPRESSED because they would have
       contained a parsed value (the defensive guard fired -- report it)

WHY THIS EXISTS (2026-10-20)
    I ran git grep / git show over appsettings.*.json, server.properties, .env
    and init.sql looking for key NAMES, with an ad-hoc sed redaction. The regex
    missed a field and live SMTP credentials plus API keys landed in my context.
    Floor item 6 says credentials are referenced by location, never stored in
    memory or ledger; a value in context is one autocomplete away from both.
    Prose rules did not stop it. This script is the executable version of the
    rule: it parses the file and prints shape only -- key path, file:line,
    value length, value class, placeholder match, sensitivity of the key name.

WHAT THIS IS NOT
    It is not a secret detector for CI, and the classes are heuristics. A value
    classed `text` can still be a secret; a key flagged sensitive can be
    harmless. The one hard guarantee is the negative one: no parsed value is
    written to stdout or stderr in any mode. render() is checked against every
    parsed value before anything is printed, and --self-test proves that with a
    sentinel.

Stdlib only. No PyYAML -- the YAML parser is line-based on purpose.
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys

# ---------------------------------------------------------------- key names

SENSITIVE_KEY = re.compile(
    r"(?i)(pass|pwd|secret|token|key|credential|auth|smtp|private|cert|salt|sig"
    r"|connection|dsn)"
)
# A key whose LAST word is one of these is clearly not a secret holder even if
# an earlier word matched above (SMTP_HOST, AuthUrl, KeyVaultName, ApiKeyId).
NON_SECRET_TAIL = ("url", "uri", "host", "hostname", "port", "name", "id",
                   "path", "env", "environment", "enabled", "timeout", "region",
                   "version", "type", "mode", "from", "to", "sender", "server",
                   "database", "user", "ssl", "tls", "level", "issuer", "audience")

PLACEHOLDER_EXACT = {
    "xxx", "changeme", "change_me", "change-me", "tbd", "replace_me",
    "replaceme", "replace-me", "password", "secret", "example", "todo",
    "placeholder", "null", "none", "undefined", "dummy",
}
PLACEHOLDER_PREFIX = ("localdev", "your-", "your_")
PLACEHOLDER_RE = re.compile(r"^(<.*>|\$\{[^}]*\}|\$[A-Z_][A-Z0-9_]*|%[A-Z_][A-Z0-9_]*%)$")

KNOWN_SECRET_FORMAT = re.compile(
    r"^(sk-|sk_live_|sk_test_|AKIA[0-9A-Z]{12,}|ghp_|gho_|github_pat_|xox[abp]-"
    r"|glpat-|AIza|-----BEGIN |eyJ[A-Za-z0-9_-]{10,}\.)"
)
URL_RE = re.compile(r"^(jdbc:)?[A-Za-z][A-Za-z0-9+.-]*://")
NUMBER_RE = re.compile(r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$")
# Shapes that mix letters and digits but are plainly not secrets.
HOSTNAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+(:\d+)?$")
HOSTPORT_RE = re.compile(r"^[a-z0-9.-]+:\d{1,5}$")
IDENT_RE = re.compile(r"^[a-z][a-z0-9]*([-_][a-z0-9]+){0,4}$")  # us-east-1, kv-prod
CONN_STRING_RE = re.compile(r"^\s*(?:[\w .]+=[^;]*;\s*){1,}[\w .]+=[^;]*;?\s*$")


def key_words(key):
    """Split a key path into lowercase words: Smtp.ApiKey_Id -> smtp api key id."""
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", key)
    return [w.lower() for w in re.split(r"[^A-Za-z0-9]+", spaced) if w]


def is_sensitive_key(key):
    words = key_words(key)
    if not words:
        return False
    if not SENSITIVE_KEY.search(key):
        return False
    tail = words[-1]
    return not any(tail.endswith(t) for t in NON_SECRET_TAIL)


# ------------------------------------------------------------------ values

def strip_quotes(v):
    """Unquote; a quoted value followed by a trailing comment keeps only the
    quoted part ("x"   # prod -> x)."""
    v = v.strip()
    if len(v) >= 2 and v[0] in "\"'`":
        end = v.find(v[0], 1)
        if end == len(v) - 1:
            return v[1:-1]
        if end > 0 and v[end + 1:].lstrip().startswith("#"):
            return v[1:end]
    return v


def is_placeholder(v):
    if v == "":
        return True
    low = v.lower()
    if len(v) <= 3:
        return True
    if len(set(v)) == 1:
        return True
    if low in PLACEHOLDER_EXACT:
        return True
    if low.startswith(PLACEHOLDER_PREFIX):
        return True
    return bool(PLACEHOLDER_RE.match(v))


def entropy(v):
    if not v:
        return 0.0
    counts = {}
    for ch in v:
        counts[ch] = counts.get(ch, 0) + 1
    n = len(v)
    return -sum(c / n * math.log2(c / n) for c in counts.values())


def looks_like_secret(v):
    if KNOWN_SECRET_FORMAT.match(v):
        return True
    if len(v) < 8 or any(ch.isspace() for ch in v):
        return False
    if HOSTNAME_RE.match(v) or HOSTPORT_RE.match(v) or (IDENT_RE.match(v) and len(v) < 16):
        return False
    has_digit = any(ch.isdigit() for ch in v)
    has_alpha = any(ch.isalpha() for ch in v)
    has_symbol = any(not ch.isalnum() for ch in v)
    ent = entropy(v)
    if has_digit and has_alpha and (len(v) >= 16 or ent >= 3.0):
        return True
    if has_symbol and len(v) >= 12 and "/" not in v:
        return True
    return len(v) >= 12 and ent >= 3.5


def classify(v):
    """-> (class, flags). Classes: empty placeholder bool number url
    looks-like-secret text."""
    flags = []
    if v == "":
        return "empty", flags
    low = v.lower()
    if low in ("true", "false", "yes", "no", "on", "off"):
        return "bool", flags
    if NUMBER_RE.match(v):
        return "number", flags
    if is_placeholder(v):
        return "placeholder", flags
    if URL_RE.match(v):
        authority = v.split("://", 1)[1].split("/", 1)[0]
        if "@" in authority and ":" in authority.split("@", 1)[0]:
            flags.append("embedded-userinfo")
        return "url", flags
    if KNOWN_SECRET_FORMAT.match(v):
        flags.append("known-secret-format")
    if looks_like_secret(v):
        return "looks-like-secret", flags
    return "text", flags


# ------------------------------------------------------------------ entries

class Entry:
    __slots__ = ("source", "line", "key", "value")

    def __init__(self, source, line, key, value):
        self.source, self.line, self.key, self.value = source, line, key, value

    def describe(self):
        v = self.value
        cls, flags = classify(v)
        sensitive = is_sensitive_key(self.key)
        placeholder = cls in ("empty", "placeholder")
        if sensitive and cls == "looks-like-secret":
            flags.append("LIVE?")
        return {
            "source": self.source, "line": self.line, "key": self.key,
            "length": len(v), "class": cls, "placeholder": placeholder,
            "sensitive": sensitive, "flags": flags,
        }


def expand(entry):
    """A connection string carries sub-fields; surface them as their own keys."""
    out = [entry]
    v = entry.value
    if ";" in v and "=" in v and CONN_STRING_RE.match(v):
        for part in v.split(";"):
            if "=" in part:
                k, sub = part.split("=", 1)
                k = k.strip()
                if k:
                    out.append(Entry(entry.source, entry.line,
                                     "%s[%s]" % (entry.key, k), sub.strip()))
    return out


# ------------------------------------------------------------------ parsers

def parse_dotenv(text, source):
    out = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_.-]*)\s*=\s*(.*)$", line)
        if not m:
            continue
        val = m.group(2)
        if not (val.startswith('"') or val.startswith("'")):
            val = val.split(" #", 1)[0].rstrip()
        out.append(Entry(source, n, m.group(1), strip_quotes(val)))
    return out


def parse_properties(text, source):
    out = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        n = i + 1
        while raw.rstrip().endswith("\\") and i + 1 < len(lines):
            i += 1
            raw = raw.rstrip()[:-1] + lines[i].lstrip()
        i += 1
        line = raw.strip()
        if not line or line[0] in "#!":
            continue
        m = re.match(r"^([^=:\s]+)\s*[=:]?\s*(.*)$", line)
        if not m:
            continue
        out.append(Entry(source, n, m.group(1), strip_quotes(m.group(2))))
    return out


_JSON_TOKEN = re.compile(
    r'\s*(?:(?P<str>"(?:[^"\\]|\\.)*")|(?P<punct>[{}\[\]:,])'
    r"|(?P<num>-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?P<lit>true|false|null))"
)


def parse_json(text, source):
    """Recursive descent with line numbers. Raises ValueError on bad JSON."""
    tokens = []
    pos = 0
    while pos < len(text):
        m = _JSON_TOKEN.match(text, pos)
        if not m:
            if text[pos:].strip() == "":
                break
            raise ValueError("bad json")
        kind = m.lastgroup
        tokens.append((kind, m.group(kind), text.count("\n", 0, m.start(kind)) + 1))
        pos = m.end()
    out = []
    idx = [0]

    def peek():
        return tokens[idx[0]] if idx[0] < len(tokens) else (None, None, 0)

    def take():
        t = peek()
        idx[0] += 1
        return t

    def scalar(tok):
        kind, val, _ = tok
        if kind == "str":
            return json.loads(val)
        return val

    def value(path):
        kind, val, line = take()
        if kind == "punct" and val == "{":
            if peek()[1] == "}":
                take()
                return
            while True:
                k = take()
                if k[0] != "str":
                    raise ValueError("bad json")
                if take()[1] != ":":
                    raise ValueError("bad json")
                value(path + [json.loads(k[1])])
                sep = take()[1]
                if sep == "}":
                    return
                if sep != ",":
                    raise ValueError("bad json")
        elif kind == "punct" and val == "[":
            if peek()[1] == "]":
                take()
                return
            i = 0
            while True:
                value(path + ["[%d]" % i])
                i += 1
                sep = take()[1]
                if sep == "]":
                    return
                if sep != ",":
                    raise ValueError("bad json")
        elif kind in ("str", "num", "lit"):
            out.append(Entry(source, line, ".".join(path) or "<root>",
                             scalar((kind, val, line))))
        else:
            raise ValueError("bad json")

    value([])
    if idx[0] != len(tokens):
        raise ValueError("bad json")
    return out


def parse_yaml(text, source):
    out = []
    stack = []  # (indent, key)
    lines = text.splitlines()
    block = None  # (entry, indent) while swallowing a | or > scalar
    for n, raw in enumerate(lines, 1):
        if block is not None:
            ind = len(raw) - len(raw.lstrip(" "))
            if raw.strip() == "" or ind > block[1]:
                block[0].value += raw.strip() + "\n"
                continue
            block[0].value = block[0].value.strip()
            block = None
        if not raw.strip() or raw.lstrip().startswith("#") or raw.strip() == "---":
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if line.startswith("- "):
            line = line[2:].lstrip()
            indent += 2
        m = re.match(r"^([^:#]+?)\s*:(?:\s+(.*)|\s*)$", line)
        if not m:
            continue
        while stack and stack[-1][0] >= indent:
            stack.pop()
        key = m.group(1).strip().strip("\"'")
        val = m.group(2)
        path = ".".join([k for _, k in stack] + [key])
        if val is not None and val.split(" #", 1)[0].strip() in ("|", ">", "|-", ">-", "|+", ">+"):
            e = Entry(source, n, path, "")
            out.append(e)
            block = (e, indent)
            continue
        if val is None:
            stack.append((indent, key))
            continue
        if not (val.startswith('"') or val.startswith("'")):
            val = val.split(" #", 1)[0].rstrip()
        if val in ("{}", "[]"):
            continue
        out.append(Entry(source, n, path, strip_quotes(val)))
    if block is not None:
        block[0].value = block[0].value.strip()
    return out


_SQL_PATTERNS = [
    (re.compile(r"(?i)\b(?:CREATE|ALTER)\s+(?:USER|ROLE|LOGIN)\s+(?:IF\s+NOT\s+EXISTS\s+)?"
                r"'?([^'\s@]+)'?(?:@'[^']*')?.*?"
                r"\b(?:IDENTIFIED\s+BY|(?:WITH\s+)?PASSWORD\s*=?)\s*'((?:[^'\\]|\\.)*)'"),
     "user:{0}.password"),
    (re.compile(r"(?i)\bIDENTIFIED\s+BY\s+'((?:[^'\\]|\\.)*)'"), "identified_by"),
    (re.compile(r"(?i)\bPASSWORD\s*=?\s*'((?:[^'\\]|\\.)*)'"), "password"),
    (re.compile(r"(?i)\bSET\s+([A-Za-z_][\w.]*)\s*=\s*'((?:[^'\\]|\\.)*)'"), "set:{0}"),
]


def parse_sql(text, source):
    out = []
    for n, raw in enumerate(text.splitlines(), 1):
        if raw.lstrip().startswith("--"):
            continue
        for rx, keyfmt in _SQL_PATTERNS:
            m = rx.search(raw)
            if not m:
                continue
            groups = m.groups()
            key = keyfmt.format(*groups[:-1]) if "{0}" in keyfmt else keyfmt
            out.append(Entry(source, n, key, groups[-1]))
            break
    return out


def parse_generic(text, source):
    out = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line[0] in "#;/":
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_.\-\[\]]*)\s*[=:]\s*(.+)$", line)
        if not m:
            continue
        out.append(Entry(source, n, m.group(1), strip_quotes(m.group(2).rstrip(",;"))))
    return out


FORMATS = {"dotenv": parse_dotenv, "properties": parse_properties, "json": parse_json,
           "yaml": parse_yaml, "sql": parse_sql, "generic": parse_generic}


def detect_format(name, text):
    base = os.path.basename(name).lower()
    ext = os.path.splitext(base)[1]
    if base.startswith(".env") or ext == ".env" or base == "env":
        return "dotenv"
    if ext == ".properties":
        return "properties"
    if ext == ".json":
        return "json"
    if ext in (".yml", ".yaml"):
        return "yaml"
    if ext == ".sql":
        return "sql"
    if ext in (".tfvars", ".ini", ".cfg", ".conf", ".toml"):
        return "generic"
    head = text.lstrip()[:1]
    if head in ("{", "["):
        return "json"
    if re.search(r"(?i)\bIDENTIFIED BY\b|\bCREATE (USER|ROLE)\b", text):
        return "sql"
    if re.search(r"(?m)^[A-Z][A-Z0-9_]*=", text):
        return "dotenv"
    if re.search(r"(?m)^\s*[\w.-]+:\s", text):
        return "yaml"
    return "generic"


def parse(text, source, fmt=None):
    fmt = fmt or detect_format(source, text)
    try:
        entries = FORMATS[fmt](text, source)
    except ValueError:
        fmt, entries = "generic", parse_generic(text, source)
    expanded = []
    for e in entries:
        expanded.extend(expand(e))
    return fmt, expanded


# ---------------------------------------------------------------- rendering

def guard_values(entries):
    """Every value that must never appear in output. Exempt only classes
    that cannot be a secret and would collide with ordinary output text
    (line numbers, 'true', the word 'password' in a key name)."""
    guarded = set()
    for e in entries:
        cls, _ = classify(e.value)
        if cls in ("empty", "placeholder", "bool"):
            continue
        if cls == "number" and len(e.value) <= 5:
            continue
        guarded.add(e.value.lower())
    return guarded


def render_text(rows, sources):
    lines = ["# safe-secret-scan: %d entries from %d source(s); values are never shown"
             % (len(rows), len(sources))]
    for r in rows:
        tag = "%s:%d" % (r["source"], r["line"])
        extra = (" " + ",".join(r["flags"])) if r["flags"] else ""
        lines.append("%-40s %-44s len=%-4d class=%-17s placeholder=%-3s sensitive=%s%s"
                     % (tag, r["key"], r["length"], r["class"],
                        "yes" if r["placeholder"] else "no",
                        "YES" if r["sensitive"] else "no", extra))
    sens = [r for r in rows if r["sensitive"]]
    live = [r for r in sens if "LIVE?" in r["flags"]]
    lines.append("# summary: %d sensitive key(s), %d look live (non-placeholder secret-shaped), "
                 "%d placeholder/empty" % (len(sens), len(live),
                                           sum(1 for r in rows if r["placeholder"])))
    return lines


def render_json(rows, sources):
    doc = {"sources": sources, "entries": rows}
    return json.dumps(doc, indent=1).splitlines()


def emit(lines, guarded, out=sys.stdout):
    """Print lines, suppressing any that contain a guarded value. Returns the
    number suppressed. This is the last line of defence and it is dumb on
    purpose: case-insensitive substring, no cleverness."""
    suppressed = 0
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(v in low for v in guarded):
            suppressed += 1
            out.write("<output line %d suppressed: it would have contained a parsed value>\n" % i)
            continue
        out.write(line + "\n")
    return suppressed


# -------------------------------------------------------------------- inputs

def read_source(path, args):
    """-> (label, text) or raises OSError/RuntimeError. Never echoes content."""
    if path == "-":
        return (args.name or "<stdin>"), sys.stdin.read()
    if args.ref:
        cmd = ["git"]
        if args.repo:
            cmd += ["-C", args.repo]
        cmd += ["show", "%s:%s" % (args.ref, path)]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if proc.returncode != 0:
            first = (proc.stderr.strip().splitlines() or ["(no stderr)"])[0]
            raise RuntimeError("git show %s:%s failed (exit %d): %s"
                               % (args.ref, path, proc.returncode, first))
        return "%s:%s" % (args.ref, path), proc.stdout
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return path, fh.read()


# ----------------------------------------------------------------- self-test

SENTINEL = "SENTINEL_qZ9vT3kLm2"

_FIXTURES = {
    ".env": "SMTP_HOST=smtp.example.test\nSMTP_PASSWORD=%s\nAPI_KEY=changeme\n"
            "export DB_PASS='%s'\nGUARDTRIP=guardtrip\nPORT=25\nDEBUG=true\n" % (SENTINEL, SENTINEL),
    "server.properties": "db.url=jdbc:mysql://localhost/x\ndb.password=%s\n"
                         "mail.smtp.secret: %s\nname=localdev-box\n" % (SENTINEL, SENTINEL),
    "appsettings.json": json.dumps({
        "Smtp": {"Host": "h", "Password": SENTINEL, "Port": 587},
        "ConnectionStrings": {"Default": "Server=db;User Id=app;Password=%s;" % SENTINEL},
        "Keys": [{"ApiKey": "<your-key-here>"}, {"ApiKey": SENTINEL}],
        "Flag": True, "Url": "https://user:%s@host/x" % SENTINEL,
    }, indent=2),
    "init.sql": "CREATE USER 'app'@'%%' IDENTIFIED BY '%s';\n"
                "ALTER USER postgres WITH PASSWORD '%s';\n"
                "SET secret_salt = '%s';\n" % (SENTINEL, SENTINEL, SENTINEL),
    "secrets.yml": "smtp:\n  host: relay\n  password: %s\nitems:\n  - token: %s\n"
                   "  - token: xxx\napi_key: ${API_KEY}\n" % (SENTINEL, SENTINEL),
}


def self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    for name, text in _FIXTURES.items():
        check(SENTINEL in text, "fixture %s does not contain the sentinel" % name)
    all_rows, all_entries = [], []
    for name, text in _FIXTURES.items():
        fmt, entries = parse(text, name)
        check(fmt == detect_format(name, text), "format for %s" % name)
        check(entries, "no entries parsed from %s" % name)
        sentinel_hits = sum(1 for e in entries if e.value == SENTINEL)
        check(sentinel_hits >= 1, "sentinel not parsed as a value in %s" % name)
        all_entries.extend(entries)
        all_rows.extend(e.describe() for e in entries)
    keys = {r["key"] for r in all_rows}
    for expected in ("SMTP_PASSWORD", "db.password", "Smtp.Password",
                     "ConnectionStrings.Default[Password]", "Keys.[1].ApiKey",
                     "user:app.password", "user:postgres.password", "set:secret_salt",
                     "smtp.password", "items.token"):
        check(expected in keys, "expected key missing: %s" % expected)
    by_key = {r["key"]: r for r in all_rows}
    check(by_key["SMTP_HOST"]["sensitive"] is False, "SMTP_HOST should be non-sensitive")
    check(by_key["SMTP_PASSWORD"]["sensitive"] is True, "SMTP_PASSWORD should be sensitive")
    check(by_key["API_KEY"]["placeholder"] is True, "changeme should be a placeholder")
    check(by_key["api_key"]["placeholder"] is True, "${API_KEY} should be a placeholder")
    check(by_key["Keys.[0].ApiKey"]["placeholder"] is True, "<your-key-here> placeholder")
    check(by_key["SMTP_PASSWORD"]["class"] == "looks-like-secret", "sentinel class")
    check("LIVE?" in by_key["SMTP_PASSWORD"]["flags"], "live flag on sentinel")
    check("embedded-userinfo" in by_key["Url"]["flags"], "url userinfo flag")
    check(by_key["PORT"]["class"] == "number" and by_key["DEBUG"]["class"] == "bool",
          "number/bool classes")

    guarded = guard_values(all_entries)
    check(SENTINEL.lower() in guarded, "sentinel not in guard set")

    import io
    for renderer in (render_text, render_json):
        lines = renderer(all_rows, list(_FIXTURES))
        buf = io.StringIO()
        suppressed = emit(lines, guarded, out=buf)
        text = buf.getvalue()
        check(SENTINEL not in text, "SENTINEL LEAKED in %s output" % renderer.__name__)
        check(SENTINEL.lower() not in text.lower(), "sentinel leaked (case) in %s"
              % renderer.__name__)
        # GUARDTRIP=guardtrip: the value equals its own key (case aside), so the
        # guard must fire on exactly that line -- once, not on everything.
        check(suppressed == 1, "guard suppressed %d line(s) in %s, expected 1"
              % (suppressed, renderer.__name__))
        check("SMTP_PASSWORD" in text, "ordinary rows missing from %s" % renderer.__name__)

    # The harness itself can fail: a planted leak must be caught.
    buf = io.StringIO()
    planted = emit(["key=%s" % SENTINEL], guarded, out=buf)
    check(planted == 1 and SENTINEL not in buf.getvalue(), "planted leak was not caught")

    if failures:
        for f in failures:
            print("FAIL: " + f)
        print("self-test: %d failure(s)" % len(failures))
        return 1
    print("self-test: OK (%d entries across %d fixtures; sentinel never appeared in "
          "text or json output; guard caught the planted leak)" % (len(all_rows), len(_FIXTURES)))
    return 0


# --------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="list config keys; never print values")
    ap.add_argument("paths", nargs="*", help="files, or - for stdin")
    ap.add_argument("--name", help="label for stdin (also drives format detection)")
    ap.add_argument("--ref", help="git ref; each path is read via `git show ref:path`")
    ap.add_argument("--repo", help="repo dir for --ref (default: cwd)")
    ap.add_argument("--format", choices=sorted(FORMATS), help="force a parser")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.paths:
        ap.print_usage(sys.stderr)
        return 2

    rows, entries, sources, errors = [], [], [], 0
    for path in args.paths:
        try:
            label, text = read_source(path, args)
        except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
            sys.stderr.write("error: %s\n" % exc)
            errors += 1
            continue
        _, found = parse(text, label, args.format)
        sources.append(label)
        entries.extend(found)
        rows.extend(e.describe() for e in found)

    guarded = guard_values(entries)
    lines = render_json(rows, sources) if args.json else render_text(rows, sources)
    suppressed = emit(lines, guarded)
    if suppressed:
        sys.stderr.write("guard: %d output line(s) suppressed because they would have "
                         "contained a parsed value\n" % suppressed)
        return 3
    return 2 if errors else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # never let a traceback carry data to the terminal
        sys.stderr.write("error: %s\n" % type(exc).__name__)
        sys.exit(2)
