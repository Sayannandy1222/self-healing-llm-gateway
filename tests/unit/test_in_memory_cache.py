from __future__ import annotations

import time

from app.infrastructure.cache.in_memory_cache import InMemoryCache


def test_cache_returns_value() -> None:
    cache = InMemoryCache()

    cache.set(
        key="hello",
        value="world",
        ttl=10,
    )

    assert cache.get("hello") == "world"


def test_cache_expires() -> None:
    cache = InMemoryCache()

    cache.set(
        key="hello",
        value="world",
        ttl=1,
    )

    time.sleep(1.1)

    assert cache.get("hello") is None
