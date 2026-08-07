from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RoutingConfig:
    """
    Runtime configuration for provider routing.
    """

    enable_sticky_routing: bool = True

    enable_fallback: bool = True

    enable_history: bool = True

    enable_adaptive_scoring: bool = True

    enable_cost_routing: bool = True

    enable_latency_routing: bool = True

    enable_capability_filter: bool = True

    enable_context_filter: bool = True

    enable_circuit_breaker: bool = True
