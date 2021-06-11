import logging
import os
import secrets
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: str = os.getenv("DATABASE_URL", "sqlite://")
    secret_key: str = os.getenv("SECRET_KEY", secrets.token_hex(32))


@lru_cache
def get_settings():
    log.info("Loading config settings from environment")
    return Settings()
