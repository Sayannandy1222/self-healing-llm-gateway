from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ProviderHealth:
    """
    Runtime health information for a provider.
    """

    provider: str

    healthy: bool = True

    failure_count: int = 0

    latency_ms: float = 0.0

    last_checked: datetime | None = None
