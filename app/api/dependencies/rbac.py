from __future__ import annotations

from fastapi import HTTPException, status

from app.core.rbac.permissions import Permission
from app.core.rbac.rbac_service import RBACService
from app.core.rbac.roles import Role

_service = RBACService()


def require_permission(
    role: Role,
    permission: Permission,
) -> None:
    """
    Require a permission.
    """

    if not _service.has_permission(
        role,
        permission,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied.",
        )
