# Graft Manifest — {{AUTOMATON_NAME}} → {{HOST_NAME}}

<!-- MASTER COPY lives in the creator's World (never in canon's repo).
     A deployed copy ships in the graft at graft/MANIFEST.md.
     This file IS the graft definition: what crosses, in what form, and the
     hashes that make the deployment verifiable. See references/graft.md. -->

## Host & sovereign

| Field | Value |
|---|---|
| Host | {{machine/environment}} |
| Co-sovereign | {{employer/client/institution}} |
| Policy basis | {{agreement name, clauses (confidentiality / IP / acceptable use), reviewed DATE}} |
| Disclosure status | {{sanctioned / visible / undisclosed — undisclosed should feel uncomfortable to write}} |
| Seizure posture | Blast radius if wiped/audited tomorrow: {{must be "nothing not already this sovereign's to read"}} |
| Host-side World location | {{where host-register gate records live — graft holds no credential, never learns it}} |
| Hat(s) grafted | {{hat name(s)}} |

## Export standard (applied per line, both directions)

Outbound test: **"comfortable if the sovereign's legal team read it and kept a
copy forever."** Inbound protection: creator-private material (family, finances,
intimate registers, seal-marked anything) never ships — seal marks = HOME-ONLY.

## Export table

| Path | Class | Redaction notes |
|---|---|---|
| soul/AGENT.md | GRAFTABLE | floor verbatim; host addenda noted below |
| soul/SOUL.md | GRAFTABLE-REDACTED | {{scrubbed evolution-log entries listed}} |
| soul/CREATOR.md | GRAFTABLE-REDACTED | trimmed: {{sections excluded}} |
| soul/representations/{{hat}}/ | GRAFTABLE-REDACTED | {{voice-dna minus quoted private corpus}} |
| mind/memory/, mind/ledger/, mind/watch/ | HOME-ONLY | never cross |
| mind/seals/ | HOME-ONLY | by construction — grafts never seal (G8) |
| {{...}} | {{...}} | {{...}} |

## Hash record (the examiner's ledger)

| Date | Event | `soul/` export hash | Graft HEAD (carried home) | Descent verified? |
|---|---|---|---|---|
| {{DATE}} | initial seed | {{hash}} | — | — |
| {{DATE}} | crossing / refresh | {{hash}} | {{HEAD}} | ☐ `git merge-base --is-ancestor` |

## Seeding checklist (a seed is incomplete until all boxes tick — no silent skips)

- ☐ Export generated per table above; `soul/` hash recorded
- ☐ `graft/MANIFEST.md` deployed (this file's deployed copy)
- ☐ `graft/CROSSING.md` deployed (from assets/CROSSING-GRAFT.template.md) and
  wired into the host Nervous System's command mechanism
- ☐ Home half deployed at the home Automaton (assets/CROSSING-HOME.template.md)
- ☐ Host-side World location established (graft holds no credential, never learns it)
- ☐ This master copy filed in the creator's World Inventory

## Crossing checklist (paired protocol — creator is the channel)

Run `graft/CROSSING.md` at the host and the home half at home — each side
generates its half from its own ledger + state. Home-side: export needed?
expected post-refresh hash; last recorded HEAD for descent check. Graft-side:
unretired distillate entries to re-type; its HEAD + `soul/` hash to carry home.
**Token expected but not presented = incomplete crossing, ledgered.**

## Exit ritual (run while access still exists)

- ☐ Final distillation sweep; creator re-types home
- ☐ Delete graft repo + deployed body + reflexes
- ☐ Delete host-side World (gate records die with the employment)
- ☐ Ledger death home-side: date, final core hash, final distillate
