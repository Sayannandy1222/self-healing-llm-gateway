from __future__ import annotations

import time

from app.infrastructure.cache.cache import Cache


class InMemoryCache(Cache):
    """
    Simple in-memory cache with TTL support.
    """

    def __init__(self) -> None:
        self._storage: dict[str, tuple[str, float]] = {}

    def get(
        self,
        key: str,
    ) -> str | None:
        item = self._storage.get(key)

        if item is None:
            return None

        value, expires_at = item

        if time.time() >= expires_at:
            del self._storage[key]
            return None

        return value

    def set(
        self,
        key: str,
        value: str,
        ttl: int,
    ) -> None:
        self._storage[key] = (
            value,
            time.time() + ttl,
        )
