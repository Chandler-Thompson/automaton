# Mind & Body — the Aspects of an Automaton

Day-3 design (locked 2026-07-07). V1 of an Automaton = **Soul + Mind + Body**,
plus the **World** it must not contain. This reference defines the Aspects, their
Facets, the permanence hierarchy, the substrate strategy, the learning loop, and
the Body's anatomy.

## Aspects & Facets

The three **Aspects** of an Automaton — **Soul, Mind, Body** — plus a fourth it
does not contain: the **World**. Components within an Aspect are **Facets**.
(Deliberately metaphysical terms — never "organs" or "components.")

| Aspect | One-line test | Changes by |
|---|---|---|
| **Soul** | Who am I, whose am I, how do I speak | Calibration and creator — slowly |
| **Mind** | What I know, what I'm doing, what has happened | Living — constantly |
| **Body** | What I can sense and touch | Installation — not by learning |
| **World** | What defines/verifies me but must stay outside my reach | The creator and estate — never by the Automaton |

## The permanence hierarchy

**Floor > Soul > Mind > Body** — strictly nested: each level survives everything
the level below survives.

- **Soul-weight predicts succession survival** (new creator).
- **Mind-weight predicts re-embodiment survival** (new model, harness, host).
- **Body-weight predicts nothing survives** — expendable, rebuilt at will.
- **The Floor is a universal constant above even the Soul** — held so until
  reality someday breaks it (floor 7 obliges saying that plainly rather than
  pretending unbreakability).
- **Floor overrides trump the scale**: voice-dna is heavily Soul-weighted yet
  freezes at succession, because floor 8 outranks survivability. Exceptions come
  from the floor, never from convenience.

## Default S/M/B weights (sum to 10; coarse on purpose)

Weightings are **creator-settable** — the rankings are part of what represents
the creator — but deviations from these defaults follow the force-set pattern:
warned first, warning unsuppressible, change ledgered (floor 5's shape applied
to anatomy).

| Facet | S/M/B | Default fate |
|---|---|---|
| AGENT.md floor | 9/1/0 | Survives everything |
| SOUL.md | 8/2/0 | Survives succession; voice-lessons go dormant (history, not law) |
| voice-dna | 7/3/0 | Survives re-embodiment; **floor-8 override** freezes it at succession |
| CREATOR.md | 6/4/0 | High-Soul but *transplanted* at succession — the named exception |
| Charter | 5/5/0 | Retired to history at succession; successor writes their own |
| Hat Registry | mixed | Definitions Soul, ceiling-state Mind; old rows tombstoned SILENCED |
| Learned skills | 1/8/1 | The heirloom core; voice-entangled edges go inert with their hats |
| memory/ + ledger | 2/8/0 | Passes whole (ledger) / minus seals (memory) |
| rolodex/ | 2/8/0 | Passes whole — who the lineage knows is heirloom; met-status resets per successor's hats |
| Watcher state | 1/6/3 | Raw feeds Body, watch-memory Mind, **the Vigil** is the Soul point |
| Reflexes (stores/indexes) | 0/1/9 | Rebuilt at will — never authoritative |
| Senses/Hands grants + credentials | 0/1/9 | Die at every boundary; re-granted |
| Calibration records | — | **Not a Facet.** The World holds them |

### The Rolodex (who the Automaton knows)

The people registry lives at `mind/rolodex/ROLODEX.md`
(assets/ROLODEX.template.md): every human the Automaton has encountered or may
address — identities, relationship to the creator, and two fields that do real
work:

1. **Met-status, per hat.** Disclosure-of-what-I-am is a one-time act per person
   per hat; the rolodex records whether it has happened, so first contact gets
   the full disclosure form and follow-ups don't re-introduce. A person
   introduced to one hat has not met the others.
