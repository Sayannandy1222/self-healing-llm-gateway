from __future__ import annotations

from app.domain.providers.provider import LLMProvider


class ProviderRegistry:
    """
    Registry responsible for storing provider instances.
    """

    def __init__(self) -> None:
        self._providers: dict[str, LLMProvider] = {}

    def register(
        self,
        name: str,
        provider: LLMProvider,
    ) -> None:
        """
        Register a provider.
        """
        self._providers[name] = provider

    def get(
        self,
        name: str,
    ) -> LLMProvider:
        """
        Resolve a provider by name.
        """
        try:
            return self._providers[name]
        except KeyError as exc:
            raise ValueError(f"Provider '{name}' is not registered.") from exc

    def contains(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a provider is registered.
        """
        return name in self._providers

    def registered_names(self) -> list[str]:
        """
        Return all registered provider names.
        """
        return sorted(self._providers.keys())
