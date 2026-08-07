from __future__ import annotations

from app.application.provider_selection.capabilities.capability_registry import (
    CapabilityRegistry,
)
from app.application.provider_selection.capabilities.model_capability import (
    ModelCapability,
)


def test_register_capability() -> None:
    registry = CapabilityRegistry()

    registry.register(
        ModelCapability(
            provider="groq",
        ),
    )

    assert registry.supports_text(
        "groq",
    )


def test_vision_support() -> None:
    registry = CapabilityRegistry()

    registry.register(
        ModelCapability(
            provider="gemini",
            supports_vision=True,
        ),
    )

    assert registry.supports_vision(
        "gemini",
    )


def test_registered_providers() -> None:
    registry = CapabilityRegistry()

    registry.register(
        ModelCapability(
            provider="groq",
        ),
    )

    registry.register(
        ModelCapability(
            provider="gemini",
            supports_vision=True,
        ),
    )

    assert registry.providers() == [
        "gemini",
        "groq",
    ]
