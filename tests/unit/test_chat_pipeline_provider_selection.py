from __future__ import annotations

from unittest.mock import Mock

from app.application.resolver.provider_selector import ProviderSelector
from app.infrastructure.registry.provider_registry import ProviderRegistry
from app.infrastructure.telemetry.health_monitor import HealthMonitor


def test_select_groq_when_healthy() -> None:
    registry = ProviderRegistry()
    monitor = HealthMonitor()

    groq = Mock(name="groq")
    gemini = Mock(name="gemini")

    registry.register("groq", groq)
    registry.register("gemini", gemini)

    monitor.register("groq")
    monitor.register("gemini")

    selector = ProviderSelector(
        registry=registry,
        health_monitor=monitor,
    )

    provider = selector.select()

    assert provider is groq


def test_select_gemini_when_groq_unhealthy() -> None:
    registry = ProviderRegistry()
    monitor = HealthMonitor()

    groq = Mock(name="groq")
    gemini = Mock(name="gemini")

    registry.register("groq", groq)
    registry.register("gemini", gemini)

    monitor.register("groq")
    monitor.register("gemini")

    monitor.mark_unhealthy("groq")

    selector = ProviderSelector(
        registry=registry,
        health_monitor=monitor,
    )

    provider = selector.select()

    assert provider is gemini
