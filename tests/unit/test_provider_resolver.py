import pytest

from app.application.resolver.provider_resolver import ProviderResolver
from app.infrastructure.providers.groq_provider import GroqProvider
from app.infrastructure.registry.provider_registry import ProviderRegistry


def test_resolve_registered_provider() -> None:
    registry = ProviderRegistry()

    provider = GroqProvider()

    registry.register(
        "groq",
        provider,
    )

    resolver = ProviderResolver(registry)

    assert resolver.resolve("groq") is provider


def test_resolve_unknown_provider() -> None:
    registry = ProviderRegistry()

    resolver = ProviderResolver(registry)

    with pytest.raises(ValueError):
        resolver.resolve("openai")
