from __future__ import annotations

from app.application.provider_selection.provider_request import (
    ProviderRequest,
)


def test_provider_request_defaults() -> None:
    request = ProviderRequest()

    assert request.requires_text is True
    assert request.requires_streaming is False
    assert request.requires_reasoning is False
    assert request.requires_vision is False
    assert request.min_context_tokens == 0


def test_provider_request_custom_values() -> None:
    request = ProviderRequest(
        requires_streaming=True,
        requires_reasoning=True,
        requires_vision=True,
        min_context_tokens=32768,
    )

    assert request.requires_streaming
    assert request.requires_reasoning
    assert request.requires_vision
    assert request.min_context_tokens == 32768
