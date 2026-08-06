from __future__ import annotations

from datetime import datetime

from app.infrastructure.telemetry.provider_health import ProviderHealth


class HealthMonitor:
    """
    Tracks provider runtime health.
    """

    def __init__(self) -> None:
        self._providers: dict[str, ProviderHealth] = {}

    def register(self, provider: str) -> None:
        self._providers[provider] = ProviderHealth(provider=provider)

    def mark_healthy(
        self,
        provider: str,
        latency_ms: float,
    ) -> None:
        health = self._providers[provider]

        health.healthy = True
        health.failure_count = 0
        health.latency_ms = latency_ms
        health.last_checked = datetime.utcnow()

    def mark_unhealthy(
        self,
        provider: str,
    ) -> None:
        health = self._providers[provider]

        health.failure_count += 1
        health.healthy = False
        health.last_checked = datetime.utcnow()

    def is_healthy(
        self,
        provider: str,
    ) -> bool:
        return self._providers[provider].healthy

    def get(
        self,
        provider: str,
    ) -> ProviderHealth:
        return self._providers[provider]
