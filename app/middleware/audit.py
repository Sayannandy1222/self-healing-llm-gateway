from __future__ import annotations

from app.core.audit.audit_event import AuditEvent
from app.core.audit.audit_logger import AuditLogger

audit_logger = AuditLogger()


def record_audit(
    *,
    user: str,
    endpoint: str,
    method: str,
    status_code: int,
    request_id: str,
) -> None:
    """
    Record an audit event.
    """

    audit_logger.log(
        AuditEvent.create(
            user=user,
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            request_id=request_id,
        ),
    )
