from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application configuration.
    """

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    app_name: str = "Self-Healing LLM Gateway"
    app_version: str = "0.1.0"
    app_environment: str = Field(default="development")

    # ------------------------------------------------------------------
    # API
    # ------------------------------------------------------------------

    api_v1_prefix: str = "/api/v1"

    # ------------------------------------------------------------------
    # Groq
    # ------------------------------------------------------------------

    groq_api_key: str = Field(alias="GROQ_API_KEY")

    default_model: str = Field(
        default="llama-3.3-70b-versatile",
        alias="DEFAULT_MODEL",
    )

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()