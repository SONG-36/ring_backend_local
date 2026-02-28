import os
from functools import lru_cache


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "ring_backend")

    ENV: str = os.getenv("ENV", "dev")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    REPOSITORY_TYPE: str = os.getenv("REPOSITORY_TYPE", "memory")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "fake")

    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")


@lru_cache()
def get_settings() -> Settings:
    return Settings()