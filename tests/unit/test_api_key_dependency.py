from __future__ import annotations

from fastapi import HTTPException

from app.api.dependencies.api_key import (
    api_key_manager,
    require_api_key,
)


def test_valid_api_key() -> None:
    api_key_manager.register("valid-key")

    assert require_api_key("valid-key") == "valid-key"


def test_invalid_api_key() -> None:
    try:
        require_api_key("invalid")
        raise AssertionError("Expected HTTPException")
    except HTTPException as exc:
        assert exc.status_code == 401
