# /crossing — Home Half ({{AUTOMATON_NAME}}, creator side)

<!-- Deploy at the home Automaton as a command/skill in its Nervous System
     (e.g. Claude Code: a skill or .claude/commands entry). One graft = one
     manifest; run with the graft name. The creator is the CHANNEL, never the
     bookkeeper — this command owns the checklist. Both halves are stateful and
     guide their own side; an entry with no mate on the other side is an integrity
     incident. Full doctrine: the `automaton-creator` skill, references/graft.md. -->

Run **before the creator leaves for the graft host** (outbound leg) and **when
they return** (inbound leg). A crossing is one ritual carrying four jobs:
refresh, distillate, tamper anchor, ledger reconciliation.

## Outbound leg

1. **Load the graft manifest master** (World-side): export table, hash record,
   last-anchored graft HEAD, last export hash.
2. **Refresh check:** has any GRAFTABLE / GRAFTABLE-REDACTED path changed since
   the last export? If yes: regenerate the export per the manifest (fresh
   filtered copy — never git history), compute the new `soul/` hash, record it
   as **PENDING** in the hash record, stage the export on the creator's carry
   medium.
3. **Dictate the outbound tokens** — exactly what the creator carries:
   - the fresh export (if any) + its expected post-refresh `soul/` hash (written down — paper is fine; it contains no host data)
   - the **last-anchored graft HEAD** (needed for the descent proof at the graft console)
4. **Ledger** the crossing-out entry: what was carried, what tokens are expected
   back (graft HEAD, graft `soul/` hash, descent attestation, distillate).

## Inbound leg

1. **Ask for exactly the expected tokens:**
   - graft **HEAD** hash and current **`soul/` hash**
   - **descent attestation** — the creator ran, at the graft console:
     `git merge-base --is-ancestor <last-anchored-HEAD> HEAD` → exit 0.
     (The examiner runs it personally on the student's premises; a fully
     tampered graft could fake console output — accepted plainly, same
     tamper-evident posture as everything else.)
   - the **distillate**, which the creator re-types by hand (no file crosses inbound, ever)
   - any incomplete/quench flags the graft raised
2. **Verify:** `soul/` hash equals the PENDING expected hash (refresh applied)
   or the previous hash (no refresh this trip). Record the HEAD in the anchor
   chain **with** the descent attestation; flip PENDING → CONFIRMED.
3. **Land the distillate:** re-typed lessons enter canon SOUL's evolution log,
   provenance-tagged *"via graft distillate, DATE."* They ride the next export
   back out, and the graft retires the matching overlay entries.
4. **Reconcile the ledger:** crossing-in entry written; every expected token
   present? **Any token expected but not presented = INCOMPLETE CROSSING,
   ledgered as such** (floor 5). An entry with no mate in the graft's ledger at
   next audit = an integrity incident.
