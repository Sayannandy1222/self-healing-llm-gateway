from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ProviderRequest:
    """
    Describes the routing requirements for an incoming request.
    """

    requires_text: bool = True

    requires_streaming: bool = False

    requires_reasoning: bool = False

    requires_vision: bool = False

    min_context_tokens: int = 0

    session_id: str | None = None

    preferred_provider: str | None = None
