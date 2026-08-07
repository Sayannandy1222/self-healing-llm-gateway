from __future__ import annotations

from dataclasses import dataclass

from app.application.provider_selection.capabilities.capability_registry import (
    CapabilityRegistry,
)
from app.application.provider_selection.config.provider_weights import (
    ProviderWeights,
)
from app.application.provider_selection.cost.provider_costs import (
    ProviderCosts,
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


@dataclass(slots=True, frozen=True)
class ProviderSelectionContext:
    """
    Groups together all dependencies required by the
    SmartProviderSelector.
    """

    health: HealthMonitor

    metrics: ProviderMetricsRegistry

    registry: ProviderRegistry

    breakers: CircuitBreakerRegistry

    weights: ProviderWeights

    costs: ProviderCosts

    capabilities: CapabilityRegistry
