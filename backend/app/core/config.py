from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env.prod', '.env.dev'),
        case_sensitive=True
    )

    DB_STR_CONNECTION: str
    DB_ECHO: bool = True


@lru_cache
def get_settings():
    return Settings()

