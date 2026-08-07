from __future__ import annotations

from unittest.mock import AsyncMock

from app.application.provider_selection.capabilities.capability_registry import (
    CapabilityRegistry,
)
from app.application.provider_selection.capabilities.model_capability import (
    ModelCapability,
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
from app.application.provider_selection.smart_provider_selector import (
    SmartProviderSelector,
)
from app.core.resilience.circuit_breaker import CircuitBreaker
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


def test_selects_live_provider() -> None:
    registry = ProviderRegistry()
    registry.register("groq", AsyncMock())

    health = HealthMonitor()
    health.register("groq")

    metrics = ProviderMetricsRegistry()
    metrics.register("groq")

    breakers = CircuitBreakerRegistry()
    breakers.register("groq", CircuitBreaker())

    weights = ProviderWeights()
    weights.register("groq", 80)

    costs = ProviderCosts()
    costs.register("groq", 0.20)

    capabilities = CapabilityRegistry()
    capabilities.register(
        ModelCapability(
            provider="groq",
        ),
    )

    history = ProviderHistoryRegistry()
    history.register("groq")

    selector = SmartProviderSelector(
        health_monitor=health,
        metrics=metrics,
        registry=registry,
        breakers=breakers,
        weights=weights,
        costs=costs,
        capabilities=capabilities,
        history=history,
    )

    selected = selector.select(
        ProviderRequest(),
    )

    assert selected.provider == "groq"
