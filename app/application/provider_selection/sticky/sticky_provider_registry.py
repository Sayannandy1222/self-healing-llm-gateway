from __future__ import annotations


class StickyProviderRegistry:
    """
    Maintains provider affinity for conversations/sessions.

    Once a provider is assigned to a session, subsequent
    requests can reuse the same provider until explicitly
    cleared or reassigned.
    """

    def __init__(self) -> None:
        self._assignments: dict[str, str] = {}

    def assign(
        self,
        session_id: str,
        provider: str,
    ) -> None:
        """
        Assign a provider to a session.
        """
        self._assignments[session_id] = provider

    def get(
        self,
        session_id: str,
    ) -> str | None:
        """
        Return the assigned provider for a session.
        """
        return self._assignments.get(session_id)

    def contains(
        self,
        session_id: str,
    ) -> bool:
        """
        Check whether a session has an assigned provider.
        """
        return session_id in self._assignments

    def remove(
        self,
        session_id: str,
    ) -> None:
        """
        Remove a session assignment.
        """
        self._assignments.pop(
            session_id,
            None,
        )

    def clear(self) -> None:
        """
        Remove all sticky assignments.
        """
        self._assignments.clear()

    def sessions(self) -> list[str]:
        """
        Return all tracked session IDs.
        """
        return sorted(
            self._assignments.keys(),
        )
