from __future__ import annotations

from app.middleware.audit import audit_logger, record_audit


def test_record_audit() -> None:
    before = audit_logger.count()

    record_audit(
        user="alice",
        endpoint="/chat",
        method="POST",
        status_code=200,
        request_id="abc",
    )

    assert audit_logger.count() == before + 1
