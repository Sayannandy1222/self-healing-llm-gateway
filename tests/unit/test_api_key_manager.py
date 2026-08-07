from __future__ import annotations

from app.core.api_keys.api_key_manager import APIKeyManager


def test_generate_key() -> None:
    manager = APIKeyManager()

    key = manager.generate()

    assert manager.validate(key)


def test_register_key() -> None:
    manager = APIKeyManager()

    manager.register("abc")

    assert manager.validate("abc")


def test_revoke_key() -> None:
    manager = APIKeyManager()

    manager.register("abc")

    manager.revoke("abc")

    assert manager.validate("abc") is False
