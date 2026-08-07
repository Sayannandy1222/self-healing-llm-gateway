from __future__ import annotations

from app.application.provider_selection.routing.routing_config import (
    RoutingConfig,
)


def test_default_configuration() -> None:
    config = RoutingConfig()

    assert config.enable_sticky_routing
    assert config.enable_fallback
    assert config.enable_history
    assert config.enable_adaptive_scoring
    assert config.enable_cost_routing
    assert config.enable_latency_routing
    assert config.enable_capability_filter
    assert config.enable_context_filter
    assert config.enable_circuit_breaker


def test_disable_feature() -> None:
    config = RoutingConfig(
        enable_sticky_routing=False,
    )

    assert not config.enable_sticky_routing
