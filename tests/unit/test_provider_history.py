from __future__ import annotations

from app.application.provider_selection.history.provider_history import (
    ProviderHistory,
)


def test_provider_history_defaults() -> None:
    history = ProviderHistory(
        provider="groq",
    )

    assert history.provider == "groq"
    assert history.total_requests == 0
    assert history.success_rate == 100.0


def test_success_tracking() -> None:
    history = ProviderHistory(
        provider="groq",
    )

    history.record_success()
    history.record_success()

    assert history.total_requests == 2
    assert history.success_rate == 100.0


def test_failure_tracking() -> None:
    history = ProviderHistory(
        provider="groq",
    )

    history.record_success()
    history.record_failure()

    assert history.total_requests == 2
    assert history.success_rate == 50.0
    assert history.failure_rate == 50.0


def test_retry_tracking() -> None:
    history = ProviderHistory(
        provider="groq",
    )

    history.record_retry()

    assert history.retry_requests == 1


def test_timeout_tracking() -> None:
    history = ProviderHistory(
        provider="groq",
    )

    history.record_timeout()

    assert history.timeout_requests == 1
