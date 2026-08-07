from __future__ import annotations

from app.domain.providers.provider import LLMProvider
from app.infrastructure.registry.provider_registry import ProviderRegistry
from app.infrastructure.telemetry.health_monitor import HealthMonitor


class ProviderSelector:
    """
    Selects the healthiest available provider.
    """

    def __init__(
        self,
        registry: ProviderRegistry,
        health_monitor: HealthMonitor,
    ) -> None:
        self._registry = registry
        self._health_monitor = health_monitor

    def select(self) -> LLMProvider:
        """
        Return the healthiest provider.
        """

        if self._health_monitor.is_healthy("groq"):
            return self._registry.get("groq")

        return self._registry.get("gemini")
