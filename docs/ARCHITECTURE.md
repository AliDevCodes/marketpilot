# Architecture

Status: **planned**, except where marked *implemented*.

## Shape

A modular monolith: one deployable Python backend plus, later, one React frontend. No microservices, message brokers or background-job infrastructure in V1.

## Intended modules (under `backend/app/`)

| Module | Responsibility | Status |
|---|---|---|
| `config.py` | Environment-based settings | implemented |
| `db.py` | Engine, sessions, connectivity probe | implemented |
| `main.py` | FastAPI app factory and routes | implemented (health only) |
| `marketdata/` | Provider adapters and normalized candles | planned |
| `strategy/` | Pure, deterministic signal rules | planned |
| `risk/` | Position sizing and risk limits | planned |
| `ledger/` | Paper accounts, orders, fills, positions, P&L | planned |
| `journal/` | Trade notes and reviews | planned |
| `exports/` | Excel, CSV, JSON, Markdown output | planned |

## Dependency direction

- `strategy` and `risk` are pure logic: they must not import FastAPI, SQLAlchemy or provider code.
- Provider-specific response shapes stay inside `marketdata/` adapters and are converted to internal models.
- `ledger` owns all cash and position state. Routes call services; services call domain logic.
- The frontend never computes authoritative balances, fills or P&L.
- AI helpers, when added, sit at the edge and consume exported facts; they never write ledger state.

## Persistence

PostgreSQL, accessed through SQLAlchemy 2.0, with schema changes managed by Alembic. Money columns use `NUMERIC`, and Python code uses `Decimal`.
