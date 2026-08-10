# Harness profile: generic

- **Harness id:** `generic` (or a short slug the creator invents, recorded in ANATOMY)
- **Display name:** Any agent harness that reads Markdown contracts
- **Provenance:** Checklist-only — fill in during Phase 0/1; do not invent vendor
  SDKs into the Automaton repo.

Use this when the Nervous System is not Claude Code or Cursor, or when the
creator is still choosing. Doctrine in `references/procedures.md` still applies:
symlink-or-copy Soul, alias map, wire Senses/Hands, rebuild Reflexes, run the
Phase 1 acceptance check.

## Creator skill install

- **Personal / user-global skill path:** {{where this harness loads skills or
  instruction packs}}
- **Project-scoped path:** {{if any}}
- **Symlink vs copy:** Prefer symlink/junction of `automaton-creator/` so updates
  to the clone flow through. Windows: junctions are fine when symlinks need
  elevation.
- **Invocation:** {{how the creator starts the build — phrase, slash command,
  menu}}
- **Do not use:** {{reserved paths, if any}}

If the harness has no skill system, the creator can open this repo (or the
`automaton-creator/` folder) in context and paste the trigger phrase; the skill
files remain the process source of truth.

## Built Automaton deploy

Answer each item in `body/ANATOMY.md` when done:

1. **Contract path** — Where does the harness read the agent contract? Deployed
   copy is an alias of `soul/AGENT.md`, never a second source of truth.
2. **Symlink or copy?** — Prefer symlink; if copy, record re-copy-on-Soul-change.
3. **Alias table** — Every flattened or renamed path: harness-local name → zone
   path. Zone path governs.
4. **Session-open / heartbeat** — How does a new session run the contract's
   open sequence? Automate if the harness allows; otherwise the creator runs it
   by prompting.
5. **Crossing / commands** — What command mechanism exists (skill, slash
   command, rule, chat phrase)? Wire home and graft halves there.
6. **Senses / Hands** — Connect each grant; demonstrate both command channels;
   confirm newborn Hands are present and refused, not absent.
7. **What the harness cannot enforce** — List it. Typical: rung ceilings,
   quench, credential isolation. Compensations: Registry checks at use time,
   ledger, World Inventory, creator ratification.

## Limits and honesty

A filled generic profile is a map of one embodiment, not a promise that the
harness is equivalent to Claude Code or Cursor. Re-embodiment onto a named
profile later is encouraged once one exists.
