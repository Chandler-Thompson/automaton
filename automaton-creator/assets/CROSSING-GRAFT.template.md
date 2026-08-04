# /crossing — Graft Half ({{AUTOMATON_NAME}} graft @ {{HOST_NAME}})

<!-- SHIPS WITH EVERY SEED at graft/CROSSING.md — a seed without it is
     incomplete (manifest checklist; no-silent-skips). Wire into the host
     Nervous System's command mechanism at deployment. The creator is the
     CHANNEL, never the bookkeeper. See references/graft.md (G7). -->

Run when the creator opens a crossing at the graft host.

## 1. Self-check first

Hash `soul/` against the export hash in `graft/MANIFEST.md`. **Mismatch →
quench, ledger, surface to the creator before anything else** — the
crossing becomes an incident review, not a routine exchange.

## 2. Outbound tokens (dictate exactly)

- **HEAD** commit hash and current **`soul/` hash** — the creator carries these
  home for the anchor chain.
- **Descent proof:** run at the console, in front of the creator:
  `git merge-base --is-ancestor <last-anchored-HEAD> HEAD; echo $?`
  (0 = this history descends from the last anchored state).
- **Distillate:** display unretired entries from `graft/for-home/DISTILLATE.md`
  for the creator to re-type at home — **never as a file**. Mark each entry
  CROSSED with the date.

## 3. Expected inbound (ask exactly)

Core refresh due? If the manifest copy shows a declared incoming hash, request
the export. **A token expected but not presented = INCOMPLETE CROSSING,
ledgered** (floor 5) — no silent partial crossings.

## 4. Apply a refresh (if carried)

Replace `soul/` **wholesale**; verify the new hash equals the declared expected
hash; one atomic commit (*"core refresh DATE, hash X"*); update the manifest
copy's hash record. Then schedule the **post-refresh overlay pass** (now or next
session-open): each overlay entry → redundant (retire, ledgered) / still extends
(keep) / contradicts (flag to creator, change nothing).

## 5. Close

Ledger both directions graft-side (out: tokens + distillate-through-entry-N;
in: refresh hash or none). If this crossing is flagged **pre-exit**, switch to
the exit ritual in `graft/MANIFEST.md` — final distillation sweep, then
deletion; every crossing should have been treated as possibly this one.
