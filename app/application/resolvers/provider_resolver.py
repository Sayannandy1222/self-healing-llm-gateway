from __future__ import annotations

from app.application.factories.provider_factory import ProviderFactory
from app.domain.providers.provider import LLMProvider


class ProviderResolver:
    """
    Resolves the provider used for request execution.

    This abstraction allows the provider selection strategy
    to evolve without changing the pipeline.
    """

    def resolve(self) -> LLMProvider:
        """
        Resolve the configured provider.
        """

        return ProviderFactory.create()
