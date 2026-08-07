from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FallbackChain:
    """
    Defines the fallback order for a provider.
    """

    primary: str

    fallback: str
