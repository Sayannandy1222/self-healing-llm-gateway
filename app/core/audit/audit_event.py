from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(slots=True)
class AuditEvent:
    """
    Immutable audit event.
    """

    timestamp: datetime

    user: str

    endpoint: str

    method: str

    status_code: int

    request_id: str

    provider: str | None = None

    latency_ms: float | None = None

    client_ip: str | None = None

    @classmethod
    def create(
        cls,
        *,
        user: str,
        endpoint: str,
        method: str,
        status_code: int,
        request_id: str,
        provider: str | None = None,
        latency_ms: float | None = None,
        client_ip: str | None = None,
    ) -> AuditEvent:
        return cls(
            timestamp=datetime.now(UTC),
            user=user,
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            request_id=request_id,
            provider=provider,
            latency_ms=latency_ms,
            client_ip=client_ip,
        )
