from __future__ import annotations

from typing import Any


class RedisCache:
    """
    Redis cache adapter.

    This implementation stores a Redis client and exposes
    a cache interface compatible with the in-memory cache.
    """

    def __init__(
        self,
        client: Any,
    ) -> None:
        self._client = client

    def get(
        self,
        key: str,
    ) -> str | None:
        value = self._client.get(key)

        if value is None:
            return None

        if isinstance(value, bytes):
            return value.decode()

        return str(value)

    def set(
        self,
        key: str,
        value: str,
        ttl: int,
    ) -> None:
        self._client.setex(
            key,
            ttl,
            value,
        )

    def delete(
        self,
        key: str,
    ) -> None:
        self._client.delete(key)
