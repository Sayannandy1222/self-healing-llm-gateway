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

    app_version: str = "1.0.0"

    environment: str = Field(
        default="development",
        alias="APP_ENVIRONMENT",
    )

    groq_api_key: str = Field(
        alias="GROQ_API_KEY",
    )

    gemini_api_key: str = Field(
        alias="GEMINI_API_KEY",
    )

    default_model: str = Field(
        default="llama-3.3-70b-versatile",
        alias="DEFAULT_MODEL",
    )

    gemini_model: str = Field(
        default="gemini-2.5-flash",
        alias="GEMINI_MODEL",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.
    """
    return Settings()  # type: ignore[call-arg]


settings = get_settings()
