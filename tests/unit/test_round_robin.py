from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from app.application.load_balancing.round_robin import (
    RoundRobinLoadBalancer,
)


def test_round_robin_rotates_providers() -> None:
    groq = AsyncMock()
    gemini = AsyncMock()

    balancer = RoundRobinLoadBalancer(
        providers=[
            groq,
            gemini,
        ],
    )

    assert balancer.next_provider() is groq
    assert balancer.next_provider() is gemini
    assert balancer.next_provider() is groq
    assert balancer.next_provider() is gemini


def test_round_robin_requires_provider() -> None:
    with pytest.raises(ValueError):
        RoundRobinLoadBalancer(
            providers=[],
        )
