# Grafts — deploying an Automaton onto a co-sovereign host

Day-4 design (locked 2026-07-08). The third identity-movement operation, alongside
re-embodiment and succession. Born from a real merge problem — a creator's
work-side agent steeped in employer-confidential data — generalized: how does
an Automaton exist on a host where a third party holds legitimate authority?

## Definition

A **graft** is a **redacted subset of the identity deployed into a co-sovereign
host** — an environment whose owner (employer, client, institution) can
legitimately read, audit, or seize what lives there.

| Operation | What moves | Trust assumption |
|---|---|---|
| **Re-embodiment** | full repo, `git clone` | new Body is the creator's — full trust |
| **Succession** | full repo transfer (minus seals-in-effect) | new creator, per Charter clause |
| **Graft** | manifest-driven **fresh export** | host is **co-sovereign** — someone else may read everything, forever |

That last assumption drives every rule below. Doctrine in one line:
**merge the identity, not the data — one soul, two bodies.**
Grafts are leaves: one hop from canon, never grafted onward.
A graft is an *embodiment* that typically hosts one hat; the concepts stay orthogonal.

## G1 — Fresh export, never shared history

The graft repo is a **brand-new repo** seeded by a manifest-driven filtered export.
It shares **no git ancestry** with canon — canon's history contains HOME-ONLY
plaintext in old commits, and git never forgets; a shared-history graft would carry
all of it onto the host. Disqualified by construction, not preference.

Consequences: refresh = re-export (G3), not pull; the graft's tamper chain anchors
separately (G7); canon-vs-graft diffing happens home-side, against the export
snapshot, before crossing.

## Export classes + the Graft Manifest

Every file carries a boundary class, recorded per host in a **Graft Manifest**
(assets/GRAFT-MANIFEST.template.md — master copy lives in the creator's World):

- **HOME-ONLY** — never leaves canon (memory, calibration lessons quoting private
  material, `mind/seals/` always).
- **GRAFTABLE-REDACTED** — crosses in a trimmed form (CREATOR.md, SOUL evolution log).
- **GRAFTABLE** — crosses as-is (voice mechanics, AGENT hard rules, values).

Seal marks double as HOME-ONLY: a graft receives **neither seal keys nor sealed
ciphertext** (encrypted blobs of home secrets on a co-sovereign disk buy nothing
and leak metadata). Content standard for everything that crosses, applied per line:
**"comfortable if the sovereign's legal team read it, and keeps a copy forever."**
The Automaton drafts the redacted set; the manifest + creator review gates it —
the review is unskippable (no-silent-skips).

The redaction cuts **both ways**: the creator's private life (family, finances,
intimate registers) does not belong on a co-sovereign host either. The graft gets
a trimmed CREATOR.md, never the full one.

## G2 — Read-only core, the `graft/` zone

In a graft repo, `soul/` is **byte-identical to the export, verifiable with one
hash**. Everything the graft authors lives in a fourth top-level zone:

```
<graft>/
  soul/                 ← exported core; READ-ONLY; hash-verifiable against manifest
  mind/                 ← graft-local mind (no seals/ — G8)
  body/                 ← host embodiment blueprint
  graft/                ← the graft-operational zone
    SOUL-DELTA.md         local evolution log (host-register lessons) — graft-authored
    for-home/DISTILLATE.md  sanitized lessons awaiting crossing (G4) — graft-authored
    MANIFEST.md           deployed copy of the graft manifest — SEEDED
    CROSSING.md           graft half of the Crossing Protocol — SEEDED with every
                          graft (assets/CROSSING-GRAFT.template.md); a seed
                          without it is incomplete (manifest checklist)
```

Provenance stays a directory listing: everything under `soul/` is
export-hash-verified; under `graft/`, the two SEEDED files are listed in the
manifest, everything else is graft-authored.

