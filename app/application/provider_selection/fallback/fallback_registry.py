from __future__ import annotations

from app.application.provider_selection.fallback.fallback_chain import (
    FallbackChain,
)


class FallbackRegistry:
    """
    Stores provider fallback chains.
    """

    def __init__(self) -> None:
        self._chains: dict[str, FallbackChain] = {}

    def register(
        self,
        primary: str,
        fallback: str,
    ) -> None:
        self._chains[primary] = FallbackChain(
            primary=primary,
            fallback=fallback,
        )

    def get(
        self,
        provider: str,
    ) -> FallbackChain:
        return self._chains[provider]

    def contains(
        self,
        provider: str,
    ) -> bool:
        return provider in self._chains

    def providers(self) -> list[str]:
        return sorted(
            self._chains.keys(),
        )
