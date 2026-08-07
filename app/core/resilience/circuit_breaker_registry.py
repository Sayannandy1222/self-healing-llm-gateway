from __future__ import annotations

from app.core.resilience.circuit_breaker import CircuitBreaker


class CircuitBreakerRegistry:
    """
    Stores one circuit breaker per provider.
    """

    def __init__(self) -> None:
        self._breakers: dict[str, CircuitBreaker] = {}

    def register(
        self,
        provider: str,
        breaker: CircuitBreaker,
    ) -> None:
        self._breakers[provider] = breaker

    def get(
        self,
        provider: str,
    ) -> CircuitBreaker:
        return self._breakers[provider]

    def contains(
        self,
        provider: str,
    ) -> bool:
        return provider in self._breakers

    def providers(self) -> list[str]:
        return sorted(self._breakers.keys())
