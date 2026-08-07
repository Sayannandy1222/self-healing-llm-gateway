from app.core.resilience.circuit_breaker import CircuitBreaker
from app.core.resilience.circuit_breaker_registry import (
    CircuitBreakerRegistry,
)


def test_register_breaker() -> None:
    registry = CircuitBreakerRegistry()

    breaker = CircuitBreaker()

    registry.register(
        "groq",
        breaker,
    )

    assert registry.contains("groq")
    assert registry.get("groq") is breaker


def test_registered_providers() -> None:
    registry = CircuitBreakerRegistry()

    registry.register(
        "groq",
        CircuitBreaker(),
    )

    registry.register(
        "gemini",
        CircuitBreaker(),
    )

    assert registry.providers() == [
        "gemini",
        "groq",
    ]
