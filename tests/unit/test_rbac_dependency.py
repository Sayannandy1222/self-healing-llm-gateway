from __future__ import annotations

import pytest
from fastapi import HTTPException

from app.api.dependencies.rbac import require_permission
from app.core.rbac.permissions import Permission
from app.core.rbac.roles import Role


def test_permission_allowed() -> None:
    require_permission(
        Role.ADMIN,
        Permission.ADMIN,
    )


def test_permission_denied() -> None:
    with pytest.raises(HTTPException):
        require_permission(
            Role.VIEWER,
            Permission.ADMIN,
        )
