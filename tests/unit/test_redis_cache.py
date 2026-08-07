from __future__ import annotations

from unittest.mock import Mock

from app.infrastructure.cache.redis_cache import RedisCache


def test_set_calls_redis() -> None:
    client = Mock()

    cache = RedisCache(client)

    cache.set(
        key="hello",
        value="world",
        ttl=300,
    )

    client.setex.assert_called_once_with(
        "hello",
        300,
        "world",
    )


def test_get_returns_value() -> None:
    client = Mock()

    client.get.return_value = b"cached"

    cache = RedisCache(client)

    assert cache.get("hello") == "cached"


def test_get_returns_none() -> None:
    client = Mock()

    client.get.return_value = None

    cache = RedisCache(client)

    assert cache.get("hello") is None


def test_delete_calls_redis() -> None:
    client = Mock()

    cache = RedisCache(client)

    cache.delete("hello")

    client.delete.assert_called_once_with("hello")
