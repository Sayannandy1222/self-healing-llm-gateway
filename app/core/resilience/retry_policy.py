from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RetryPolicy:
    """
    Immutable retry configuration.
    """

    max_attempts: int = 3

    initial_delay: float = 0.5

    backoff_factor: float = 2.0

    max_delay: float = 8.0

    jitter: bool = True
