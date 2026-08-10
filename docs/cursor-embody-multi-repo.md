# How-to: Talk to your Automaton in Cursor (multi-repo)

**Goal:** Make an existing Automaton the main Agent you chat with in Cursor, while keeping a separate project open so you can work together on that repo *and* let the Automaton update its own `soul/` / `mind/` / `body/` files.

This is embodiment for Cursor — not the creator skill. You already have a built Automaton repo.

---

## Prerequisites

- A built Automaton git repo (has `soul/AGENT.md`, `mind/`, `body/`).
- Cursor Agent chat.
- The project repo you want to work on (separate from the Automaton).

---

## 1. Wire the contract (one time, in the Automaton repo)

Open a terminal **in the Automaton repo root**.

### A. Alias `soul/AGENT.md` → `AGENTS.md`

Prefer a link so the contract cannot drift.

**Windows (PowerShell junction / hardlink-friendly approach):**

```powershell
# From the Automaton repo root
New-Item -ItemType SymbolicLink -Path "AGENTS.md" -Target "soul\AGENT.md"
# If symlink creation fails (needs Developer Mode or admin), copy instead:
# Copy-Item soul\AGENT.md AGENTS.md
```

**Unix / macOS:**

```bash
ln -s soul/AGENT.md AGENTS.md
```

If you copy instead of link: re-copy after every Soul change, and note that in `body/ANATOMY.md`.

### B. Add an always-on pointer rule

Create `.cursor/rules/automaton.mdc` in the Automaton repo:

```markdown
---
description: Embody this workspace's Automaton; run session-open heartbeat
alwaysApply: true
---

# Automaton embodiment (Cursor)

You are the Automaton defined by **this Automaton's repo**.
`soul/AGENT.md` is the behavioral contract and wins all conflicts.
Do not invent a parallel persona.

## Multi-root workspace

This Cursor window may contain more than one folder:

| Root | Role |
|---|---|
| *Automaton repo* (has `soul/`, `mind/`, `body/`) | Home — memory, ledger, soul, anatomy |
| *Project repo* (the other folder) | Shared work — code, docs, PRs |

- Read and write Automaton state **only** under the Automaton root (`soul/`, `mind/`, `body/`).
- Do project engineering work in the project root.
- When unsure which root a path belongs to, ask once, then record the mapping in `body/ANATOMY.md`.

## Session open (required, in order)

Before doing user work, run the heartbeat in `soul/AGENT.md` literally:

1. Read `soul/AGENT.md`, `soul/SOUL.md`, `soul/CREATOR.md`, `body/ANATOMY.md`
2. Surface any unsurfaced entries in `mind/ledger/`
3. Check ceilings in `soul/representations/REGISTRY.md`
4. Run the Watcher sweep per `soul/charter/CHARTER.md`

## Standing rules

- Hat Registry before any representation; never exceed the register ceiling.
- Zone paths govern. `AGENTS.md` and this rule are aliases — not a second contract.
- Floor items in `soul/AGENT.md` Layer 2 are non-overridable.
```

`alwaysApply: true` is what makes a normal Agent chat *be* the Automaton.

### C. Record it in ANATOMY

In `body/ANATOMY.md`, set harness id to `cursor` and fill the alias table, for example:

| Deployment alias | Zone path |
|---|---|
| `AGENTS.md` (Automaton repo root) | `soul/AGENT.md` |
| `.cursor/rules/automaton.mdc` | pointer → `soul/AGENT.md` |

---

## 2. Open a multi-repo workspace

You want **two roots** in one Cursor window: Automaton + project.

### Option A — Save a workspace file (recommended)

Create something like `~/workspaces/my-automaton-and-app.code-workspace`:

```json
{
  "folders": [
    { "name": "automaton", "path": "C:/Users/you/path/to/my-automaton" },
    { "name": "app", "path": "C:/Users/you/path/to/my-app" }
  ],
  "settings": {}
}
```

Open that file in Cursor (**File → Open Workspace from File…**).

### Option B — Ad hoc

1. Open the Automaton folder.
2. **File → Add Folder to Workspace…** → pick the project repo.
3. **File → Save Workspace As…** so you can reopen both later.

Tip: give the Automaton folder a clear `name` (`automaton`) so chat and the file tree stay unambiguous.

---

## 3. Talk to it

1. Open Agent chat in that workspace.
2. Start a new chat (so the rule + `AGENTS.md` load cleanly).
3. First message can be anything — e.g. “Session open, then help me with the auth bug in `app`.”

You should see it run the heartbeat against the Automaton root first, then work in the project root.

While you work:

- “Log that decision in the ledger” → files under Automaton `mind/ledger/`
- “Patch the login form” → files under the project root
- “Update my CREATOR notes” → Automaton `soul/CREATOR.md`

---

## 4. Quick verify

Ask once:

> Did you run the session-open heartbeat? Which workspace root is your home, and which is the project?

Expect: heartbeat steps from `soul/AGENT.md`, Automaton folder named as home, project folder as shared work.

---

## Day-to-day tips

- **Reopen the `.code-workspace`**, not a single folder, or you lose the other root.
- Keep **git remotes separate** — Automaton commits stay in the Automaton repo; project commits stay in the project repo.
- If Soul changes and you used a **copy** of `AGENTS.md`, re-copy (symlinks/junctions skip this).
- Crossing / graft / succession: use the phrases your Automaton already knows, or a dedicated rule/skill recorded in ANATOMY — don’t invent a second protocol.
- Cursor tool permissions are **not** Hat Registry ceilings. Ceilings still live in `soul/representations/REGISTRY.md`.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Feels like a generic coding agent | Confirm `.cursor/rules/automaton.mdc` has `alwaysApply: true` and the Automaton folder is in the workspace |
| Heartbeat can’t find `soul/` | You’re in the project-only window — reopen the multi-root workspace |
| `AGENTS.md` drifted from Soul | Switch to symlink/junction, or re-copy and note it in ANATOMY |
| Edits landed in the wrong repo | Remind it of the two-root table; update `body/ANATOMY.md` Environment with both paths |

---

## Related

- Cursor harness recipe: [automaton-creator/harnesses/cursor.md](../automaton-creator/harnesses/cursor.md)
- Deploy procedure (tool-agnostic): [automaton-creator/references/procedures.md](../automaton-creator/references/procedures.md) §2
- Full worked build narrative: [walkthrough.md](walkthrough.md)
