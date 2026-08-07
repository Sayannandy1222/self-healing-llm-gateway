from __future__ import annotations

from app.core.audit.audit_event import AuditEvent


class AuditLogger:
    """
    In-memory audit logger.

    Can later be replaced with Kafka,
    Elasticsearch,
    CloudWatch,
    Splunk,
    etc.
    """

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def log(
        self,
        event: AuditEvent,
    ) -> None:
        self._events.append(event)

    def events(self) -> list[AuditEvent]:
        return list(self._events)

    def count(self) -> int:
        return len(self._events)
