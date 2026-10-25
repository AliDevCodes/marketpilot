# Project State

Last updated: initial skeleton, not yet committed.

## Implemented (in working tree)

- Backend skeleton: FastAPI app factory (`backend/app/main.py`).
- Settings loaded from environment / `.env` (`backend/app/config.py`).
- SQLAlchemy engine, session factory and database probe (`backend/app/db.py`).
- `GET /health` endpoint reporting database reachability.
- Repository hygiene: `.gitignore`, `.env.example`.

## Verified

- Python syntax of the files above (`py_compile`).
- `pytest`: 2 of 2 passed on Windows, Python 3.14.7.
- `ruff check .`: all checks passed.
- `GET /health` returned `status: ok`, `database: up` against local PostgreSQL.

## Not yet verified

- Database schema and migrations: not created yet (no tables).
- Commit and push: not done. Waiting for explicit user approval.

## Planned (not implemented)

- Database schema and Alembic migrations.
- Market-data adapters: Nobitex first, CSV import as fallback. TSETMC and Codal only after their terms and endpoints are verified.
- Deterministic trend + momentum + pullback strategy with explicit rules.
- Position sizing, fee and slippage model, paper-trading ledger.
- Trading journal, backtesting, exports (Excel, CSV, JSON, Markdown).
- Frontend (React, TypeScript, Vite) in Persian RTL.

## Known unknowns

- Exact Nobitex endpoints, rate limits and terms of use: not yet verified.
- Whether historical data depth is sufficient for backtesting: unknown until a source is selected.
