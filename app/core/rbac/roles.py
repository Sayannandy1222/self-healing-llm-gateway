from __future__ import annotations

from enum import StrEnum


class Role(StrEnum):
    """
    Supported application roles.
    """

    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"
