from __future__ import annotations

from app.core.audit.audit_event import AuditEvent
from app.core.audit.audit_logger import AuditLogger


def test_log_event() -> None:
    logger = AuditLogger()

    event = AuditEvent.create(
        user="alice",
        endpoint="/chat",
        method="POST",
        status_code=200,
        request_id="123",
    )

    logger.log(event)

    assert logger.count() == 1

    assert logger.events()[0] is event
