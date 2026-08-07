from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AdaptiveScore:
    """
    Runtime adaptive score for a provider.
    """

    provider: str

    score: float = 100.0

    def increase(
        self,
        amount: float = 1.0,
    ) -> None:
        self.score = min(
            100.0,
            self.score + amount,
        )

    def decrease(
        self,
        amount: float = 1.0,
    ) -> None:
        self.score = max(
            0.0,
            self.score - amount,
        )
