from __future__ import annotations

from app.application.provider_selection.adaptive.adaptive_score import (
    AdaptiveScore,
)


def test_default_score() -> None:
    score = AdaptiveScore(
        provider="groq",
    )

    assert score.score == 100.0


def test_decrease_score() -> None:
    score = AdaptiveScore(
        provider="groq",
    )

    score.decrease(20)

    assert score.score == 80.0


def test_increase_score() -> None:
    score = AdaptiveScore(
        provider="groq",
        score=50.0,
    )

    score.increase(10)

    assert score.score == 60.0


def test_score_upper_bound() -> None:
    score = AdaptiveScore(
        provider="groq",
    )

    score.increase(100)

    assert score.score == 100.0


def test_score_lower_bound() -> None:
    score = AdaptiveScore(
        provider="groq",
    )

    score.decrease(500)

    assert score.score == 0.0
