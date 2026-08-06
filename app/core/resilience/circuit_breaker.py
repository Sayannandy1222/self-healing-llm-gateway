from __future__ import annotations

import time

from app.core.resilience.circuit_state import CircuitState


class CircuitBreaker:
    """
    Production-ready circuit breaker.

    Prevents requests from reaching an unhealthy dependency.
    """

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
    ) -> None:
        self._failure_threshold = failure_threshold
        self._recovery_timeout = recovery_timeout

        self._failure_count = 0
        self._success_count = 0

        self._last_failure_time = 0.0

        self._state = CircuitState.CLOSED

    @property
    def state(self) -> CircuitState:
        """
        Current circuit state.
        """
        return self._state

    @property
    def failure_count(self) -> int:
        """
        Number of consecutive failures.
        """
        return self._failure_count

    @property
    def success_count(self) -> int:
        """
        Number of successful executions.
        """
        return self._success_count

    def allow_request(self) -> bool:
        """
        Determine whether a request should be executed.
        """

        if self._state == CircuitState.CLOSED:
            return True

        if self._state == CircuitState.OPEN:
            elapsed = time.monotonic() - self._last_failure_time

            if elapsed >= self._recovery_timeout:
                self._state = CircuitState.HALF_OPEN
                return True

            return False

        # HALF_OPEN allows a trial request.
        return True

    def record_success(self) -> None:
        """
        Record a successful execution.
        """

        self._success_count += 1
        self._failure_count = 0
        self._last_failure_time = 0.0
        self._state = CircuitState.CLOSED

    def record_failure(self) -> None:
        """
        Record a failed execution.
        """

        self._failure_count += 1
        self._last_failure_time = time.monotonic()

        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.OPEN
            return

        if self._failure_count >= self._failure_threshold:
            self._state = CircuitState.OPEN

    def reset(self) -> None:
        """
        Reset the circuit breaker to its initial state.
        """

        self._failure_count = 0
        self._success_count = 0
        self._last_failure_time = 0.0
        self._state = CircuitState.CLOSED
