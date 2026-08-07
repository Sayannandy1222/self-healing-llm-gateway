from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class CORSConfig:
    """
    Production CORS configuration.
    """

    allow_origins: list[str] = field(
        default_factory=lambda: ["*"],
    )

    allow_methods: list[str] = field(
        default_factory=lambda: ["*"],
    )

    allow_headers: list[str] = field(
        default_factory=lambda: ["*"],
    )

    allow_credentials: bool = True

    def is_origin_allowed(
        self,
        origin: str,
    ) -> bool:
        """
        Check whether an origin is allowed.
        """

        return "*" in self.allow_origins or origin in self.allow_origins
