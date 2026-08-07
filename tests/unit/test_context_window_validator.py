from __future__ import annotations

from app.application.provider_selection.context_window.context_window_validator import (
    ContextWindowValidator,
)


def test_context_supported() -> None:
    assert ContextWindowValidator.supports(
        provider_context_window=1_000_000,
        required_context_window=128_000,
    )


def test_context_not_supported() -> None:
    assert not ContextWindowValidator.supports(
        provider_context_window=8_192,
        required_context_window=128_000,
    )


def test_equal_context_supported() -> None:
    assert ContextWindowValidator.supports(
        provider_context_window=32_768,
        required_context_window=32_768,
    )
