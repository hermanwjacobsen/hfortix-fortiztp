"""
FortiZTP Response Models

Provides structured response objects for FortiZTP Cloud API.
"""

from __future__ import annotations

from typing import Any, Iterator


class FortiZTPDevice:
    """
    Wrapper for individual device objects in FortiZTP responses.
    
    Provides attribute access to device fields.
    """
    
    def __init__(self, data: dict[str, Any]):
        """Initialize device wrapper."""
        self._data = data
    
    def __getattr__(self, name: str) -> Any:
        """Allow attribute access to device fields."""
        if name.startswith("_"):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        if name in self._data:
            return self._data[name]
        
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __getitem__(self, key: str) -> Any:
        """Dictionary-style access to device fields."""
        return self._data[key]
    
    def __repr__(self) -> str:
        """String representation."""
        return f"<FortiZTPDevice({self._data.get('deviceSN', 'unknown')})>"
    
    def to_dict(self) -> dict[str, Any]:
        """Get the original dictionary data."""
        return self._data


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
        >>> response = client.devices.list(provision_status="provisioned")
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
    def json(self) -> dict[str, Any]:
        """Raw API response as JSON/dictionary (alias for .raw)."""
        return self._data
    
    @property
    def data(self) -> Any:
        """
        Response data field.
        
        For list responses, returns the list of items.
        For single object responses, returns the object data.
        """
        return self._data.get('data', self._data)
    
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
    
    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over response data.
        
        If response contains a 'data' field that is a list, iterates over the list items,
        wrapping each dict in FortiZTPDevice for attribute access.
        Otherwise, iterates over response field names.
        
        This allows:
            devices = client.devices.get()
            for device in devices:  # Iterates over device objects
                print(device.deviceSN)  # Attribute access
        """
        # Check if 'data' field exists and is a list
        if 'data' in self._data and isinstance(self._data['data'], list):
            # Wrap each dict in FortiZTPDevice for attribute access
            for item in self._data['data']:
                if isinstance(item, dict):
                    yield FortiZTPDevice(item)
                else:
                    yield item
        else:
            # Otherwise iterate over field names (dict keys)
            yield from iter(self._data)
    
    def __len__(self) -> int:
        """
        Number of items in response.
        
        If response contains a 'data' field that is a list, returns length of that list.
        Otherwise, returns number of fields in response.
        """
        if 'data' in self._data and isinstance(self._data['data'], list):
            return len(self._data['data'])
        return len(self._data)
    
    def __repr__(self) -> str:
        """String representation of response."""
        status = f"status={self._http_status_code}" if self._http_status_code else ""
        time = f"time={self._response_time:.3f}s" if self._response_time else ""
        parts = [p for p in [status, time] if p]
        metadata = f"({', '.join(parts)})" if parts else ""
        return f"<{type(self).__name__}{metadata}>"


__all__ = ["FortiZTPResponse", "FortiZTPDevice"]
