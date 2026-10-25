from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.db import check_database, make_engine

APP_VERSION = "0.1.0"


def create_app() -> FastAPI:
    settings = get_settings()
    engine = make_engine(settings.database_url)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        engine.dispose()

    app = FastAPI(
        title="MarketPilot API",
        version=APP_VERSION,
        lifespan=lifespan,
    )
    app.state.engine = engine

    @app.get("/health", tags=["system"])
    def health() -> dict[str, object]:
        """Report service status and whether PostgreSQL is reachable."""
        db_ok = check_database(engine)
        return {
            "status": "ok" if db_ok else "degraded",
            "version": APP_VERSION,
            "environment": settings.app_env,
            "database": "up" if db_ok else "down",
        }

    return app


app = create_app()
