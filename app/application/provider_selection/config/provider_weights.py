from __future__ import annotations


class ProviderWeights:
    """
    Stores routing weights for providers.

    Higher weight means the provider is preferred
    when all other factors are equal.
    """

    def __init__(self) -> None:
        self._weights: dict[str, float] = {}

    def register(
        self,
        provider: str,
        weight: float,
    ) -> None:
        """
        Register a provider weight.
        """

        if weight < 0:
            raise ValueError(
                "Weight must be non-negative.",
            )

        self._weights[provider] = weight

    def get(
        self,
        provider: str,
    ) -> float:
        """
        Return the configured weight.

        Defaults to 50 if not configured.
        """

        return self._weights.get(
            provider,
            50.0,
        )

    def contains(
        self,
        provider: str,
    ) -> bool:
        return provider in self._weights

    def providers(
        self,
    ) -> list[str]:
        return sorted(
            self._weights.keys(),
        )
