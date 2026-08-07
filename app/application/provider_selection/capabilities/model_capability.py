from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ModelCapability:
    """
    Describes the capabilities of a model/provider.
    """

    provider: str

    supports_text: bool = True

    supports_streaming: bool = True

    supports_reasoning: bool = False

    supports_vision: bool = False

    max_context_tokens: int = 8192
