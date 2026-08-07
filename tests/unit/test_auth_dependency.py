from __future__ import annotations

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.api.dependencies.auth import require_auth


def test_require_auth_accepts_valid_token() -> None:
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="user:abcdef123456",
    )

    token = require_auth(credentials)

    assert token == "user:abcdef123456"


def test_require_auth_rejects_invalid_token() -> None:
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="invalid-token",
    )

    try:
        require_auth(credentials)
        raise AssertionError("Expected HTTPException")
    except HTTPException as exc:
        assert exc.status_code == 401
