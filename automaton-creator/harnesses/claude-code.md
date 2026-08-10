# Harness profile: Claude Code

- **Harness id:** `claude-code`
- **Display name:** Claude Code
- **Provenance:** Proven — the original packaging and first live builds used this path.

## Creator skill install

**Unix / macOS**

```bash
git clone https://github.com/Chandler-Thompson/automaton.git ~/github/automaton
mkdir -p ~/.claude/skills
ln -s ~/github/automaton/automaton-creator ~/.claude/skills/automaton-creator
```

**Windows (PowerShell junction)**

```powershell
git clone https://github.com/Chandler-Thompson/automaton.git $env:USERPROFILE\github\automaton
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\automaton-creator" `
  -Target "$env:USERPROFILE\github\automaton\automaton-creator"
```

- **Project-scoped path:** N/A for the creator skill (install once per machine).
- **Invocation:** In Claude Code, say **"build my automaton"** (or any entry phrase in `SKILL.md`).
- **Do not use:** paths outside `~/.claude/skills/` for this skill unless Claude Code docs change.

## Built Automaton deploy

1. Clone the Automaton repo to the host that will run it.
2. Install `soul/AGENT.md` where Claude Code reads the agent contract — prefer a
   **symlink** to `soul/AGENT.md`; if symlinks are unavailable, copy and record
   copy-on-Soul-change in `body/ANATOMY.md`.
3. Record every flattened / renamed path in the ANATOMY alias table. Zone paths
   govern; aliases are local conveniences. (Historical pitfall: a `TOOLS.md`
   alias that no template produces — acceptance checks must open every path the
   contract names.)
4. Wire Senses and Hands from `body/SENSES.md` / `body/HANDS.md`; demonstrate
   both command channels.
5. Rebuild Reflexes (session-open floor check, heartbeat, quench behavior).
6. Crossing: deploy home/graft halves as a **skill** or **`.claude/commands`**
   entry — one graft, one command name.

## Limits and honesty

Claude Code can often express tool permissions, but HANDS rung enforcement is
still checked at use time against the Hat Registry. Floor, ledger, and creator
ratification remain authoritative regardless of harness features.
