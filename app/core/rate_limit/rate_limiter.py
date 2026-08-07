from __future__ import annotations

from app.core.rate_limit.token_bucket import TokenBucket


class RateLimiter:
    """
    Per-client token bucket rate limiter.
    """

    def __init__(
        self,
        capacity: int,
        refill_rate: float,
    ) -> None:
        self._capacity = capacity
        self._refill_rate = refill_rate
        self._buckets: dict[str, TokenBucket] = {}

    def allow(
        self,
        client_id: str,
    ) -> bool:
        """
        Return whether the client may perform another request.
        """

        if client_id not in self._buckets:
            self._buckets[client_id] = TokenBucket(
                capacity=self._capacity,
                refill_rate=self._refill_rate,
            )

        return self._buckets[client_id].allow()
