from __future__ import annotations


class ProviderCosts:
    """
    Stores provider routing costs.

    Lower cost means a provider receives
    a higher routing score.
    """

    def __init__(self) -> None:
        self._costs: dict[str, float] = {}

    def register(
        self,
        provider: str,
        cost: float,
    ) -> None:
        """
        Register provider cost.
        """

        if cost < 0:
            raise ValueError(
                "Cost must be non-negative.",
            )

        self._costs[provider] = cost

    def get(
        self,
        provider: str,
    ) -> float:
        """
        Return provider cost.

        Defaults to 1.0 if unknown.
        """

        return self._costs.get(
            provider,
            1.0,
        )

    def score(
        self,
        provider: str,
    ) -> float:
        """
        Convert cost into routing score.

        Lower cost → higher score.
        """

        cost = self.get(provider)

        return 100.0 / (1.0 + cost)
