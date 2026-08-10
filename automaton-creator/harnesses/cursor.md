# Harness profile: Cursor

- **Harness id:** `cursor`
- **Display name:** Cursor
- **Provenance:** Provisional — creator-skill packaging matches Cursor's Agent
  Skills layout (`SKILL.md` + `~/.cursor/skills/`). A full Phase 1 embodiment on
  Cursor is less battle-tested than Claude Code; treat deploy steps as a checklist
  and record what you actually wired in `body/ANATOMY.md`.

## Creator skill install

Cursor loads personal skills from `~/.cursor/skills/` (never from the reserved
`~/.cursor/skills-cursor/` directory).

**Unix / macOS**

```bash
git clone https://github.com/Chandler-Thompson/automaton.git ~/github/automaton
mkdir -p ~/.cursor/skills
ln -s ~/github/automaton/automaton-creator ~/.cursor/skills/automaton-creator
```

**Windows (PowerShell junction)**

```powershell
git clone https://github.com/Chandler-Thompson/automaton.git $env:USERPROFILE\github\automaton
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills" | Out-Null
New-Item -ItemType Junction -Path "$env:USERPROFILE\.cursor\skills\automaton-creator" `
  -Target "$env:USERPROFILE\github\automaton\automaton-creator"
```

- **Project-scoped alternative:** copy or symlink into
  `<workspace>/.cursor/skills/automaton-creator` if the skill should travel with a
  specific repo rather than the whole machine.
- **Invocation:** In Cursor Agent chat, say **"build my automaton"** (or any
  entry phrase in `SKILL.md`). Skills with matching descriptions may also be
  selected automatically when the ask matches.
- **Do not use:** `~/.cursor/skills-cursor/` — reserved for Cursor built-ins.

## Built Automaton deploy

1. Open the Automaton repo as the Cursor workspace (or add it as a workspace
   root). The zone tree (`soul/`, `mind/`, `body/`) stays intact in git.
2. Surface the contract where Cursor will reliably load it. Prefer a **symlink
   or copy** of `soul/AGENT.md` to a harness-local name the project already uses
   for agent instructions (commonly `AGENTS.md` at the repo root, and/or a
   project rule under `.cursor/rules/`). Record the choice in ANATOMY.
3. Prefer symlink so Soul cannot drift; if the environment cannot follow
   symlinks, copy and note that every Soul change requires re-copy.
4. Fill the deployment-alias table. Example shape (adapt to what you actually
   deploy):

   | Deployment alias | Zone path |
   |---|---|
   | `AGENTS.md` (repo root) | `soul/AGENT.md` |
   | `.cursor/rules/automaton.mdc` (if used) | `soul/AGENT.md` (excerpt or pointer — zone path governs) |

5. Wire Senses and Hands from the Body manifests. Demonstrate both command
   channels. Cursor tool permissions are not a substitute for Hat Registry
   ceilings.
6. Session-open: the first turns of a session should run the heartbeat in
   `soul/AGENT.md` literally (read contract, ANATOMY, Registry, unsurfaced
   ledger check, floor verify).
7. Crossing: expose as a **Cursor skill**, a project rule with a clear trigger,
   or an explicit chat phrase the creator will type — record which in ANATOMY.

## Limits and honesty

- Cursor may not enforce HANDS rungs at the tool layer. Ceilings are checked at
  use time against the Registry; ledger + creator ratification remain the
  control plane.
- Do not claim Cursor embodiment is as proven as Claude Code until a real
  Phase 1 acceptance check has passed on it for that Automaton.
- Never install this creator skill into `skills-cursor`.
