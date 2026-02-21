"""
FortiZTP API - Regions

Wrapper for regions-specific endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .firmwareprofiles import Firmwareprofiles

__all__ = ["Regions"]


class Regions:
    """Regions endpoints wrapper."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Regions endpoints.

        Args:
            client: HTTP client instance for API communication
        """
        self.firmwareprofiles = Firmwareprofiles(client)
