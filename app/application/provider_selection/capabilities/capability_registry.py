from __future__ import annotations

from app.application.provider_selection.capabilities.model_capability import (
    ModelCapability,
)


class CapabilityRegistry:
    """
    Registry of provider capabilities.
    """

    def __init__(self) -> None:
        self._capabilities: dict[str, ModelCapability] = {}

    def register(
        self,
        capability: ModelCapability,
    ) -> None:
        self._capabilities[capability.provider] = capability

    def get(
        self,
        provider: str,
    ) -> ModelCapability:
        return self._capabilities[provider]

    def supports_vision(
        self,
        provider: str,
    ) -> bool:
        return self.get(
            provider,
        ).supports_vision

    def supports_reasoning(
        self,
        provider: str,
    ) -> bool:
        return self.get(
            provider,
        ).supports_reasoning

    def supports_streaming(
        self,
        provider: str,
    ) -> bool:
        return self.get(
            provider,
        ).supports_streaming

    def supports_text(
        self,
        provider: str,
    ) -> bool:
        return self.get(
            provider,
        ).supports_text

    def max_context(
        self,
        provider: str,
    ) -> int:
        return self.get(
            provider,
        ).max_context_tokens

    def providers(
        self,
    ) -> list[str]:
        return sorted(
            self._capabilities.keys(),
        )
