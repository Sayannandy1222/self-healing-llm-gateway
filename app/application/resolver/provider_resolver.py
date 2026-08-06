from __future__ import annotations

from app.domain.providers.provider import LLMProvider
from app.infrastructure.registry.provider_registry import ProviderRegistry


class ProviderResolver:
    """
    Resolves providers using the provider registry.
    """

    def __init__(
        self,
        registry: ProviderRegistry,
    ) -> None:
        self._registry = registry

    def resolve(
        self,
        provider_name: str,
    ) -> LLMProvider:
        """
        Resolve a provider by name.
        """
        return self._registry.get(provider_name)
