# Claude Code mods

Three mods for running several agents at once.

| Mod | What it does | Commands |
|---|---|---|
| `session-relay` | Pass work between sessions. `/handoff builder` makes this session write a brief (goal, decisions, done, next steps, open questions) and sends it to the session named `builder`. Messages that come in are kept in an inbox and announced with a toast. | `/handoff <session> [note]` |
| `model-router` | Easy prompts (short lookups, renames, formatting) run their turn on a cheaper model; anything with reasoning words, code or length stays on the session's model. Explore and guide subagents run on the cheap model too. | `/route`, `/route auto\|off\|cheap` |
| `agent-dashboard` | A pane showing your agents and their status, context use, cost and rate limits, messages from other sessions, and the latest from your vault (any MCP tool, default `JW AI Vault` / `room_read`). | `/dash` |

## Install

At the prompt of a terminal Claude Code session:

```
/plugin install session-relay --marketplace jaywesterlow/jaywesterlow
/plugin install model-router --marketplace jaywesterlow/jaywesterlow
/plugin install agent-dashboard --marketplace jaywesterlow/jaywesterlow
```

Answer `y` to add the marketplace, then pick a scope. (The marketplace is read from the default branch, so this works once these files are on `main`.) Before that, run one from the folder: `claude --plugin-dir mods/model-router`.

Settings: `/config` lists `model-router.cheapModel` (default `haiku`) and `agent-dashboard.vaultServer` / `vaultTool`.

## Plan in one session, build in another

1. Start two sessions in the same repo, name them `planner` and `builder` (`/rename`).
2. Plan in `planner`. When the plan is done: `/handoff builder start with step 1`.
3. `builder` receives the brief as a message and starts. It can answer with the built-in SendMessage tool ("tell planner when the tests pass").
4. `/dash` in either session shows the agents and the messages going back and forth.

## Develop

```
claude plugin validate mods/<mod>
claude plugin test mods/<mod>
```
