from __future__ import annotations

from app.application.provider_selection.provider_score import (
    ProviderScore,
)


def test_total_score() -> None:
    score = ProviderScore(
        provider="groq",
        health_score=50,
        latency_score=30,
        weight_score=20,
    )

    assert score.total_score == 100
