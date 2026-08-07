from __future__ import annotations

from app.application.provider_selection.history.provider_history import (
    ProviderHistory,
)


class ProviderHistoryRegistry:
    """
    Stores historical routing information for providers.
    """

    def __init__(self) -> None:
        self._history: dict[str, ProviderHistory] = {}

    def register(
        self,
        provider: str,
    ) -> None:
        self._history[provider] = ProviderHistory(
            provider=provider,
        )

    def get(
        self,
        provider: str,
    ) -> ProviderHistory:
        return self._history[provider]

    def record_success(
        self,
        provider: str,
    ) -> None:
        self.get(provider).record_success()

    def record_failure(
        self,
        provider: str,
    ) -> None:
        self.get(provider).record_failure()

    def record_retry(
        self,
        provider: str,
    ) -> None:
        self.get(provider).record_retry()

    def record_timeout(
        self,
        provider: str,
    ) -> None:
        self.get(provider).record_timeout()

    def providers(
        self,
    ) -> list[str]:
        return sorted(
            self._history.keys(),
        )
