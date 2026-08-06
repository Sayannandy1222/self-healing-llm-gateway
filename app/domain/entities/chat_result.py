from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ChatResult:
    """
    Immutable domain entity representing the output produced by an LLM.
    """

    response: str

    provider: str

    model: str

    finish_reason: str | None = None
