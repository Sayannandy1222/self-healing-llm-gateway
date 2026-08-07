from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from app.application.load_balancing.round_robin import (
    RoundRobinLoadBalancer,
)
from app.infrastructure.telemetry.health_monitor import (
    HealthMonitor,
)


def test_skips_unhealthy_provider() -> None:
    health = HealthMonitor()

    health.register("groq")
    health.register("gemini")

    health.mark_unhealthy("groq")

    groq = AsyncMock()
    gemini = AsyncMock()

    balancer = RoundRobinLoadBalancer(
        providers={
            "groq": groq,
            "gemini": gemini,
        },
        health_monitor=health,
    )

    assert balancer.next_provider() is gemini


def test_raises_when_every_provider_is_down() -> None:
    health = HealthMonitor()

    health.register("groq")

    health.mark_unhealthy("groq")

    balancer = RoundRobinLoadBalancer(
        providers={
            "groq": AsyncMock(),
        },
        health_monitor=health,
    )

    with pytest.raises(RuntimeError):
        balancer.next_provider()
