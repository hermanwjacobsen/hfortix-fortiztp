"""
FortiZTP API - Firmwareprofiles

Endpoint for firmwareprofiles resources.

API Endpoints:
    GET /v2/devices/{deviceSN}/regions/{region}/firmwareprofiles

Example Usage:
    >>> from hfortix_fortiztp import FortiZTP
    >>> client = FortiZTP(api_key="your-api-key")
    >>>
    >>> response = client.devices.regions.firmwareprofiles.get(...)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from hfortix_fortiztp.models import FortiZTPResponse


class Firmwareprofiles:
    """Firmwareprofiles Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Firmwareprofiles endpoint."""
        self._client = client

    def get(
        self,
        device_sn: str,
        region: str,
    ) -> FortiZTPResponse:
        """
        Get firmware profiles for specific device.

        Retrieve firmware profiles for specific device.

        Args:
            device_sn: Device serial number (required)
            region: Region identifier (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.firmware_profiles(...)
            >>> print(response.http_status_code)
        """
        path = f"/v2/devices/{device_sn}/regions/{region}/firmwareprofiles"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )

