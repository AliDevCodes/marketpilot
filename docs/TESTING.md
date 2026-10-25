# Testing

## Commands

Run from the `backend` folder with the virtual environment active:

```powershell
pip install -e ".[dev]"
pytest
ruff check .
```

## Current test coverage

- `tests/test_health.py` — checks `/health` returns `ok` when the database probe succeeds and `degraded` when it fails. The probe is replaced by a stub, so these tests do not need a running PostgreSQL.

## Verification status

| Check | Status |
|---|---|
| Python syntax (`py_compile`) | run, passed |
| `pytest` | passed (2 of 2) on Windows, Python 3.14.7, user's machine |
| `ruff check` | passed on Windows, user's machine |
| Manual `uvicorn` start against local PostgreSQL | passed: `/health` returned `database: up` |

A check moves to "passed" only after its output has been observed and recorded here.

## Automated launcher

`run.bat` in the repository root creates the virtual environment, installs dependencies, runs pytest and ruff, then starts the server.

## Manual verification

1. Start PostgreSQL and make sure the `marketpilot` database exists.
2. Start the API with `uvicorn app.main:app --reload --port 8000` from `backend`.
3. Open `http://localhost:8000/health`. Expected: `"status": "ok"` and `"database": "up"`.
4. Stop PostgreSQL, refresh the page. Expected: `"status": "degraded"` and `"database": "down"`, with HTTP 200 still returned.
