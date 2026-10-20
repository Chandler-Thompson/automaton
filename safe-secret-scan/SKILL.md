---
name: safe-secret-scan
description: Inventory the keys in a config or secrets file without ever reading a value into context. Use when asked to "look for keys", "which secrets/config does X need", "grep for credentials", "what env vars does this service use", or before ANY read of .env / appsettings*.json / *.properties / secrets.yml / docker-compose env blocks / init.sql / *.tfvars — in the working tree or via git show. Prints key names, file:line, value length and class; never the value.
---

# Safe secret scan — key names without values

Status: **PROVISIONAL** (born 2026-10-20, skill genesis from an incident).

The incident: I ran `git grep` / `git show` over `appsettings.*.json`,
`server.properties`, `.env` and `init.sql` looking for key names and URLs, with
an ad-hoc `sed` redaction. The regex missed a field and live SMTP credentials
plus API keys were printed into my context. Floor 6 says credentials are
referenced by location, never stored in memory or ledger. A value sitting in
context is one summary away from both. A prose rule did not prevent it, so this
one is executable (same reasoning as `send-lint`).

## The protocol

1. **Never read a config/secrets file raw.** No `cat`, `head`, `sed -n`, `grep`,
   `git show`, `git grep -n`, Read tool, or `jq` against: `.env*`, `*.env`,
   `appsettings*.json`, `*.properties`, `secrets.y*ml`, `*.tfvars`, `init.sql`
   or any SQL with `IDENTIFIED BY` / `PASSWORD`, docker-compose `environment:`
   blocks, `*.pem`/`*.key`, or anything a human calls "the config". Content I
   did not request still counts: a `git diff` or `git log -p` that touches one
   of these files is a raw read.
2. **Always go through the script.** It parses the file and prints shape only:

   ```sh
   python3 -I mind/skills/safe-secret-scan/scan.py <file> [<file>...]
   python3 -I mind/skills/safe-secret-scan/scan.py --ref origin/main --repo <dir> <path> [<path>...]
   python3 -I mind/skills/safe-secret-scan/scan.py --json <file>
   ```

   Per entry: key path (dotted for JSON/YAML, `ConnectionStrings.Default[Password]`
   for embedded connection strings), `file:line`, value **length**, value
   **class** (`empty` `placeholder` `bool` `number` `url` `looks-like-secret`
   `text`), `placeholder=yes|no` against the known list (empty, `xxx`, `changeme`,
   `TBD`, `<...>`, `REPLACE_ME`, `localdev*`, `password`, `secret`, `your-*`,
   `example`, `${VAR}`, all-same-char, length ≤ 3), and `sensitive=YES` when
   the key name matches pass/pwd/secret/token/key/credential/auth/smtp/private/
   cert/salt/sig/connection and does not end in a plainly non-secret word
   (url, host, port, name, id, path, env, server, database, user, ...).
   Flags: `LIVE?` (sensitive key with a secret-shaped non-placeholder value),
   `embedded-userinfo` (URL carries `user:pass@`), `known-secret-format`
   (`sk-`, `AKIA`, `ghp_`, `-----BEGIN`, JWT, ...).
3. **The value is never printed.** Not in text mode, not in `--json`, not on
   stderr, not in an error. Before anything is written, every output line is
   checked against every parsed value (case-insensitive substring) and a line
   that would carry one is replaced with `<output line N suppressed ...>` and
   the script exits 3. A suppressed line almost always means a value happens to
   equal a key or file name; report it as such, never retry with a raw read.
4. **Bash-pipeline rule.** When the content comes from `git show <ref>:<path>`
   or any other producer, it goes into the script's stdin mode and nowhere else:

   ```sh
   git -C <dir> show <ref>:<path> | python3 -I .../scan.py - --name <path>
   ```

   Never `| head`, `| sed`, `| grep`, `| jq`, `| cut`, or into a file I then
   read. Prefer `--ref` so the script runs `git show` itself (subprocess, no
   shell). A `--name` matching the real filename drives format detection; use
   `--format` to force one.
5. **Scope the question first.** "Which secrets does X need" is answered by key
   names and the `placeholder`/`LIVE?` columns. Nearly every real question stops
   there. Say so in the answer rather than reaching for a value.

## When I still need a value

I do not. Two legitimate shapes remain, and neither puts the value in context:

- **The human runs the command.** Hand the creator the exact command and let him
  read the output on his own terminal. Record in the ledger that I asked, and
  what for.
- **Compare without printing.** When the question is "is the value in A the
  same one that is in B", test by hash or by count against a dump I never read:

  ```sh
  K=$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["Smtp"]["Password"])' appsettings.json)
  grep -c -F "$K" /path/to/other-dump     # prints a count, never $K
  printf '%s' "$K" | sha256sum | cut -c1-12   # prints a fingerprint
  unset K
  ```

  `$K` is never echoed, never put in a command I will see expanded, never
  written to a file I read, and is unset after. (This is what I did correctly
  on 2026-10-20; it is the pattern, the sed regex was the failure.)

## Reporting

Lead with the answer in key names: which keys exist, which are placeholders,
which look live, where (file:line). Include the summary line from the script.
If the guard fired (exit 3), say so and how many lines. Never paraphrase a
class into a guess about the value ("looks like a Stripe key" is as far as
`known-secret-format` goes).

## Self-test

`python3 -I scan.py --self-test` feeds dotenv, properties, JSON, SQL and YAML
fixtures carrying a sentinel and asserts the sentinel never appears in text or
JSON output, that the guard suppresses exactly the planted collision, and that
a deliberately planted leak is caught. Run it after any edit to `scan.py`.

## Known limits

Heuristics, not truth: a weak all-letters password reads as `text`; a hostname
with digits may read as `looks-like-secret`. The YAML parser is line-based
(no anchors, no flow mappings, block scalars captured as one value). JSON with
comments falls back to the generic line parser. None of that weakens the one
guarantee, which is the negative one.
