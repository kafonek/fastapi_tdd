import secrets

from pydantic import BaseSettings, Field


### Reminder: Pydantic Settings implicitly accepts config from
### environ variables matching the attribute name
class Settings(BaseSettings):
    DATABASE_URL: str = Field(default="sqlite://:memory:")
    DB_ECHO: bool = Field(default=False)

    ### JWT token stuff
    SECRET_KEY: str = Field(default=secrets.token_hex(32))
    ACCESS_TOKEN_EXPIRES_MINUTES: int = Field(default=60 * 24 * 7)


settings = Settings()
