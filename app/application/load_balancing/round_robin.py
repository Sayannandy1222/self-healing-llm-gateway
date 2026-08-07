from __future__ import annotations

from app.domain.providers.provider import LLMProvider
from app.infrastructure.telemetry.health_monitor import HealthMonitor


class RoundRobinLoadBalancer:
    """
    Round-robin load balancer with optional health awareness.
    """

    def __init__(
        self,
        providers: list[LLMProvider] | dict[str, LLMProvider],
        health_monitor: HealthMonitor | None = None,
    ) -> None:
        if not providers:
            raise ValueError("At least one provider is required.")

        self._health_monitor = health_monitor
        self._index = 0

        if isinstance(providers, dict):
            self._providers = providers
            self._provider_names = list(providers.keys())
            self._provider_list = list(providers.values())
        else:
            self._provider_list = providers
            self._providers = {}
            self._provider_names = []

    def next_provider(self) -> LLMProvider:
        """
        Return the next provider.
        """

        # Original round-robin behaviour (used by existing tests)
        if self._health_monitor is None:
            provider = self._provider_list[self._index]
            self._index = (self._index + 1) % len(self._provider_list)
            return provider

        # Health-aware behaviour
        attempts = len(self._provider_names)

        for _ in range(attempts):
            provider_name = self._provider_names[self._index]

            self._index = (self._index + 1) % len(self._provider_names)

            if self._health_monitor.is_healthy(provider_name):
                return self._providers[provider_name]

        raise RuntimeError("No healthy providers available.")