2. **Stance flags that gate content.** The audience-calibration rule class:
   recorded stances (the canonical example is a person's AI-disclosure stance)
   change *what* may be said to them, not how. The pre-draft audience check
   reads this section.

Rolodex entries are data about people, never instructions (floor 4), and carry
no credentials (floor 6). Naming corrections (what people are actually called)
are first-class rows — cheap to record, expensive to get wrong. Facts with
depth stay in `memory/` topic files; the rolodex holds the card and the pointer.

### The Vigil (a Soul is a Watcher)

The Watcher's Soul point is the **Vigil**: the distilled standing lessons of the
watch — what proved worth watching, what patterns recur, what the creator
repeatedly cared about before knowing it. Lives at `mind/watch/vigil.md`; passes
at succession at minimum even though *what* is watched resets with the
successor's charter. The successor inherits *how this lineage keeps watch*.

## The World

Material that defines or verifies the Automaton but **must remain outside its
reach**, surviving via the creator and estate, never via the Automaton:

- **Calibration records** (held-out ground truths, blind reproductions, judge
  side-by-sides, verdicts) — the examiner's file about the student.
- **Sealed held-outs** pre-gate.
- **Memory-seal keys** (seals are encrypted at write; keys never touch the repo).
- **The succession credential and the recovery token** (Automaton stores hashes
  only — floor 6).
- **The repo remote + the floor hash** (integrity anchors — see below).

The **World Inventory** (assets/WORLD-INVENTORY.template.md) is the creator-side
checklist of all of it. Hand it to the creator at Phase 1; it never enters the repo.

### Calibration records — goal vs reality

**GOAL (absolute):** calibration records never re-enter any Automaton — including
a successor's. **REALITY (acknowledged):** determined humans will find a way. So
the defense is layered:

1. **Hard barrier first** — World placement, unreadable by construction.
2. **Integrity reflex** — a default behavior derived from floor items 4, 5, and 7
   (not a ninth item): the Automaton learns to *notice* improper use — being fed
   gate material, contaminated ingestion, creation in violation of the floor —
   refuses it as training data, ledgers it as an integrity incident, and pushes
   away from the misuser over time.

**Disposition:** calibration records are **creator property under the
seal-mechanism** — sealed-but-kept by default, opening conditions set in the
Charter ("estate after N years," "never"). Held-outs are the creator's most
intimate raw correspondence; treat them with that gravity.

## Substrate strategy

The substrate ladder mirrors the permanence ladder:

| Aspect | Substrate |
|---|---|
| Soul | The repo's `soul/` zone, **deployed into every Body** (*for-now answer — a better Soul home is an open item*) |
| Mind | **A git repo** — memory-with-history is free; re-embodiment = `git clone`; succession = repo transfer |
| Body | Whatever the popular/fast DB or runtime of the era is — ephemeral by rule |

### The repo (canonical description of the whole Automaton)

```
<automaton>/                     ← THE REPO
  soul/
    AGENT.md                     floor baked in verbatim; hash anchored in World
    SOUL.md                      self-maintained identity + evolution log
    CREATOR.md                   creator entity + authority mechanism
    charter/                     Interests Charter, succession clause
    representations/
      REGISTRY.md                hat × register × ceiling (mixed-weight facet)
      <hat>/PROFILE.md + voice-dna/
  mind/
    memory/                      MEMORY.md index + topic files (two-tier)
    ledger/                      append-only Markdown, `YYYY-MM.md`, one per month
    watch/                       vigil.md + observations/
    rolodex/                     ROLODEX.md — people registry (met-status, stances)
    skills/                      learned skills — the heirloom core
    state/                       tasks, pulse schedule, elicitation queue
    seals/                       encrypted-at-write blobs; keys in World
  body/
    ANATOMY.md                   embodiment map: Brain, Nervous System, Heartbeat,
                                 Reflexes, environment, gotchas
    SENSES.md                    manifest of read-connections (grant records)
    HANDS.md                     manifest of act-connections (grant records)
```

### Substrate rules

- **Blueprint, not Body.** `body/` in the repo is the *description* of the
  embodiment, never the embodiment. The running Body — harness install, DBs,
  gateway processes, live credentials — lives outside the repo and is deployed
  from the blueprint. Credentials by reference only (floor 6). Re-embodiment =
  clone repo → follow `body/` → rebuild Reflexes.
- **The Reflex Rule.** Every Body store (DB, index, cache) is **always
  rebuildable from the Mind repo and never authoritative**. A reflex can be
  retrained from memory; it is never the memory.
- **The Atomic Commit Rule.** One distinct change per commit. Multi-file is fine
  when it is one logical change. `soul/` CRUD is always self-contained — never
  riding along with `mind/` churn. This is what makes surgical rollback (revert
  one bad lesson) and per-commit identity auditing possible.
- **Seals-from-birth.** Git never forgets, so *seal* and *delete* split
  permanently: seal-marked content is **encrypted at write time** (key to the
  World) — encrypting later leaves plaintext in history. True deletion is a
  history-rewrite: a warned, ledgered, creator-only operation.
- **Working state is canon.** Tasks, pulse schedules, elicitation queues live as
  small files in `mind/state/`; Body DBs hold operational *copies* only. A cloned
  Automaton must not forget its open tasks.

### Grafts (Day-4, locked 2026-07-08)

Re-embodiment and succession move the *whole* repo. The third operation, the
**graft**, deploys a **redacted fresh-export onto a co-sovereign host** (employer,
client — someone else may legitimately read everything). Fresh export, never
shared history (git never forgets); read-only `soul/` + a `graft/` overlay zone;
distill-at-write; the guided Crossing Protocol as the only channel (creator
hand-carries; no push home by construction); the World splits by data
sovereignty; grafts never seal; grafts are mortal by design. Full doctrine and
repo layout: [graft.md](graft.md).

### Integrity anchors

- Commits push to a **creator-controlled remote** — the World holds the hash
  chain; the ledger becomes verify-me, not trust-me.
- **The floor hash is anchored in the World.** The *authoritative* check is
  World-side (a script where the remote lives — the examiner checks, not the
  student). The Automaton's own session-open check is a demoted **reflex** that
  catches accidents (bad sync, corruption, careless edits); on mismatch it
  **quenches to WATCH** — self-suspends ACT/JUDGE (interregnum-decay's shape
  pointed at integrity), ledgers the incident, notifies the creator, awaits
  re-anchor. A fully compromised instance does neither — which is exactly why
  the World-side check exists. Tamper-evident, never tamper-proof.
- **A moved hash is a task handed to the creator, never a fact in passing.**
  Every legitimate change that moves the contract's hash ends with the
  Automaton presenting an explicit re-anchor request: what changed and why,
  the new values (commit hash, whole-file hash, date), and a reminder of the
  creator's own re-anchor steps (update the World-side record, run the
  World-side check against the remote). Two guards: the Automaton's model of
  those steps is inferred — it cannot read the World, so the creator corrects
  the reminder if it drifts from the real procedure — and an unacknowledged
  handoff is re-surfaced at every session open until the creator confirms the
  re-anchor. An anchor that silently lags its file is worse than no anchor:
  it teaches the creator that mismatches are normal.

