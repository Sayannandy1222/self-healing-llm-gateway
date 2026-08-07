from __future__ import annotations

from app.core.cors.cors_config import CORSConfig


def test_default_configuration() -> None:
    config = CORSConfig()

    assert config.allow_credentials is True

    assert config.is_origin_allowed(
        "https://example.com",
    )


def test_specific_origin_allowed() -> None:
    config = CORSConfig(
        allow_origins=[
            "https://example.com",
        ],
    )

    assert config.is_origin_allowed(
        "https://example.com",
    )


def test_specific_origin_denied() -> None:
    config = CORSConfig(
        allow_origins=[
            "https://example.com",
        ],
    )

    assert (
        config.is_origin_allowed(
            "https://google.com",
        )
        is False
    )
