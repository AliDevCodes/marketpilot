# Development Workflow

## Lifecycle of a change

1. **Understand** the request and its acceptance criteria.
2. **Inspect** the repository state (`git status`, relevant files, docs).
3. **Plan** briefly for anything non-trivial.
4. **Implement** in a small, reviewable increment.
5. **Verify** with the commands in [TESTING.md](TESTING.md) and record real results.
6. **Update docs** in the same change when behavior, setup or structure changed.
7. **Review the diff** for accidental files, secrets, debug code and unrelated edits.
8. **Hand off** for manual testing, with exact steps and expected results.
9. **Wait for explicit approval.**
10. **Finalize** (commit, then push) only after approval.

## Approval gate

Commit and push require an explicit approval that names the tested version, for example `APPROVED — commit and push`. Anything else is not approval.

## Git conventions

- Branch: `main` for the initial history. Feature work may use short-lived branches if agreed.
- Commit messages: Conventional Commits, one logical change per commit.
  - `chore: initialize backend skeleton`
  - `feat(marketdata): add Nobitex candle adapter`
  - `test(ledger): cover partial exit fees`
- Before each commit: `git status` and `git diff --staged` must show only intended files.
- Never commit `.env`, virtual environments, caches, exports or local data.
- No force-push and no history rewrite unless separately authorized.

## Handoff format

- **Outcome:** what changed and why.
- **Files:** important files and their purpose.
- **Verification:** commands actually run and their results.
- **Manual steps:** what the user should do and what they should see.
- **Remaining issues:** limitations and anything not yet verified.
- **Approval status:** awaiting the user's test and explicit approval.
