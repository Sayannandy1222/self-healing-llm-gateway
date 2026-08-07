from __future__ import annotations

from app.core.security.jwt import JWTManager


def test_create_token() -> None:
    manager = JWTManager()

    token = manager.create_token("user")

    assert token.startswith("user:")


def test_verify_token() -> None:
    manager = JWTManager()

    token = manager.create_token("user")

    assert manager.verify_token(token) is True


def test_invalid_token() -> None:
    manager = JWTManager()

    assert manager.verify_token("invalid") is False
