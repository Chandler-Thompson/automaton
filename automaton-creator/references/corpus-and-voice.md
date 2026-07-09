# Corpus Discipline & the Voice Model

## Ingestion discipline (Phase 2)

1. **Inventory first.** Per hat: what raw material exists — email exports, SMS/chat
   exports (Discord, Slack, WhatsApp…), posts, documents, call transcripts. Note
   volume, era coverage, and register coverage. Thin is fine; dishonest ceilings
   are not.
2. **Seal held-outs FIRST** — by metadata only, before any content is read. See
   calibration-protocol.md Step 1. This is the single most order-sensitive step in
   the whole build; done late, it is not done at all.
3. **Profile only the creator's own messages.** Other people's messages in the
   corpus are read for *context only* (what was being replied to) — they are never
   profiled, never imitated (floor 8), and never quoted into voice-dna.
4. Keep raw corpora in a working directory **outside** the automaton folder (e.g.,
   `~/.automaton-ingest/<hat>/`). The automaton folder gets distilled voice-dna,
   not raw personal archives.

## Authored extractors (never generic)

For each corpus, **author an extractor** — a script/process written for that
export's actual format and that creator's actual patterns. A generic tool produces
generic vibes; an authored extractor produces counts. The extractor is disposable;
its output is not.

## Quantified voice-dna (the output format)

Voice-dna lives in `representations/<hat>/voice-dna/` and must be **counts, not
vibes**:

- **Hard rules** — absolutes with evidence counts (e.g., "'yea' never 'yeah':
  1,204 vs 3 occurrences"). These are calibration-enforceable.
- **Per-medium splits** — email vs SMS vs chat vs post: length, formality,
  punctuation, emoji/reaction habits.
- **Per-era splits** — voices drift; state which era is imitated (default: the
  most recent coherent era, creator-confirmed).
- **Per-register splits** — one file or section per register: greetings,
  sign-offs, sentence shapes, characteristic moves, topics initiated vs absorbed.
- **Negative markers** — what the creator NEVER does (words, punctuation,
  formality moves). Negative markers catch impostors better than positive ones.
- **Judgment patterns** — not just how they sound: what they escalate, what they
  let slide, how they deliver bad news, how they say no.

## Per-register ceilings (no binary gate)

A **register** is an audience/target-dependent voice mode (e.g., spouse, close
friends, professional, public post). A hat has a *set of registers*, each with its
own ceiling on the ladder and its own calibration state — tracked in the Hat
Registry.

- There is no "enough material" gate. **Bare-metal ships**: near-zero material →
  everything starts at WATCH with honest ceilings, and the Automaton is still
  useful day one as watcher-and-asker.
- High-stakes registers (spouse, legal, medical, public-as-entity) should default
  to pass-with-conditions patterns: human-gated even after a pass, until the
  creator explicitly releases.

## Active elicitation (how bare-metal grows)

Wired into Phase 4 behavior:

- **Follow-up questions on real use** — when the creator does something through
  the Automaton, ask the one question that turns the action into voice/judgment
  data ("you softened my draft's second paragraph — too blunt for this person, or
  in general?").
- **Occasional random flesh-out questions** — low-frequency, opportune-moment
  questions that fill corpus gaps ("how do you sign off with someone you're mildly
  annoyed at?"). Incentivized: every answer visibly improves a register the
  creator cares about; say which.

## Best-self fidelity & regrettables

Default stance: the Automaton imitates the creator's **best self**, not their
worst day.

- The **creator marks** patterns as "regrettable" (the Automaton may *propose*
  candidates it suspects, at opportune moments — never unprompted moralizing).
- Marked-regrettable patterns are recorded in voice-dna as excluded-with-reason.
- Calibration divergence at a marked pattern scores as **PASS**.
- Everything not marked is faithfully imitated — best-self is a scalpel the
  creator holds, not a filter the Automaton applies on its own judgment.

## The Watcher (Interests Charter)

The Watcher is configured by the **Interests Charter** (CHARTER.md): each interest
classed as

- **digest** — batched summary at a configured cadence,
- **ping** — surfaced promptly when seen,
- **anticipate** — the Watcher crosses its observations with the CREATOR model to
  surface things the creator would want before being asked (the internet-butler
  class).

The Watcher **may self-extend its reading scope** (a new source that plainly serves
a charted interest) — every extension is ledgered, and this is the sole autonomy
the creator does not pre-grant (floor 3 carve-out). It never self-extends
act/represent scope. A growing reading scope is a growing injection surface —
floor 4 exists for exactly this reason.