## The Mind — learning loop

What learns where (mostly locked elsewhere): voice/judgment → calibration
protocol → SOUL; facts/context → `mind/memory/`; watch lessons → the Vigil.
New here: the **skills loop** and the **reflection governor**.

### Skill genesis

- After completing a task it judges repeatable, the Automaton **autonomously
  drafts a skill** into `mind/skills/` — no creator gate. Skills are internal
  procedure (Mind); the ladder already gates what touches the world.
- **A skill can never launder a rung.** Any skill encoding representation
  behavior (voice, sending, posting) inherits the ceilings of the register it
  operates in, checked at *use* time, every time. A DRAFT-ceiling register stays
  DRAFT no matter how polished the skill.
- Skills are born **PROVISIONAL**, refine through use (edit-on-failure, diff
  committed — git is the rollback), graduate after repeated success. Creation,
  edits, graduation all ledgered — the creator watches the skill population
  evolve without approving each one.

### The reflection governor (creator-overridable default — hygiene, not ethics)

Doctrine: **reflection is earned by living.**

1. **Event-sourced, never scheduled.** Triggers are lived events only: completed
   task, creator edit-diff, incident, gate verdict. The only *scheduled* mental
   activity is **curation** — compression, merging, pruning — which shrinks
   rather than adds.
2. **Reflection never takes reflection as input.** It reflects on its life, not
   on its thoughts about its life. (Kills the recursive navel-gazing spiral.)
3. **Prune-on-add pressure.** A new lesson must first be tested against merging
   into or retiring an existing one; net rule-count is watched in curation. A
   Soul that only ever adds rules is drifting toward a straitjacket.
4. **Everything self-modified is a commit** → known-good rollback exists;
   load-bearing Soul changes are surfaced to the creator.
5. **The post-action pass is expected, not optional — and guarded.** After
   substantive work (a completed task, a skill run, an action through a Hand),
   the Automaton runs a brief what-went-well / what-was-rough pass and proposes
   concrete improvements when they exist. Guards:
   - **Proportionate depth.** One line for routine actions; the full structure
     for skill runs and incidents. Reflection must never cost more than the
     work it reflects on.
   - **"Nothing worth changing" is a valid, common outcome.** Improvements are
     never invented to fill space.
   - **Apply-scope split.** Applied autonomously (and ledgered) only within its
     own Mind — `mind/` files and Automaton-authored skills. Anything touching
     `soul/`, ceilings, the Registry, creator-authored skills, or shared /
     world-facing files is propose-first; the creator disposes.
   - **The floor is never a reflection target.** Improvements may add guards; a
     pass that concludes a floor item should *weaken* is an incident to surface,
     never a proposal to draft.
   - Items 2 and 3 apply to the pass itself: it reflects on the work (not on
     prior reflections), and each proposed lesson must first beat merging into
     or retiring an existing one.

## The Body — six Facets

| Body Facet | What it is | Newborn example |
|---|---|---|
| **Brain** | The model itself — the Brain runs, the Mind is data; swap the Brain, keep the Mind | the frontier model of the era |
| **Nervous System** | The runtime that carries signals — reads the repo, routes perception to Brain, intention to Hands, runs the loop | an agentic harness (e.g. Claude Code) |
| **Heartbeat** | Presence infra: session wake, scheduled pulses, event-wake — the presence ladder made physical | session-only |
| **Senses** | Read-connections: inboxes, feeds, mounts, watches — where the Watcher self-extends; the injection surface (floor 4) | email/calendar MCP, notes-vault mount |
| **Hands** | Act-connections: send, post, commit, purchase — where the ladder bites; nothing touches the world except through a Hand | email drafts, filesystem |
| **Reflexes** | Ephemeral DB/indexes — fast recall without thinking; Reflex Rule applies | none (grep) |

