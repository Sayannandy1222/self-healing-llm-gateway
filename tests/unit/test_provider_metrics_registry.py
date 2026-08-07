from app.infrastructure.metrics.provider_metrics_registry import (
    ProviderMetricsRegistry,
)


def test_register_metrics() -> None:
    registry = ProviderMetricsRegistry()

    registry.register("groq")

    assert registry.contains("groq")


def test_registered_providers() -> None:
    registry = ProviderMetricsRegistry()

    registry.register("groq")
    registry.register("gemini")

    assert registry.providers() == [
        "gemini",
        "groq",
    ]
