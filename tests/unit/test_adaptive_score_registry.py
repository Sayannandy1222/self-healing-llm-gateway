from __future__ import annotations

from app.application.provider_selection.adaptive.adaptive_score_registry import (
    AdaptiveScoreRegistry,
)


def test_register_provider() -> None:
    registry = AdaptiveScoreRegistry()

    registry.register(
        "groq",
    )

    assert (
        registry.get(
            "groq",
        ).provider
        == "groq"
    )


def test_increase_score() -> None:
    registry = AdaptiveScoreRegistry()

    registry.register(
        "groq",
    )

    registry.increase(
        "groq",
        10,
    )

    assert (
        registry.get(
            "groq",
        ).score
        == 100.0
    )


def test_decrease_score() -> None:
    registry = AdaptiveScoreRegistry()

    registry.register(
        "groq",
    )

    registry.decrease(
        "groq",
        25,
    )

    assert (
        registry.get(
            "groq",
        ).score
        == 75.0
    )


def test_registered_providers() -> None:
    registry = AdaptiveScoreRegistry()

    registry.register("groq")
    registry.register("gemini")

    assert registry.providers() == [
        "gemini",
        "groq",
    ]
