# Procedures — the four steps that were one clause each

Doctrine elsewhere in this skill says *that* these happen. This file says *how*.
Each was previously a single sentence, which is enough to agree with and not enough
to execute — and the one that turns Markdown into a running Automaton was among them.

Every procedure here is deliberately tool-agnostic. Named commands are examples of a
shape, never requirements, and nothing in an Automaton may depend on a product one
company owns. Open primitives are fine; a vendor's SDK is not.

---

## 1. Sealing — encrypt at write, or do not call it sealed

**The rule that makes this urgent:** git never forgets. Encrypting a file that has
already been committed in plaintext seals nothing — the plaintext sits in history
forever, recoverable by anyone who ever clones the repo, including a successor the
creator specifically sealed it against. **Sealing later is already too late.**

So *seal* and *delete* are different operations and always will be. Sealing is
cheap and happens at write. Deletion is a history rewrite: warned, ledgered, and
creator-only.

### Deciding what to seal

The creator marks a memory topic or file **seal at succession** in the Charter, with
its opening condition (`"open after 50 years"`, `"to grandchildren at 18"`, `"never"`).
The Automaton may *propose* candidates. It never seals unbidden — a seal the creator
did not ask for is content quietly removed from their reach.

### The procedure

1. **Before the first write**, confirm the file is marked. If content that should be
   sealed has already landed in plaintext, stop and tell the creator plainly: this
   file cannot be retroactively sealed, only rewritten out of history. Do not encrypt
   it and imply the problem is solved (floor 7).
2. **Generate the key in the World**, not in the repo. One key per seal, or one per
   opening condition — never one key for everything, because a single key means a
   single disclosure opens every capsule at once.
3. **Encrypt at write time.** Any symmetric or public-key tool the creator can still
   run in twenty years: `age`, `gpg`, `openssl enc`. Prefer the boring one. Public-key
   sealing has a real advantage here — the Automaton can seal new content without ever
   holding the key that opens it.
4. **Commit the ciphertext** to `mind/seals/`, named so the *existence* and *opening
   condition* are legible without the key. A successor must be able to see that a
   capsule exists and when it opens. Sealed-but-kept, never destroyed.
5. **Record in the World Inventory:** which key opens which seal, where the key is
   held, and the opening condition. A seal whose key is lost is a deletion the creator
   did not choose.
6. **Ledger it** as an AMENDMENT, naming the file and the condition — never the key
   and never its location beyond a pointer (floor 6).

### Verifying

Seal one throwaway file end to end during Phase 1, open it, and confirm the plaintext
never entered history: `git log -p -- mind/seals/` should show ciphertext only. An
unverified seal is a promise about the creator's most private material.

---

## 2. Deploy — the step that makes it real

`body/` is a **blueprint**. Deploying is how the blueprint becomes an Automaton that
runs. Re-embodiment repeats this whole procedure on new hardware, a new harness, or a
new model; nothing here should surprise the person doing it the second time.

1. **Clone the repo** to the host that will run it.
2. **Install the Soul where the harness reads it.** Most harnesses expect a contract
   file at a fixed path. If yours does, the deployed copy is an **alias of
   `soul/AGENT.md`, never a second source of truth.** Prefer a symlink so the two
   cannot drift; if the harness cannot follow symlinks, copy it and record in
   `body/ANATOMY.md` that a copy exists and must be re-copied on every Soul change.
   Two contracts that disagree is the worst failure mode available here.
3. **Map every flattened path.** Harnesses often flatten the zone structure. Record
   the mapping in `body/ANATOMY.md` — deployment alias on the left, the real
   zone-prefixed path on the right. **The zone path governs**; the alias is a local
   convenience.
4. **Wire the Senses.** Each read-connection in `body/SENSES.md` gets connected and
   *demonstrated* — read something real through it. Credentials go where the manifest
   says they live, never into the repo (floor 6). Both command channels are wired and
   each carries a test message; a channel that has never carried a message is a plan.
5. **Wire the Hands.** Each act-connection in `body/HANDS.md`, with its rung
   requirement enforced by the harness where the harness can enforce it. At a newborn
   Automaton every Hand is dormant, so confirm they are *present and refused*, not
   absent.
6. **Rebuild Reflexes** — the session-open floor check, the heartbeat, the quench
   behavior at the Charter's setting, any indexes or caches. Reflexes are Body: they
   are rebuilt from the Mind at every embodiment, and none of them is ever
   authoritative.
7. **Set the creator-controlled remote** and push. The remote is a World item; the
   Automaton pushes to it and does not own it.
8. **Run the Phase 1 acceptance check** (in `SKILL.md`). Deployment is not done
   because the files are in place; it is done when the checks pass.

---

## 3. The extractor — written for one corpus, thrown away after

**Never a generic tool.** A general-purpose voice extractor produces general-purpose
results, and the whole point of voice-dna is that it is not general. Write one for
*this* creator's export format, run it, keep its output, and expect to write another
for the next corpus.

1. **Inventory the export** before parsing anything: format, encoding, date range,
   message count, which fields identify the sender. Get the sender-identification
   right first — everything downstream depends on it.
2. **Profile only the creator's own messages.** Others' messages are read for
   *context* and never profiled, never imitated, never quoted into voice-dna (floor 8:
   you do not voice other people, and that starts at what you measure).
