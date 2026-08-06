from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Self-Healing LLM Gateway"

    app_version: str = "0.1.0"

    environment: str = "development"

    groq_api_key: str = Field(
        alias="GROQ_API_KEY",
    )

    default_model: str = "llama-3.3-70b-versatile"


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.
    """
    return Settings()  # type: ignore[call-arg]


settings = get_settings()
