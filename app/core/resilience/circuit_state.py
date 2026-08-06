from enum import StrEnum


class CircuitState(StrEnum):
    """
    Represents the current state of a circuit breaker.
    """

    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"
