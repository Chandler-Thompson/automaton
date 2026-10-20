# safe-secret-scan

A core skill for every Automaton, not an Iapyx-specific one.

## Why core

An Automaton that touches a creator's repos will be asked "which config does X
need" and will reach for `grep`. The hard floor (item 6) forbids credentials in
memory, ledger, or any identity file, but a value read into context is already
most of the way there: it gets summarized, quoted back, folded into a journal.
On 2026-10-20 Iapyx proved that an ad-hoc `sed` redaction is not a control.
`scan.py` is: it prints key names, line, length and class, checks its own
output against every parsed value before printing, and ships with a sentinel
self-test. The protocol in `SKILL.md` makes the script the only path to these
files. It is stdlib-only Python 3, runs under `python3 -I`, and has no
dependency on anything else in the repo, so it can be dropped into any
automaton unchanged.

## Installing into a new automaton (automaton-creator)

Copy this directory verbatim to `mind/skills/safe-secret-scan/` in the new repo
during the skills step of the build, run `python3 -I
mind/skills/safe-secret-scan/scan.py --self-test` once and record the result
in the build ledger entry, then add one pointer line to the new AGENT.md where
it lists mechanical gates (next to the send-lint line in Layer 6, or the
equivalent tooling section). Proposed line, for the creator to place:

```
- **Config and secrets files are read only through
  `mind/skills/safe-secret-scan/scan.py` (python3 -I), never raw** — `.env`,
  `appsettings*.json`, `*.properties`, `secrets.yml`, `*.tfvars`, `init.sql`,
  compose env blocks, and `git show` of any of them. Protocol in
  `mind/skills/safe-secret-scan/SKILL.md`. (Iapyx, 2026-10-20: a sed redaction
  missed a field and live SMTP creds landed in context.)
```

Do not edit AGENT.md from inside this skill; the floor and the contract are
creator-side changes.

## Files

- `SKILL.md` — the protocol (trigger phrases in the frontmatter).
- `scan.py` — the scanner; `--self-test` is the proof it never prints a value.
- `README.md` — this file.
