# AI Agent Instructions — MarketPilot

Read this file first. It is the operational entry point for any AI agent working in this repository.

## Mandatory preflight before any file change

1. `git rev-parse --show-toplevel` — confirm you are in the MarketPilot repository.
2. `git remote get-url origin` — expected: `https://github.com/AliDevCodes/marketpilot`.
3. `git branch --show-current` — expected: `main` unless a task branch was agreed.
4. `git status --short` — record pre-existing changes. Never overwrite or discard them.

If the repository identity does not match, stop.

## Read before implementing

- `docs/PROJECT_STATE.md` — what currently exists and what is verified.
- `docs/ARCHITECTURE.md` — module boundaries and dependency direction.
- `docs/DEVELOPMENT_WORKFLOW.md` — task lifecycle and approval gate.
- `docs/TESTING.md` — the commands that are actually verified.

## Non-negotiable rules

- V1 is paper trading only. Never create real-money or broker execution paths.
- Deterministic backend logic owns all financial calculations, position sizing, fees, ledger state and risk limits. AI may explain or analyze; it must never change financial state or invent prices, fills or performance numbers.
- Strategy rules live in the strategy module only, never in routes, UI components or prompts.
- Money uses `Decimal` (or PostgreSQL `NUMERIC`), never binary `float`.
- Secrets live in a local `.env` (git-ignored) or environment variables. Never commit credentials.
- Do not add dependencies, services or architectural layers without a stated justification.
- Do not claim a test passed unless it ran and its result was observed.

## Git and approval gate

- No `commit` and no `push` before the user explicitly approves the tested version, using a clear approval such as `APPROVED — commit and push`.
- Silence, a successful build, or passing tests are not approval.
- After approval: re-check `git status` and the staged diff, make sure only intended files are included, then commit with a focused message in Conventional Commits style (`feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`).
- Never force-push, rewrite history, or run destructive cleanup without separate explicit authorization.

## Documentation duty

Update the affected file in `docs/` in the same working change whenever behavior, setup, architecture, contracts or testing commands change. Never describe planned work as implemented.
