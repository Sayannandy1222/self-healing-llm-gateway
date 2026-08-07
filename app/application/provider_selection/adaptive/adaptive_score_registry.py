from __future__ import annotations

from app.application.provider_selection.adaptive.adaptive_score import (
    AdaptiveScore,
)


class AdaptiveScoreRegistry:
    """
    Stores adaptive routing scores.
    """

    def __init__(self) -> None:
        self._scores: dict[str, AdaptiveScore] = {}

    def register(
        self,
        provider: str,
    ) -> None:
        self._scores[provider] = AdaptiveScore(
            provider=provider,
        )

    def get(
        self,
        provider: str,
    ) -> AdaptiveScore:
        return self._scores[provider]

    def increase(
        self,
        provider: str,
        amount: float = 1.0,
    ) -> None:
        self.get(provider).increase(amount)

    def decrease(
        self,
        provider: str,
        amount: float = 1.0,
    ) -> None:
        self.get(provider).decrease(amount)

    def providers(
        self,
    ) -> list[str]:
        return sorted(
            self._scores.keys(),
        )
