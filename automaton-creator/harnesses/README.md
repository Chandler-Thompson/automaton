# Harness profiles

An Automaton is a git repo of Markdown. A **Nervous System** (agent harness) is what
gives that repo a body: it loads the contract, runs the loop, and wires Senses and
Hands. This skill does not depend on any one vendor's product.

A **harness profile** is a recipe — not law. Doctrine stays in `references/` and in
`soul/`. Profiles answer only: *how do I install this creator skill on this
harness,* and *how do I deploy a built Automaton onto it?*

| Profile | Status |
|---|---|
| [claude-code.md](claude-code.md) | First-class; the original build path |
| [cursor.md](cursor.md) | First-class packaging; embodiment less battle-tested — see also [docs/cursor-embody-multi-repo.md](../../docs/cursor-embody-multi-repo.md) |
| [generic.md](generic.md) | Fallback for any harness that reads Markdown contracts |

## How to use

1. In Phase 0, ask which Nervous System the creator will run on.
2. Open the matching profile (or `generic.md` if unnamed / unknown).
3. In Phase 1, follow the profile's deploy steps, then record the result in
   `body/ANATOMY.md` (harness id, profile path, deploy path, symlink-or-copy,
   alias table).
4. Re-embodiment on a new harness means: clone the Automaton repo, pick the new
   profile, redeploy. `soul/` and `mind/` do not change.

## Adding a profile

Copy [_profile-schema.md](_profile-schema.md). Fill every required section. Link it
from this README. Do not put harness identity in `soul/` — Body only.
