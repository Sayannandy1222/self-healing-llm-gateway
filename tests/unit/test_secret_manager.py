from __future__ import annotations

import os

import pytest

from app.core.secrets.secret_manager import SecretManager


def test_get_secret() -> None:
    os.environ["TEST_SECRET"] = "secret"

    manager = SecretManager()

    assert manager.get("TEST_SECRET") == "secret"


def test_exists() -> None:
    os.environ["ANOTHER_SECRET"] = "value"

    manager = SecretManager()

    assert manager.exists("ANOTHER_SECRET")


def test_require_secret() -> None:
    os.environ["REQUIRED_SECRET"] = "value"

    manager = SecretManager()

    assert manager.require("REQUIRED_SECRET") == "value"


def test_missing_secret() -> None:
    manager = SecretManager()

    with pytest.raises(RuntimeError):
        manager.require("DOES_NOT_EXIST")
