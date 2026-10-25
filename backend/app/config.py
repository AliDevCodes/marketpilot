from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration read from environment variables or a local .env file."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = Field(
        ...,
        description="SQLAlchemy URL for the local PostgreSQL database, e.g. postgresql+psycopg://...",
    )
    app_env: Literal["development", "test", "production"] = "development"
    base_currency: str = Field(default="IRT", min_length=2, max_length=10)


@lru_cache
def get_settings() -> Settings:
    return Settings()
