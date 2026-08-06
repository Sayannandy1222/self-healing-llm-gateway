from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TimeoutPolicy:
    """
    Immutable timeout configuration.
    """

    timeout_seconds: float = 30.0
