from __future__ import annotations

from app.infrastructure.metrics.provider_metrics import ProviderMetrics


class ProviderMetricsRegistry:
    """
    Stores runtime metrics for every registered provider.
    """

    def __init__(self) -> None:
        self._metrics: dict[str, ProviderMetrics] = {}

    def register(
        self,
        provider: str,
    ) -> None:
        """
        Register a provider if it has not already been registered.
        """
        if provider not in self._metrics:
            self._metrics[provider] = ProviderMetrics(
                provider=provider,
            )

    def get(
        self,
        provider: str,
    ) -> ProviderMetrics:
        """
        Return metrics for a provider.
        """
        return self._metrics[provider]

    def contains(
        self,
        provider: str,
    ) -> bool:
        """
        Check whether a provider has been registered.
        """
        return provider in self._metrics

    def providers(self) -> list[str]:
        """
        Return all registered providers.
        """
        return sorted(self._metrics.keys())
