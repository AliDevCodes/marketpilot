# MarketPilot

A personal, local-first market-research and paper-trading workspace. It helps monitor markets, test explicit trading rules, track a simulated portfolio, keep a trading journal, and export evidence for later analysis.

**Status:** early skeleton. Only the backend health endpoint exists. See [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md).

**Not included:** real-money trading, broker connections, or guaranteed-profit forecasts.

## Prerequisites

- Python 3.12 or newer
- A local PostgreSQL server (Docker is not required)

## Local setup

1. Create a database and user in your local PostgreSQL (for example with `psql` or pgAdmin):

   ```sql
   CREATE USER marketpilot WITH PASSWORD 'choose-a-password';
   CREATE DATABASE marketpilot OWNER marketpilot;
   ```

2. Copy the environment template and set your password:

   ```powershell
   Copy-Item .env.example .env
   ```

   Then edit `.env` so `DATABASE_URL` matches your user, password and port.

3. Install the backend in a virtual environment:

   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -e ".[dev]"
   ```

4. Run the API:

   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```

5. Check it: open `http://localhost:8000/health`. `"database": "up"` means PostgreSQL is reachable.

Run the tests with `pytest` from the `backend` folder. Current verified commands are listed in [docs/TESTING.md](docs/TESTING.md).

## Documentation

- [AGENTS.md](AGENTS.md) — rules for AI agents and the approval gate
- [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md) — current verified status
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — planned module boundaries
- [docs/DEVELOPMENT_WORKFLOW.md](docs/DEVELOPMENT_WORKFLOW.md) — how changes are built, verified and committed
- [docs/TESTING.md](docs/TESTING.md) — verified test and run commands
