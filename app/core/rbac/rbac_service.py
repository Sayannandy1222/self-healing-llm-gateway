from __future__ import annotations

from app.core.rbac.permissions import Permission
from app.core.rbac.roles import Role


class RBACService:
    """
    Role Based Access Control service.
    """

    _permissions: dict[Role, set[Permission]] = {
        Role.ADMIN: {
            Permission.CHAT,
            Permission.STREAM,
            Permission.METRICS,
            Permission.PROVIDERS,
            Permission.ADMIN,
        },
        Role.DEVELOPER: {
            Permission.CHAT,
            Permission.STREAM,
            Permission.METRICS,
            Permission.PROVIDERS,
        },
        Role.VIEWER: {
            Permission.CHAT,
        },
    }

    def has_permission(
        self,
        role: Role,
        permission: Permission,
    ) -> bool:
        """
        Check whether a role has a permission.
        """

        return permission in self._permissions.get(
            role,
            set(),
        )
