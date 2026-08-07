from __future__ import annotations

from enum import StrEnum


class CircuitState(StrEnum):
    """
    Circuit breaker states used for routing penalties.
    """

    CLOSED = "closed"
    HALF_OPEN = "half_open"
    OPEN = "open"


class CircuitPenalty:
    """
    Calculates routing penalty based on circuit state.
    """

    _PENALTIES = {
        CircuitState.CLOSED: 100.0,
        CircuitState.HALF_OPEN: 70.0,
        CircuitState.OPEN: 20.0,
    }

    @classmethod
    def score(
        cls,
        state: CircuitState,
    ) -> float:
        return cls._PENALTIES[state]
