from __future__ import annotations

import time

from app.core.rate_limit.token_bucket import TokenBucket


def test_bucket_allows_initial_requests() -> None:
    bucket = TokenBucket(
        capacity=2,
        refill_rate=1,
    )

    assert bucket.allow() is True
    assert bucket.allow() is True
    assert bucket.allow() is False


def test_bucket_refills() -> None:
    bucket = TokenBucket(
        capacity=1,
        refill_rate=10,
    )

    assert bucket.allow() is True
    assert bucket.allow() is False

    time.sleep(0.2)

    assert bucket.allow() is True
