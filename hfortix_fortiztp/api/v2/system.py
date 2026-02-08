"""
FortiZTP System API.

Auto-generated from schema - contains 1 endpoints.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from hfortix_core.http.cloud_client import CloudHTTPClient

from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import (
    DeviceType,
    ProvisionStatus,
    ProvisionTarget,
)


class SystemAPI:
    """System API endpoints."""

    def __init__(self, client: "CloudHTTPClient") -> None:
        """Initialize System API."""
        self._client = client

    def get(
        self,
    ) -> FortiZTPResponse:
        """
        Get system status.

        Get system status

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.system.get(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/system"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


__all__ = ["SystemAPI"]
