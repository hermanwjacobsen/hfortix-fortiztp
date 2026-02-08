"""
FortiZTP Response Models

Provides structured response objects for FortiZTP Cloud API.
"""

from __future__ import annotations

from typing import Any, Iterator


class FortiZTPResponse:
    """
    Structured wrapper for FortiZTP API responses.
    
    Provides clean attribute access to API response data with metadata.
    
    Features:
    - Attribute access to response fields: response.total, response.data
    - HTTP metadata: response.http_status_code, response.response_time
    - Raw data access: response.raw, response.dict()
    - Iteration support for list responses
    
    Examples:
        >>> response = client.v2.devices.list.get(provision_status="provisioned")
        >>>
        >>> # Attribute access
        >>> response.total  # Total number of devices
        >>> response.data  # Array of device data
        >>> response.hasCache  # Cache status
        >>>
        >>> # HTTP metadata
        >>> response.http_status_code  # 200, 404, etc.
        >>> response.response_time  # Request duration in seconds
        >>>
        >>> # Raw access
        >>> response.raw  # Full API response dict
        >>> response.dict()  # Convert to dict
        >>>
        >>> # Iteration (for list responses)
        >>> for device in response.data:
        ...     print(device['deviceSN'])
    
    Args:
        data: Dictionary from FortiZTP API response
        http_status_code: HTTP status code (200, 404, 500, etc.)
        response_time: Response time in seconds
        request_info: HTTP request information
    """
    
    def __init__(
        self,
        data: dict[str, Any],
        http_status_code: int | None = None,
        response_time: float | None = None,
        request_info: dict[str, Any] | None = None,
    ):
        """
        Initialize FortiZTP response object.
        
        Args:
            data: Dictionary containing the API response fields
            http_status_code: HTTP status code from response
            response_time: Response time in seconds
            request_info: Request metadata (method, url, params, data)
        """
        self._data = data
        self._http_status_code = http_status_code
        self._response_time = response_time
        self._request_info = request_info
    
    # ========================================================================
    # Metadata Properties
    # ========================================================================
    
    @property
    def http_status_code(self) -> int | None:
        """HTTP status code (200, 404, 500, etc.)."""
        return self._http_status_code
    
    @property
    def response_time(self) -> float | None:
        """Response time in seconds."""
        return self._response_time
    
    @property
    def raw(self) -> dict[str, Any]:
        """Raw API response dictionary."""
        return self._data
    
    @property
    def request_info(self) -> dict[str, Any] | None:
        """HTTP request information (method, url, params, data)."""
        return self._request_info
    
    # ========================================================================
    # HTTP Request Metadata (convenience accessors for request_info)
    # ========================================================================
    
    @property
    def request_method(self) -> str | None:
        """HTTP request method (GET, POST, PUT, DELETE)."""
        if self._request_info:
            return self._request_info.get("method")
        return None
    
    @property
    def request_url(self) -> str | None:
        """Full request URL."""
        if self._request_info:
            return self._request_info.get("url")
        return None
    
    @property
    def request_params(self) -> dict[str, Any] | None:
        """Query parameters sent with request."""
        if self._request_info:
            return self._request_info.get("params")
        return None
    
    @property
    def request_data(self) -> dict[str, Any] | None:
        """Request body data."""
        if self._request_info:
            return self._request_info.get("data")
        return None
    
    # ========================================================================
    # Data Access Methods
    # ========================================================================
    
    def dict(self) -> dict[str, Any]:
        """
        Convert response to dictionary.
        
        Returns:
            Copy of response data as dictionary
        """
        return self._data.copy()
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get value from response data with optional default.
        
        Args:
            key: Field name to retrieve
            default: Default value if field not found
            
        Returns:
            Field value or default
        """
        return self._data.get(key, default)
    
    def __getattr__(self, name: str) -> Any:
        """
        Allow attribute access to response fields.
        
        Args:
            name: Attribute name
            
        Returns:
            Value from response data
            
        Raises:
            AttributeError: If attribute not found in response data
        """
        if name.startswith("_"):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        if name in self._data:
            return self._data[name]
        
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __getitem__(self, key: str) -> Any:
        """
        Dictionary-style access to response fields.
        
        Args:
            key: Field name
            
        Returns:
            Field value
        """
        return self._data[key]
    
    def __contains__(self, key: str) -> bool:
        """Check if field exists in response data."""
        return key in self._data
    
    def __iter__(self) -> Iterator[str]:
        """Iterate over response field names."""
        return iter(self._data)
    
    def __len__(self) -> int:
        """Number of fields in response."""
        return len(self._data)
    
    def __repr__(self) -> str:
        """String representation of response."""
        status = f"status={self._http_status_code}" if self._http_status_code else ""
        time = f"time={self._response_time:.3f}s" if self._response_time else ""
        parts = [p for p in [status, time] if p]
        metadata = f"({', '.join(parts)})" if parts else ""
        return f"<{type(self).__name__}{metadata}>"


__all__ = ["FortiZTPResponse"]
