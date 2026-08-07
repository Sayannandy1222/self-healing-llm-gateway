from __future__ import annotations

import time


class TokenBucket:
    """
    Token Bucket rate limiter.

    Allows bursts while enforcing an average request rate.
    """

    def __init__(
        self,
        capacity: int,
        refill_rate: float,
    ) -> None:
        self._capacity = capacity
        self._tokens = float(capacity)
        self._refill_rate = refill_rate
        self._last_refill = time.monotonic()

    def allow(self) -> bool:
        """
        Return True if a request is allowed.
        """
        now = time.monotonic()

        elapsed = now - self._last_refill

        self._tokens = min(
            self._capacity,
            self._tokens + elapsed * self._refill_rate,
        )

        self._last_refill = now

        if self._tokens < 1:
            return False

        self._tokens -= 1

        return True
