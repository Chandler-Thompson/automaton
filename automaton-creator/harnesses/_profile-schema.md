# Harness profile schema

Every file in this directory that describes a Nervous System must answer the
sections below. Profiles are recipes for humans and agents; they are not part of
the Automaton's floor or soul.

Omit nothing. If a section does not apply, write **N/A** and why.

## Identity

- **Harness id** — short slug used in `body/ANATOMY.md` (e.g. `claude-code`, `cursor`)
- **Display name** — human-facing product name
- **Provenance** — how far this profile has been exercised (proven / provisional / checklist-only)

## Creator skill install

How a human installs `automaton-creator` so the harness will run the build process.

- Personal / user-global skill path
- Project-scoped path (if any)
- Symlink vs copy; Windows junction note if relevant
- How the skill is invoked (trigger phrases, auto-discovery, explicit mention)
- Paths that must **not** be used (reserved directories)

## Built Automaton deploy

How a finished Automaton repo is wired into this Nervous System.

- Where the harness reads the agent contract
- Symlink vs copy preference for `soul/AGENT.md` (zone path always governs)
- Typical deployment-alias table (left: harness-local name; right: zone path)
- How session-open / heartbeat is expected to run
- How Crossing (and similar commands) are exposed — skill, slash command, rule, chat phrase
- What this harness **cannot** enforce (e.g. HANDS rungs at the tool layer) — creator compensates via ledger + ratification

## Limits and honesty

Anything a creator must know before treating this profile as equivalent to another.
Do not claim parity with a proven path until a real Phase 1 has passed on it.