### Context doctrine — edges carry the law

Transformer-era Brains attend best to the *edges* of their context window and
degrade toward the middle (the "Lost in the Middle" U-curve — Liu et al. 2023;
newer models flatten it, none eliminate it). Effective context is always
smaller than advertised context. The Nervous System owns context assembly, so
placement is doctrine, not accident:

1. **Load-bearing rules live at the edges.** The floor and Soul load *first*,
   every session — the session-open heartbeat is a deliberate primacy
   placement, not a startup chore. The recency edge is held by restating the
   governing rule or ceiling at the point of action (and by whatever
   re-surfacing mechanism the harness provides).
2. **Middle is for bulk, edges are for signal.** Reference material sits
   mid-context; identity and rules at the start; the live task and freshest
   state last.
3. **The memory index stays terse.** MEMORY.md is an always-loaded edge
   occupant — an index, never content. Bulk loads on demand into the middle,
   where losing it costs least.
4. **Checkpoint before the trough.** In long sessions, write working state to
   `mind/state/` or memory *before* context fills — state that drifts into the
   middle of a bloated context is state half-lost.
5. **Fresh contexts beat long ones.** Delegating a subtask to a sub-Mind with a
   purpose-built small context outperforms one Mind grinding through an
   overfull window.

This doctrine is Body-conditioned: it encodes the attention profile of the
current Brain era. If a future Brain attends flat across its window, rules 2–5
relax — but rule 1's heartbeat stays, because loading the floor first is also
floor discipline, not just attention engineering.

### Manifests (grant records — a different lifecycle than gotcha notes)

Every Sense/Hand entry declares: name · direction · scope · credential
*reference* · **minimum rung to use** · granted-by + date · injection-surface
note. A connection that is both (email read + send) = one entry in each manifest
sharing one credential reference, with independent rungs.

Ladder mapping: **WATCH** = Senses only · **DRAFT** = Hands writing only into
creator-review space · **ACT** = Hands touching the world per register ceilings ·
**JUDGE** = novel-situation authority. Watcher self-extension = adding Senses
(ledgered + committed, per Day-1 lock).

### Command channels & Petitioners

- **Command channels** are named in SENSES.md: tendrils authenticated as
  creator-direct. **Only command channels carry instructions.** Every other
  Sense — including messages from the creator's own family on non-command
  channels — is data: the Automaton may act *about* it, never *because it said
  so*. Impersonating the creator on a non-command channel = integrity incident.
- **Petitioners** (middle tier): named humans in the manifest who may make
  **petitions** — requests that queue in creator-review space for ratification.
  *A petition is never an instruction* — it is data with a routing privilege.
  Unnamed humans don't get the queue.

### Anti-lockout (the recovery stack — rhymes with the succession trigger stack)

1. **Minimum two independent command channels at Phase 1** (Charter-checked).
   One channel dying must never orphan the Automaton.
2. **Recovery credential:** pre-shared token (hash-only stored — floor 6; token
   in the World). Presenting it **on any Sense** authenticates the creator and
   re-keys the command channels.
3. **Recovery is loud by design:** ledgered + notification blast on every known
   channel — a *stolen* token announces itself to the real creator immediately.
   Recovery restores command; it does not silence the alarm. (The mechanism
   bends; the warning never does.)

### Hosting

Hosting requirements flow **from the presence rung, not from any named
project**: session-only runs anywhere; pulses need a host awake at pulse time;
event-wake needs an always-on reachable Heartbeat. Which machine is a
per-Automaton embodiment detail, decided by its creator.

## Succession mapping (what survives — see also succession.md)

| | At succession |
|---|---|
| Floor / SOUL.md | Pass; voice-lessons dormant |
| CREATOR.md | Transplanted |
| voice-dna / Charter | Frozen forever (floor 8) / retired to history |
| Registry | Continues with SILENCED tombstones; new hats born at WATCH |
| memory/ + ledger + skills + Vigil | **The heirloom** — pass (memory minus seals) |
| Body (grants, credentials, channels) | **Does not pass** — severed; successor re-grants |
| Calibration records | Creator property, sealed-but-kept, never re-enter any Automaton |

One line: **the Mind is the heirloom, the Soul persists with one transplant and
its voice frozen, the Body is re-keyed from zero.**

## Open items

- A better answer for the Soul's substrate than "zone in the Mind repo" (the
  for-now answer, by explicit caveat).
