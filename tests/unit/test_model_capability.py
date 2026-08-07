from __future__ import annotations

from app.application.provider_selection.capabilities.model_capability import (
    ModelCapability,
)


def test_model_capability_defaults() -> None:
    capability = ModelCapability(
        provider="groq",
    )

    assert capability.provider == "groq"
    assert capability.supports_text
    assert capability.supports_streaming
    assert capability.max_context_tokens == 8192


def test_model_capability_vision() -> None:
    capability = ModelCapability(
        provider="gemini",
        supports_vision=True,
        supports_reasoning=True,
        max_context_tokens=1048576,
    )

    assert capability.supports_vision
    assert capability.supports_reasoning
    assert capability.max_context_tokens == 1048576
