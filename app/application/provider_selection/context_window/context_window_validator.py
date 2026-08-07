from __future__ import annotations


class ContextWindowValidator:
    """
    Validates whether a provider can satisfy
    the requested context window.
    """

    @staticmethod
    def supports(
        provider_context_window: int,
        required_context_window: int,
    ) -> bool:
        """
        Return True if the provider supports the
        requested context size.
        """

        return provider_context_window >= required_context_window