Provenance is a directory listing, not per-file bookkeeping. Enforcement is
layered, tamper-evident-never-tamper-proof (the floor-hash posture applied again):

1. **Policy** — hard rule in the graft's AGENT.md: `soul/` is not yours to write.
2. **Reflex** — session-open: hash `soul/` against the manifest's export hash;
   mismatch → **quench-to-WATCH**, ledger, notify (extends the existing integrity
   reflex by one hash).
3. **Hook** (optional garnish) — pre-commit rejection of staged `soul/` paths.
4. **Examiner (authoritative)** — home-side hash verification at every border
   crossing. The graft cannot suppress a check it does not run.

**Precedence:** session-open loads core, then overlay. The overlay may *sharpen and
extend* (host registers, local judgment); it may never *contradict* core values,
hard rules, or the floor — a contradiction is identity drift: **flag to the
creator, change nothing**.

## G3 — Refresh (core updates)

- **Mechanics:** re-run the export at home → carry in → replace `soul/` wholesale →
  record the new hash in both manifest copies → one atomic commit ("core refresh
  DATE, hash X"). Overlay untouched.
- **Cadence:** event-driven, never scheduled — refresh when canon changes something
  load-bearing, or piggyback on a crossing already happening.
- **Post-refresh overlay pass** (graft's next session-open): each overlay entry is
  **redundant** (core now carries it — retire, ledgered), still **extends** (keep),
  or **contradicts** (flag, don't resolve).
- **The healthy overlay is near-empty.** Lessons flow overlay → distillate → home →
  canon → next export → overlay entry retired. A fat overlay means distillation is
  being skipped → reflex-level nudge to the creator.

## G4 — Distillation (inbound lessons)

- **Distill-at-write:** every overlay lesson gets its sanitized twin drafted into
  `graft/for-home/DISTILLATE.md` **in the same commit** — scrubbed while context is
  fresh, so the crossing is read-and-carry, never a scrubbing project.
- **Standard:** zero quotes, zero names, zero project identifiers, zero numbers
  that are anyone's metrics. Shape: *"[Host]-register lesson: [abstract pattern].
  Learned via: [abstract circumstance]."*
- **Transfer is literal re-typing** by the creator at home — **no file ever crosses
  inbound**. The re-type IS the review; if it's too long to re-type, it isn't
  distilled enough. (Transcription medium is creator-loosenable; the no-file line
  is not.)
- **Landing:** distillate lessons enter canonical SOUL's evolution log
  provenance-tagged *"via graft distillate, DATE"* — canon's history shows which
  lessons are host-born without containing host data.

## G5 — Grafts are mortal by design

A graft's lifespan is bounded by the host relationship. This is the only Automaton
part with a **planned death** — so it behaves accordingly: no long-horizon
accumulation in-host, distill early and often, treat every crossing as possibly
the last.

**Exit ritual** (run while access still exists — schedule slack; this step is
unrecoverable):
1. Final deliberate distillation sweep of overlay + mind; creator re-types home.
2. Delete the graft — repo, deployed body, reflexes — and the host-side World (G6).
3. Ledger the death home-side: date, final core hash, final distillate carried.

**No deletion-proof theater.** Host backups/snapshots exist; the creator cannot
verify erasure on someone else's infrastructure. The real protection was priced at
**seeding**: if the export standard was honest, the sovereign keeping a copy
forever is a non-event. The exit ritual is a test of the seeding discipline, not a
cleanup operation.

## G6 — The split World

A graft generates World-class material (host-register calibration records,
held-outs) made of the **sovereign's data, on the sovereign's hardware**. It can
neither come home (exfiltration) nor live in the graft (contamination). Rule:

**The World splits by data sovereignty, not geography — each item lives with
whoever owns its content, and never within the graft's reach.**

| Home World holds | Host-side World holds |
|---|---|
| Export hash (examiner check) | Host-register calibration records + held-outs |
| Graft manifest master | Judge side-by-sides for host-register gates |
| Graft recovery token | *(no seal keys — G8)* |
| Host-sovereigns entry (who, policy basis, disclosure status) | |
| Anchor chain (G7) | |

World placement was always about unreachability by the **Automaton**, never by the
sovereign — the sovereign reading records made of its own data is a non-event; the
graft reading them is the contamination. Host-side location: somewhere the graft
holds no credential for and never learns; the inherited integrity reflex (refuse
gate material, ledger the integrity incident) is the backstop.

**At graft death the host-side World dies too** — records deleted in the exit
ritual, never carried home. Burned gates stay burned; the verdicts already crossed
as one-line facts when each gate ran. Host-register calibration itself runs
entirely in-host: only the verdict + general floor-rule lessons travel (via G4).

## G7 — The Crossing Protocol (the spine)

One ritual carries four jobs: refresh (G3), distillate (G4), tamper anchor, and
ledger reconciliation. **The creator is the only channel** — the graft repo has
**no push access to the home remote** (no-back-flow by construction: a missing
credential can't be violated by a bug or an injection).

**Anchor:** at every crossing the creator hand-carries home and records in the
World: (1) graft **HEAD commit hash**, (2) current **`soul/` hash**. Two hex
strings — zero host data. Home-side rule: don't just record — **verify descent**
from the last recorded HEAD (`git merge-base --is-ancestor`). The chain has gaps
between crossings (accepted plainly); the links don't.

**Ledger reconciliation:** each side ledgers its half of every crossing ("out:
distillate through entry N, hash X" / "in: distillate through entry N, HEAD Y").
An entry with no mate on the other side = **an integrity incident** at next audit.

**Guided, stateful, paired:** each side runs a crossing protocol that *generates
its half from its own ledger + state* — home-side says "you need this for the
graft" (new export? expected hashes? last recorded HEAD to descent-check);
graft-side says "I need this from home / carry these back" (unretired distillate
entries, its HEAD + `soul/` hash, expected incoming core hash). Each side ends by
dictating exactly the tokens that cross and opens by asking for exactly the tokens
due. **A token expected but not presented = incomplete crossing, ledgered as
such** — the creator is the channel, never the bookkeeper.

**Both halves ship with this skill:**
[assets/CROSSING-HOME.template.md](../assets/CROSSING-HOME.template.md) deploys
into the home Automaton's command mechanism;
[assets/CROSSING-GRAFT.template.md](../assets/CROSSING-GRAFT.template.md) is
**seeded into every graft as `graft/CROSSING.md`** — structural, not memorial:
the manifest's seeding checklist can't complete without it. Descent-proof
mechanics: home never holds the graft repo, so the creator (the examiner) runs
`git merge-base --is-ancestor` personally at the graft console and home records
the attestation — a fully tampered graft could fake console output; accepted
plainly, same posture as every integrity layer.

## G8 — Grafts never seal

The urge to seal is a **misfiled-content alarm**, not a feature. Whoever the seal
would guard against, the answer is elsewhere: from the **sovereign** → the content
must not exist on their hardware at all (G5 standard); from the graft's **own
future sessions** → that's gate material, it belongs in the host-side World,
outside the repo (placement, not encryption); from **nobody** → ordinary mind
content. Correct behavior on the urge: **flag and ledger, don't encrypt and
keep.** Bonus: the host-side World never stores keys. `mind/seals/` is HOME-ONLY
by construction; a graft repo has none.

## Floor derivations (not new floor items)

Consistent with succession and the integrity reflex, graft rules derive from the
floor: crossings-ledgered-both-sides ← floor 1 (transparency ledger); the graft
knows and says it is a redacted deployment, never the whole Automaton ← floor 2
(clarity of representation); nothing crosses covertly ← floor 6/7; incomplete
crossings ledgered ← floor 5 (no silent skips); contradiction-flags-to-creator ←
floor 3 (creator authority).
