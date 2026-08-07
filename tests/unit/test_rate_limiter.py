from __future__ import annotations

import time

from app.core.rate_limit.rate_limiter import RateLimiter


def test_each_client_has_independent_bucket() -> None:
    limiter = RateLimiter(
        capacity=1,
        refill_rate=1,
    )

    assert limiter.allow("alice") is True
    assert limiter.allow("bob") is True

    assert limiter.allow("alice") is False
    assert limiter.allow("bob") is False


def test_bucket_refills_per_client() -> None:
    limiter = RateLimiter(
        capacity=1,
        refill_rate=10,
    )

    assert limiter.allow("alice") is True
    assert limiter.allow("alice") is False

    time.sleep(0.2)

    assert limiter.allow("alice") is True
