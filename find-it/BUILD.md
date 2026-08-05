# Building and maintaining the routing table

Read this only when [SKILL.md](SKILL.md) Step 0 sends you here. It is the rarely-run
half, kept in its own file so ordinary lookups do not pay to load it.

## When this runs

| Trigger | Mode | Detected how |
|---|---|---|
| Automaton build, Phase 1 | **build** | `automaton-creator` invokes it once `body/SENSES.md` exists |
| First lookup with no provenance stamp | **build** | SKILL.md Step 0 |
| `body/SENSES.md` sha differs from the stamp | **update** | SKILL.md Step 0 |
| A lookup routed to the wrong source | **repair** | Reflection after the failed run |

The build-at-Phase-1 trigger is the one worth defending. Waiting for the first
lookup works, but Phase 1 is a strictly better moment: `body/SENSES.md` was just
written, so the grants are fresh, and **the creator is sitting there**, already
answering questions about where their working life lives. The interview below costs
them a few minutes then and a context-switch later.

---

## The interview is not optional, and here is why

`body/SENSES.md` tells you what sources **exist**. It cannot tell you which one is
**authoritative** when two disagree, because that is a judgment about how the
creator's world actually works, not a fact derivable from a grant record.

A tracker and a chat surface both describe a piece of work. Which one do you believe
on a Thursday afternoon? For most working lives the discussion leads and the tracker
lags — but in a compliance-bound shop the tracker *is* the truth and the discussion is
hearsay, and an Automaton that guessed the common case would be confidently wrong in
the way that costs the most. So: ask.

**Ask per contested fact class, not per sense.** Two or three questions of this shape
cover most deployments:

- "When the tracker and the live discussion disagree about the state of a piece of
  work, which do you believe?"
- "When a document and the code disagree about what the system does — is the code
  always right here, or are there documents that override it?" (Usually code wins.
  Confirm rather than assume; specifications and contracts are real exceptions.)
- "Where does your own working history live — the thing you would re-read to
  reconstruct last Tuesday?"
- "Which sources are you *not* going to connect, and should I say so out loud every
  time that gap is in play?"

Record the answer as the row, and record any reasoning that surprised you in
`mind/memory/` — it is a durable fact about the creator's world, and the next rebuild
should not have to re-ask.

---

## Build mode

1. **Read `body/SENSES.md` and `body/HANDS.md` in full.** Senses are where answers
   come from; Hands matter because "can I even act on this" is often the real question
   behind a lookup.
2. **One row per fact class, not per sense.** A sense can serve several classes and a
   class can span several senses. The table is indexed by *what the creator is asking
   for*, because that is what is known at lookup time.
3. **Fill the world-facing rows** from the interview. Every row gets: authoritative
   source, echoes, and a note carrying the source's characteristic failure — lag,
   staleness, a metadata trap, a coverage hole.
4. **Fill the anchor-key classes** in SKILL.md from the creator's actual conventions:
   tracker key formats, change-proposal numbering, branch and commit patterns,
   per-surface identifiers for people, container ids already in `mind/memory/`.
5. **Write the gaps in as rows.** A mailbox that is not connected, a system the
   credential cannot reach, a record sealed World-side. A gap recorded in the table
   gets reported at lookup time; a gap held in the head gets filled with a guess.
6. **Never put a secret in the table** (floor 6). Credentials are referenced by
   location — "the token at `<path>`" — never by value, and the table is a committed
   file in a repo that may later be exported or grafted.
7. **Stamp provenance** at the bottom of the table:
   `routing-table: built <YYYY-MM-DD> against body/SENSES.md @ <sha>`,
   the sha from `git log -1 --format=%H -- body/SENSES.md`.
8. **Ledger it.** A build or update is a self-modification of the Mind: autonomous
   under the apply-scope split, and ledgered like any other.

**Acceptance check.** The build is done when no `‹unfilled›` remains, every row's note
names that source's characteristic failure, the stamp is present, and every gap the
interview surfaced appears as a row rather than as a memory.

---

## Update mode

Triggered by a sha mismatch, so the question is narrow: what changed, and which rows
does it touch?

```sh
git diff <stamped-sha>..HEAD -- body/SENSES.md
```

- **Sense added** → which fact classes does it now serve authoritatively? A new
  source frequently *demotes* an existing row to an echo, and that demotion is the
  edit most often missed.
- **Sense removed or expired** → the rows it served become gaps. Write the gap in.
  Do not leave a row pointing at a credential that expired last month.
- **Scope changed** → re-read the row's note. Scope changes rarely move the
  authoritative source but routinely invalidate the caveat.
- **Nothing relevant** → re-stamp anyway. The stamp records "checked against", and an
  unstamped table re-runs this diff on every lookup forever.

---

## Repair mode

A lookup that went to the wrong source is a reflection event, and the table lives in
the Automaton's own Mind, so the fix applies autonomously and ledgered. Edit the row
that mis-routed, and prefer fixing the **note** over fixing the source: most
mis-routes are not "wrong source" but "right source, unstated failure mode".

Born PROVISIONAL, refined by edit-on-failure, graduating after repeated success — the
ordinary skill lifecycle. Git is the rollback.

---

## The drift this cannot fix, and what can

Everything above keys on `body/SENSES.md` changing. The harder failure is the manifest
**not** changing: a grant arrives mid-task, the work continues, and registration
loses to momentum. The knowledge lands in memory and the manifest never catches up.
The sha check sees nothing wrong, because nothing about the table is wrong — the
manifest is.

This is not fixable inside a routing table, and pretending otherwise would put a
guard where it cannot fire. What fixes it is a **manifest-drift audit** at session
open: something mechanical that compares the *observable* surface of the Body against
what `body/SENSES.md` and `body/HANDS.md` claim, and reports both directions.

Detector classes that generalize (the specific paths are per-deployment):

- **Credential stores** — new files in the directories where this deployment keeps
  credentials; new entries in a CLI's auth config; scope changes on an existing token.
- **New local working copies** — repositories or export directories that appeared
  since the last audit, especially ones with push access.
- **Connector inventory** — the tools actually available in the harness this session,
  compared against the registered Sense rows. Also catches the reverse: a row whose
  connector now exposes only an `authenticate` stub has **lapsed**, and a lapsed sense
  reported as healthy is worse than one reported as down.
- **Reverse direction** — registered rows whose credential path or working copy no
  longer exists. Stale rows rot quietly and get cited confidently.

Two design notes for whoever implements it. It must be a **script, not a
remembered habit**: the whole failure mode is that recognition loses to momentum, and
prose that the Automaton is supposed to recall does not fix a recall failure. And its
output belongs in the session-open surface next to the ledger check, because an
unregistered Hand is a floor-2 clarity problem the moment it is used, not a
housekeeping item.

Adding a session-open duty edits `soul/AGENT.md`, which is **propose-first** — the
script is the Automaton's own Mind and autonomous; the duty that invokes it is the
creator's call.
