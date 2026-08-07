from __future__ import annotations

from app.application.provider_selection.history_registry import (
    ProviderHistoryRegistry,
)


def test_register_provider() -> None:
    registry = ProviderHistoryRegistry()

    registry.register(
        "groq",
    )

    assert (
        registry.get(
            "groq",
        ).provider
        == "groq"
    )


def test_record_success() -> None:
    registry = ProviderHistoryRegistry()

    registry.register(
        "groq",
    )

    registry.record_success(
        "groq",
    )

    assert registry.get("groq").successful_requests == 1


def test_record_failure() -> None:
    registry = ProviderHistoryRegistry()

    registry.register(
        "groq",
    )

    registry.record_failure(
        "groq",
    )

    assert registry.get("groq").failed_requests == 1


def test_record_retry() -> None:
    registry = ProviderHistoryRegistry()

    registry.register(
        "groq",
    )

    registry.record_retry(
        "groq",
    )

    assert registry.get("groq").retry_requests == 1


def test_record_timeout() -> None:
    registry = ProviderHistoryRegistry()

    registry.register(
        "groq",
    )

    registry.record_timeout(
        "groq",
    )

    assert registry.get("groq").timeout_requests == 1


def test_registered_providers() -> None:
    registry = ProviderHistoryRegistry()

    registry.register("groq")
    registry.register("gemini")

    assert registry.providers() == [
        "gemini",
        "groq",
    ]