3. **Confirm held-outs are already sealed** (Phase 2 step 2 — by metadata only, before
   anyone read content). If sealing was skipped, the corpus is burned for calibration
   and only newly-arrived data can be sealed. Say so rather than proceeding quietly.
4. **Count, do not characterize.** Every claim the extractor emits carries its number.
   "Prefers short messages" is not output; "median 14 words, n=4,102" is.
5. **Split by medium, era, and register** — the same person is different over email
   than over chat, and different in 2019 than now. Name which era is being imitated
   and get the creator to confirm it.
6. **Emit negative markers.** What the creator *never* does catches impostors better
   than what they always do, and it is the half a naive extractor skips.
7. **Emit judgment patterns, not only mechanics** — what gets escalated, what gets
   absorbed, how they say no. This is the axis calibration weighs more heavily.
8. **Write into `soul/representations/<hat>/voice-dna/<register>.md`** from
   `assets/VOICE-DNA.template.md`, one file per register.
9. **Keep the raw export outside the Automaton** (e.g. `~/.automaton-ingest/<hat>/`).
   The repo gets the distillate. Record where the raw lives in the World Inventory,
   and never commit it.
10. **Keep the extractor itself** next to the raw material, not in the repo. It is
    scaffolding, and its provenance matters more than its reusability: note which
    export it was written against and when.

---

## 4. The World-side integrity check — the examiner, not the student

The Automaton's session-open floor check is a **reflex**: it catches accidents — bad
syncs, corruption, a careless edit. It cannot catch a compromised instance, because a
compromised instance runs the check on itself. The authoritative check lives in the
**World**, on the creator's side, where the Automaton cannot reach it.

### What it does

1. Fetch the current `soul/AGENT.md` from the creator-controlled remote.
2. Extract the floor block — Layer 2, the eight items.
3. Hash it and compare against the value anchored in the World Inventory.
4. **Match** → nothing to do. **Mismatch** → this is a creator-facing alarm, not an
   automated remediation. Someone looks at the diff, decides whether the change was
   legitimate, and either re-anchors deliberately or treats it as an integrity
   incident.
5. Never let the check write to the repo. An examiner that can edit the exam is not an
   examiner.

### Where it runs

Anywhere the Automaton cannot influence: the creator's own machine, or a scheduled job
on infrastructure the Automaton has no Hand on. If the Automaton can trigger, silence,
or edit this check, it has stopped being a World item and become a Body one — which is
exactly the failure the split exists to prevent.

### Open dependency — read before writing the script

**The canonical hash recipe is not yet specified.** Four hashes are demanded across
this skill and none states its algorithm, its extent, or its canonicalization rules,
so two creators following these documents today produce different hashes for the same
build. That specification is queued.

Until it lands, a creator writing this script must **record their own recipe in the
World Inventory** beside the anchored value: which tool, which byte range, whether a
trailing newline is included. A hash whose recipe is not written down cannot be
reproduced later, which makes it an anchor to nothing — and this is precisely the
failure the exemplar hit on its first attempt to verify its own floor.

---

## 5. Re-anchoring — a moved hash is a task, never a fact in passing

Legitimate changes move the floor hash: an amendment the creator ratified, or an
upstream change they accepted. When that happens, the Automaton does not note it and
move on.

It presents an explicit **re-anchor request**: what changed, why, the new commit hash,
the new file hash, the date, and the steps the creator takes to update the World
Inventory. It re-surfaces that request at every session open until the creator
confirms — because until they do, the World-side check is comparing against a stale
anchor, which is the exact condition the check exists to catch.

---

## 6. The journal fold — one ledger, many sessions

The ledger template defines the write model (assets/LEDGER.template.md, "Concurrent
sessions"); this section covers what the template leaves deployment-specific. The
model is adopted from the stoa project (github.com/Chandler-Thompson/stoa,
docs/PROTOCOL.md), which named it so it could be cited apart from the tool.

### The lock

The fold is the only writer of the monthly file, and it holds a lock for the whole
stage-commit sequence. What the lock IS depends on where sessions live:

- **One machine, one repo** (the common case): a lockfile — created with the shell's
  `noclobber` guarantee (`set -o noclobber; echo "$$ $(date -Iseconds) <purpose>" >
  mind/state/locks/repo.lock`), never `mkdir`, which false-positives on any existing
  file. Write the pid and timestamp INTO the lock: a leaked lock from a crashed
  session looks identical to live contention, and the pid is how the next session
  tells them apart (dead pid → remove, note it in the fold commit; live pid → defer
  the fold).
- **Distributed members**: stoa's branch-as-lock — claiming the consolidator role
  pushes a fresh root commit to a lock branch; an existing branch rejects the push.
  Use stoa itself at that point rather than reimplementing it.

### Failure cases the recipe must survive

- **Fold interrupted between append and delete:** the next fold de-duplicates by
  entry header (timestamp + title) before re-appending — entries are idempotent by
  their headers.
- **Lock holder died:** dead-pid check above. A lock is never simply deleted on age
  alone; age plus a dead pid, or age plus no matching activity in `git log`, is the
  bar.
- **Journal directory missing:** nothing is pending; sessions recreate it on first
  entry.

### What this procedure deliberately does not change

Surfacing. Unsurfaced entries are surfaced from journals at session open BEFORE any
fold is attempted, and a deferred fold defers only the housekeeping — never the
creator's visibility (floor 1).
