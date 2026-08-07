from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ProviderScore:
    """
    Represents the computed score for a provider.
    """

    provider: str

    health_score: float

    latency_score: float

    weight_score: float

    @property
    def total_score(self) -> float:
        """
        Overall provider score.
        """

        return self.health_score + self.latency_score + self.weight_score
