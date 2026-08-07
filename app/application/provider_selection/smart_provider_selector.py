from __future__ import annotations

from app.application.provider_selection.capabilities.capability_registry import (
    CapabilityRegistry,
)
from app.application.provider_selection.config.provider_weights import (
    ProviderWeights,
)
from app.application.provider_selection.cost.provider_costs import (
    ProviderCosts,
)
from app.application.provider_selection.history_registry import (
    ProviderHistoryRegistry,
)
from app.application.provider_selection.provider_request import (
    ProviderRequest,
)
from app.application.provider_selection.provider_score import (
    ProviderScore,
)
from app.core.resilience.circuit_breaker_registry import (
    CircuitBreakerRegistry,
)
from app.infrastructure.metrics.provider_metrics_registry import (
    ProviderMetricsRegistry,
)
from app.infrastructure.registry.provider_registry import (
    ProviderRegistry,
)
from app.infrastructure.telemetry.health_monitor import (
    HealthMonitor,
)


class SmartProviderSelector:
    """
    Production intelligent provider selector.
    """

    def __init__(
        self,
        health_monitor: HealthMonitor,
        metrics: ProviderMetricsRegistry,
        registry: ProviderRegistry,
        breakers: CircuitBreakerRegistry,
        weights: ProviderWeights,
        costs: ProviderCosts,
        capabilities: CapabilityRegistry,
        history: ProviderHistoryRegistry,
    ) -> None:
        self._health = health_monitor
        self._metrics = metrics
        self._registry = registry
        self._breakers = breakers
        self._weights = weights
        self._costs = costs
        self._capabilities = capabilities
        self._history = history

    def scores(
        self,
        request: ProviderRequest,
    ) -> list[ProviderScore]:
        """
        Build provider scores from runtime state.
        """

        results: list[ProviderScore] = []

        for provider in self._registry.registered_names():
            if not self._health.is_healthy(provider):
                continue

            capability = self._capabilities.get(provider)

            if request.requires_vision and not capability.supports_vision:
                continue

            if request.requires_reasoning and not capability.supports_reasoning:
                continue

            if request.requires_streaming and not capability.supports_streaming:
                continue

            if capability.max_context_tokens < request.min_context_tokens:
                continue

            metric = self._metrics.get(provider)

            latency_score = max(
                0.0,
                100.0 - metric.average_latency_ms,
            )

            cost_score = self._costs.score(provider)

            history_score = self._history.get(provider).success_rate

            results.append(
                ProviderScore(
                    provider=provider,
                    health_score=100.0,
                    latency_score=latency_score,
                    weight_score=(
                        self._weights.get(provider) + cost_score + history_score
                    ),
                ),
            )

        return results

    def select(
        self,
        request: ProviderRequest,
    ) -> ProviderScore:
        """
        Return the highest-scoring compatible provider.
        """

        scores = self.scores(request)

        if not scores:
            raise RuntimeError(
                "No compatible providers available.",
            )

        return max(
            scores,
            key=lambda provider: provider.total_score,
        )
