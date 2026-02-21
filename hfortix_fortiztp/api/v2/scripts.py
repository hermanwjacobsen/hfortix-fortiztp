"""
FortiZTP Scripts API.

Auto-generated from schema - contains 7 endpoints.
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


class ScriptsAPI:
    """Scripts API endpoints."""

    def __init__(self, client: "CloudHTTPClient") -> None:
        """Initialize Scripts API."""
        self._client = client

    def scripts_get(
        self,
        oid: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Get specific script meta data.

        Get specific script meta data.

        Args:
            oid: Script object ID (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_get(...)
            >>> print(response.http_status_code)
        """
        # Build path - either specific resource or collection
        if oid:
            path = f"/v2/setting/scripts/{oid}"
        else:
            path = "/v2/setting/scripts"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_put(
        self,
        oid: int,
        name: str,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Update specific script meta data.

        Update specific script meta data.

        Args:
            oid: Script object ID (required)
            name: Script name (required)
            update_time: Update time in milliseconds since Jan. 01 1970. (UTC) (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_put(...)
            >>> print(response.http_status_code)
        """
        path = f"/v2/setting/scripts/{oid}"

        # Build request body
        data = {}
        data['oid'] = oid
        data['name'] = name
        if update_time is not None:
            data['updateTime'] = update_time

        # Make HTTP request
        response = self._client.put(path, data=data)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_delete(
        self,
        oid: int,
    ) -> FortiZTPResponse:
        """
        Delete script.

        Delete script

        Args:
            oid: Script object ID (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_delete(...)
            >>> print(response.http_status_code)
        """
        path = f"/v2/setting/scripts/{oid}"

        # Make HTTP request
        response = self._client.delete(path)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_list(
        self,
    ) -> FortiZTPResponse:
        """
        Get scripts meta data.

        Get all existed scripts meta.

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_list(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/setting/scripts"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_post(
        self,
        oid: int,
        name: str,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Add script meta data.

        Add script meta data

        Args:
            oid: Unique identifier for script (required)
            name: Script name (required)
            update_time: Update time in milliseconds since Jan. 01 1970. (UTC) (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_post(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/setting/scripts"

        # Build request body
        data = {}
        data['oid'] = oid
        data['name'] = name
        if update_time is not None:
            data['updateTime'] = update_time

        # Make HTTP request
        response = self._client.post(path, data=data)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_get_content(
        self,
        oid: Optional[int] = None,
    ) -> FortiZTPResponse:
        """
        Get script content.

        Get specific script content.

        Args:
            oid: Script object ID (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_get_content(...)
            >>> print(response.http_status_code)
        """
        # Build path - either specific resource or collection
        if oid:
            path = f"/v2/setting/scripts/{oid}/content"
        else:
            path = "/v2/setting/scripts/content"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )


    def scripts_put_content(
        self,
        oid: int,
    ) -> FortiZTPResponse:
        """
        Update specific script content.

        Update specific script content.

        Args:
            oid: Script object ID (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.scripts.scripts_put_content(...)
            >>> print(response.http_status_code)
        """
        path = f"/v2/setting/scripts/{oid}/content"

        # Build request body
        data = None

        # Make HTTP request
        response = self._client.put(path, data=data)

        # Wrap in FortiZTPResponse - unpack the response envelope
        return FortiZTPResponse(
            data=response["data"],
            http_status_code=response.get("http_status_code"),
            response_time=response.get("response_time"),
            request_info=response.get("request_info")
        )

