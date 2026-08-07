from __future__ import annotations

from abc import ABC, abstractmethod


class Cache(ABC):
    """
    Abstract cache interface.
    """

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> str | None:
        """
        Return cached value or None.
        """
        raise NotImplementedError

    @abstractmethod
    def set(
        self,
        key: str,
        value: str,
        ttl: int,
    ) -> None:
        """
        Store a value with a TTL (seconds).
        """
        raise NotImplementedError
