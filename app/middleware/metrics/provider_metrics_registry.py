from __future__ import annotations

from app.infrastructure.metrics.provider_metrics import ProviderMetrics


class ProviderMetricsRegistry:
    """
    Stores metrics for every registered provider.
    """

    def __init__(self) -> None:
        self._metrics: dict[str, ProviderMetrics] = {}

    def register(
        self,
        provider: str,
    ) -> None:
        self._metrics[provider] = ProviderMetrics(provider=provider)

    def get(
        self,
        provider: str,
    ) -> ProviderMetrics:
        return self._metrics[provider]

    def contains(
        self,
        provider: str,
    ) -> bool:
        return provider in self._metrics

    def providers(self) -> list[str]:
        return sorted(self._metrics.keys())
