from __future__ import annotations

from app.application.provider_selection.fallback.fallback_registry import (
    FallbackRegistry,
)


def test_register_chain() -> None:
    registry = FallbackRegistry()

    registry.register(
        "groq",
        "gemini",
    )

    chain = registry.get(
        "groq",
    )

    assert chain.primary == "groq"
    assert chain.fallback == "gemini"


def test_contains_chain() -> None:
    registry = FallbackRegistry()

    registry.register(
        "groq",
        "gemini",
    )

    assert registry.contains("groq")


def test_registered_providers() -> None:
    registry = FallbackRegistry()

    registry.register(
        "groq",
        "gemini",
    )

    assert registry.providers() == [
        "groq",
    ]
