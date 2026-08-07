from __future__ import annotations

from app.core.resilience.circuit_breaker import CircuitBreaker
from app.core.resilience.circuit_breaker_registry import (
    CircuitBreakerRegistry,
)


def test_register_breaker() -> None:
    registry = CircuitBreakerRegistry()

    breaker = CircuitBreaker()

    registry.register(
        provider="groq",
        breaker=breaker,
    )

    assert registry.contains("groq") is True
    assert registry.get("groq") is breaker


def test_multiple_breakers() -> None:
    registry = CircuitBreakerRegistry()

    groq = CircuitBreaker()
    gemini = CircuitBreaker()

    registry.register(
        provider="groq",
        breaker=groq,
    )

    registry.register(
        provider="gemini",
        breaker=gemini,
    )

    assert registry.providers() == [
        "gemini",
        "groq",
    ]

    assert registry.get("groq") is groq
    assert registry.get("gemini") is gemini
