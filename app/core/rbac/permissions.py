from __future__ import annotations

from enum import StrEnum


class Permission(StrEnum):
    """
    Supported permissions.
    """

    CHAT = "chat"
    STREAM = "stream"
    METRICS = "metrics"
    PROVIDERS = "providers"
    ADMIN = "admin"
