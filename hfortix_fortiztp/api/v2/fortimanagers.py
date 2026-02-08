"""
FortiZTP Fortimanagers API.

Auto-generated from schema - contains 5 endpoints.
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


class FortiManagersAPI:
    """Fortimanagers API endpoints."""

    def __init__(self, client: "CloudHTTPClient") -> None:
        """Initialize Fortimanagers API."""
        self._client = client

    def fortimanagers_get(
        self,
        oid: int,
    ) -> FortiZTPResponse:
        """
        Get specific FortiManager data.

        Get specific FortiManager data

        Args:
            oid: FortiManager oid (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.fortimanagers.fortimanagers_get(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/setting/fortimanagers/{oid}"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def fortimanagers_put(
        self,
        oid: int,
        sn: str,
        ip: str,
        script_oid: Optional[int] = None,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Update specific FortiManager data.

        Update specific FortiManager data

        Args:
            oid: FortiManager oid (required)
            sn: FortiManager serial number. To support HA, enter multiple items comma-separated. Dual SN with single IP/Hostname allowed for FMG 7.2 HA (required)
            ip: FortiManager IP/Hostname. To support HA, enter multiple items comma-separated. Dual SN with single IP/Hostname allowed for FMG 7.2 HA (required)
            script_oid: Pre-run CLI Script oid (optional)
            update_time: Update time in milliseconds since Jan. 01 1970. (UTC) (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.fortimanagers.fortimanagers_put(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/setting/fortimanagers/{oid}"

        # Build request body
        data = {}
        if oid is not None:
            data['oid'] = oid
        data['sn'] = sn
        data['ip'] = ip
        if script_oid is not None:
            data['scriptOid'] = script_oid
        if update_time is not None:
            data['updateTime'] = update_time

        # Make HTTP request
        response = self._client.put(path, data=data)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def fortimanagers_delete(
        self,
        oid: int,
    ) -> FortiZTPResponse:
        """
        Delete FortiManager data.

        Delete FortiManager data

        Args:
            oid: FortiManager oid (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.fortimanagers.fortimanagers_delete(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/setting/fortimanagers/{oid}"

        # Make HTTP request
        response = self._client.delete(path)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def fortimanagers_list(
        self,
    ) -> FortiZTPResponse:
        """
        Get FortiManager data.

        Get all existed FortiManager data

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.fortimanagers.fortimanagers_list(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/setting/fortimanagers"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def fortimanagers_post(
        self,
        sn: str,
        ip: str,
        oid: Optional[int] = None,
        script_oid: Optional[int] = None,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Add FortiManager data.

        Add FortiManager data

        Args:
            oid: Unique identifier for FortiManager setting data (optional)
            sn: FortiManager serial number. To support HA, enter multiple items comma-separated. Dual SN with single IP/Hostname allowed for FMG 7.2 HA (required)
            ip: FortiManager IP/Hostname. To support HA, enter multiple items comma-separated. Dual SN with single IP/Hostname allowed for FMG 7.2 HA (required)
            script_oid: Pre-run CLI Script oid (optional)
            update_time: Update time in milliseconds since Jan. 01 1970. (UTC) (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.fortimanagers.fortimanagers_post(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/setting/fortimanagers"

        # Build request body
        data = {}
        if oid is not None:
            data['oid'] = oid
        data['sn'] = sn
        data['ip'] = ip
        if script_oid is not None:
            data['scriptOid'] = script_oid
        if update_time is not None:
            data['updateTime'] = update_time

        # Make HTTP request
        response = self._client.post(path, data=data)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


__all__ = ["FortiManagersAPI"]
