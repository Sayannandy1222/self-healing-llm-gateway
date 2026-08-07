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
from app.application.provider_selection.provider_selection_context import (
    ProviderSelectionContext,
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


def test_provider_selection_context_creation() -> None:
    context = ProviderSelectionContext(
        health=HealthMonitor(),
        metrics=ProviderMetricsRegistry(),
        registry=ProviderRegistry(),
        breakers=CircuitBreakerRegistry(),
        weights=ProviderWeights(),
        costs=ProviderCosts(),
        capabilities=CapabilityRegistry(),
    )

    assert isinstance(
        context.health,
        HealthMonitor,
    )

    assert isinstance(
        context.metrics,
        ProviderMetricsRegistry,
    )

    assert isinstance(
        context.registry,
        ProviderRegistry,
    )

    assert isinstance(
        context.breakers,
        CircuitBreakerRegistry,
    )

    assert isinstance(
        context.weights,
        ProviderWeights,
    )

    assert isinstance(
        context.costs,
        ProviderCosts,
    )

    assert isinstance(
        context.capabilities,
        CapabilityRegistry,
    )
