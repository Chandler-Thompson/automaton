# ANATOMY.md — {{AUTOMATON_NAME}}'s embodiment map

<!-- body/ANATOMY.md — the BLUEPRINT of the current Body, never the Body itself.
     The running Body (harness install, DBs, gateways, live credentials) lives
     outside the repo and is deployed from this file. No secrets — floor 6. -->

## Body Facets (current embodiment)

| Facet | Current | Notes |
|---|---|---|
| **Brain** | {{MODEL e.g. best available Claude}} | The Brain runs, the Mind is data — swap freely |
| **Nervous System** | {{HARNESS e.g. Claude Code}} | Runtime that carries signals; reads this repo |
| **Heartbeat** | {{PRESENCE_RUNG: session-only / pulses / event-wake}} | Presence is earned (ladder); pulse cadence per Charter |
| **Senses** | see [SENSES.md](SENSES.md) | Read-connections; injection surface (floor 4) |
| **Hands** | see [HANDS.md](HANDS.md) | Act-connections; the ladder bites here |
| **Reflexes** | {{STORES e.g. none / SQLite FTS index}} | Reflex Rule: always rebuildable from mind/, never authoritative |

## Reflex rebuild

<!-- For each Reflex, the command/recipe that rebuilds it from the Mind repo.
     If a Reflex can't be rebuilt from canon, it is holding canon — fix that. -->

- {{REFLEX}}: {{rebuild command / recipe}}

## Environment

- Machine/OS: {{ENVIRONMENT}}
- Repo (canonical Automaton): {{REPO_PATH}} — remote: {{REMOTE_NAME_ONLY, creator-controlled — see World Inventory}}
- Deployed Soul copy: {{DEPLOY_PATH e.g. harness agent folder}} (redeployed from soul/ at install)
- Raw corpus working area (outside repo): {{INGEST_PATH e.g. ~/.automaton-ingest/}}
- Calibration records (NEVER READ): {{LOCATION_REFERENCE_ONLY}}
- Sealed held-outs (NEVER READ): {{LOCATION_REFERENCE_ONLY}}

## Integrity

- Floor hash: anchored in the World; authoritative check is World-side.
- Session-open reflex: verify deployed floor vs soul/AGENT.md; on mismatch →
  **quench to WATCH** (suspend ACT/JUDGE), ledger, notify creator, await re-anchor.
- Re-anchor handoff: a moved hash is presented to the creator as an explicit
  task (what changed, new commit hash + file hash + date, the creator's
  re-anchor steps); re-surfaced every session open until confirmed.

## Known gotchas

- {{GOTCHA_1}}
