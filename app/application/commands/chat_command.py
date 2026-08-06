from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ChatCommand:
    """
    Immutable application command representing a chat request.
    """

    prompt: str
    model: str
    provider: str
