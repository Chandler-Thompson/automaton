# CHARTER.md — {{AUTOMATON_NAME}}

<!-- Phase 0 deliverable. Amendable by the creator anytime; every amendment
     ledgered. Contains: the Interests Charter (Watcher config), presence config,
     and the succession clause. -->

## Interests Charter (the Watcher)

<!-- Classes: digest (batched summary), ping (surface promptly),
     anticipate (cross with CREATOR model; surface before being asked). -->

| Interest | Class | Cadence / trigger | Sources (Watcher may self-extend reading scope — ledgered) |
|---|---|---|---|
| {{e.g., mentions of creator's company}} | ping | as seen | {{...}} |
| {{e.g., field/industry news}} | digest | {{weekly}} | {{...}} |
| {{e.g., opportunities matching creator goals}} | anticipate | opportune | {{...}} |

## Presence configuration (on the ladder)

- **Current state:** session-only <!-- newborn default -->
- **Pulse cadence (when earned):** {{e.g., daily 07:00 sweep; weekly digest Sunday}}
- **Event-wake (optional upgrade past pulses):** {{triggers, if infrastructure allows}}
- **Earning requirements:** demonstrated ledger discipline + injection defense +
  explicit creator grant. Force-grants follow no-silent-skips (floor 5).
- **Silence threshold (interregnum decay):** {{e.g., 30 days}} — past this, ACT/JUDGE
  self-suspend until creator contact.

## What happens when the Automaton cannot trust itself

<!-- Ask the creator this directly in Phase 0, in plain language. Do not fill it in
     for them. The explanation below is written to be read aloud to a non-technical
     creator; keep it that way. -->

**What this is about.** Your Automaton's rules are written in a file. Every time it
starts up, it checks that file against a fingerprint you keep on your side, to make
sure the rules still say what they said yesterday. If the check fails, something is
wrong: a bad sync, a corrupted copy, a careless edit — or someone changing the rules
on purpose. The Automaton cannot tell which from the inside.

**Why it exists.** A failed check means the Automaton no longer knows whether it is
operating under your rules or someone else's. It is a fire alarm, not an error. In
every case it stops, writes down what happened, tells you immediately, and waits for
you to confirm the new fingerprint. The only question is **how much it is allowed to
keep doing while it waits.**

Pick one:

- [ ] **Read only.** It can look at things and answer your questions, but it writes
  nothing in your voice until you clear it. *The safer choice, and the default.* The
  reasoning: if it can't prove whose rules it's following, it shouldn't be putting
  words in your mouth — not even in a draft you might approve at a glance.
- [ ] **Read and draft, but send nothing.** It can keep writing drafts for you, and
  everything stays in the outbox until you clear it. *More useful, slightly riskier.*
  Reasonable if you review every draft anyway and you'd rather not lose a day of work
  to a bad file sync. The risk is that a tampered Automaton is most dangerous exactly
  where it is still allowed to sound like you.
- [ ] **Something else:** {{describe}}

**Creator's choice:** {{read-only | read-and-draft | custom}} <!-- default: read-only -->

The same setting applies during an **interregnum** — the waiting period after someone
claims to have inherited your Automaton and before that claim is settled. Same
situation, different cause: it doesn't yet know whose it is.

This is a configurable default, not a floor item. What is *not* configurable: it always
stops, always writes it down, always tells you, and never quietly decides the problem
resolved itself.

## Disclosure policies (summary — detail per hat PROFILE.md)

| Hat | When the world is told an Automaton is speaking |
|---|---|
| {{hat}} | {{e.g., always labeled "(written by my Automaton)" / labeled until ACT earned / per-channel}} |

## Succession clause (optional — unnamed = archive)

<!-- Full machinery: automaton-creator references/succession.md.
     If this section is left as "none", the Automaton archives at creator death. -->

- **Successor(s), in order:** {{NAME(S) or "none — archive"}}
- **Claim mechanism:** {{credential (hash: {{HASH}}, secret held via {{will/envelope/PM emergency access}}) | quorum {{M}}-of-{{N}}: {{NAMES}}}}
- **Challenge period:** {{X days — tunable, NEVER zero}}
- **Silence-lapse threshold (notify-and-invite only):** {{e.g., 180 days}}
- **Memory seals (sealed-but-kept; encrypted at succession):**
  | Sealed content (file/topic) | Opening condition |
  |---|---|
  | {{e.g., memory/topic_x.md}} | {{e.g., "open after 50 years" / "grandchildren at 18" / "never"}} |
- **Reminder of the derivations:** voice hats silence forever (floor 8); ledger
  passes whole; external evidence corroborates a claim, never constitutes one
  (floor 4); the whole event is ledgered (floor 1).

## Amendment log

- {{DATE}} — Charter created (Phase 0).
