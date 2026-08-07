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
        """
        Register a circuit breaker for a provider.
        """
        self._breakers[provider] = breaker

    def get(
        self,
        provider: str,
    ) -> CircuitBreaker:
        """
        Return the provider's circuit breaker.
        """
        return self._breakers[provider]

    def contains(
        self,
        provider: str,
    ) -> bool:
        """
        Check whether a provider has a registered circuit breaker.
        """
        return provider in self._breakers

    def providers(self) -> list[str]:
        """
        Return all registered providers.
        """
        return sorted(self._breakers.keys())
