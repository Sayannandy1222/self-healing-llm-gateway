from __future__ import annotations

from app.core.rbac.permissions import Permission
from app.core.rbac.rbac_service import RBACService
from app.core.rbac.roles import Role


def test_admin_has_everything() -> None:
    service = RBACService()

    assert service.has_permission(
        Role.ADMIN,
        Permission.ADMIN,
    )


def test_viewer_cannot_access_admin() -> None:
    service = RBACService()

    assert (
        service.has_permission(
            Role.VIEWER,
            Permission.ADMIN,
        )
        is False
    )


def test_developer_can_stream() -> None:
    service = RBACService()

    assert service.has_permission(
        Role.DEVELOPER,
        Permission.STREAM,
    )
