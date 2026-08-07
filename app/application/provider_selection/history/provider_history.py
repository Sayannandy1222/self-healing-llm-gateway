from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ProviderHistory:
    """
    Tracks historical provider performance.
    """

    provider: str

    successful_requests: int = 0

    failed_requests: int = 0

    timeout_requests: int = 0

    retry_requests: int = 0

    def record_success(self) -> None:
        self.successful_requests += 1

    def record_failure(self) -> None:
        self.failed_requests += 1

    def record_timeout(self) -> None:
        self.timeout_requests += 1

    def record_retry(self) -> None:
        self.retry_requests += 1

    @property
    def total_requests(self) -> int:
        return self.successful_requests + self.failed_requests

    @property
    def success_rate(self) -> float:
        if self.total_requests == 0:
            return 100.0

        return (self.successful_requests / self.total_requests) * 100.0

    @property
    def failure_rate(self) -> float:
        return 100.0 - self.success_rate
