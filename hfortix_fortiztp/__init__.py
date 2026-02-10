"""
FortiZTP Cloud API SDK for Python.

Provides a fully-typed Python interface to the FortiZTP Cloud API v2.0.
Supports device provisioning, script management, FortiManager integration,
and system status monitoring.

Basic Usage:
    >>> from hfortix_fortiztp import FortiZTP
    >>> 
    >>> # Initialize client with OAuth credentials
    >>> client = FortiZTP(
    ...     client_id="your_client_id",
    ...     client_secret="your_client_secret"
    ... )
    >>> 
    >>> # List all devices
    >>> response = client.devices.list_devices(limit=10)
    >>> for device in response["data"]:
    ...     print(f"{device['deviceSN']}: {device['provisionStatus']}")
    >>> 
    >>> # Get device by serial number
    >>> device = client.devices.get_device(serial_number="FG123456789")
    >>> print(f"Status: {device['provisionStatus']}")
    >>> 
    >>> # Provision device to FortiManager
    >>> result = client.devices.provision_device(
    ...     serial_number="FG123456789",
    ...     provision_target="FortiManager",
    ...     fortimanager_oid=12345
    ... )

Features:
    - Full OAuth 2.0 authentication support
    - Complete device lifecycle management (list, get, create, update, delete)
    - Script management for pre-run CLI scripts
    - FortiManager integration
    - System status monitoring
    - Comprehensive type hints for IDE autocomplete
    - Request/response metadata tracking
    - Rate limiting (2,000 calls/hour)

API Coverage:
    Devices (10 endpoints):
        - List devices (paginated)
        - Get device by serial number
        - Create/update device provisioning
        - Delete device
        - Provision/unprovision devices
        - Bulk operations
    
    Scripts (3 endpoints):
        - List scripts
        - Get/create/update/delete scripts
    
    FortiManagers (3 endpoints):
        - List FortiManagers
        - Get/create/update/delete FortiManager settings
    
    System (2 endpoints):
        - Get system status
        - Health check
"""

from typing import TYPE_CHECKING, Any, Optional

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_core.http.oauth import FortiCloudAuth
from hfortix_core.session import CloudSession
from hfortix_core.ratelimit import RateLimitStats

# Response models
from .models import FortiZTPResponse

# Type definitions
from .types import (
    DeviceType,
    DeviceV2Data,
    ErrorData,
    FortiManagerMetaData,
    PageDtoDeviceData,
    PageDtoFortiManagerMetaData,
    PageDtoScriptMetaData,
    ProvisionStatus,
    ProvisionSubStatus,
    ProvisionTarget,
    ScriptMetaData,
    ServiceStatus,
    SystemData,
)

if TYPE_CHECKING:
    from .api.v2 import V2API
    from .api.v2.devices import DevicesAPI
    from .api.v2.scripts import ScriptsAPI
    from .api.v2.fortimanagers import FortiManagersAPI
    from .api.v2.system import SystemAPI


__version__ = "0.5.161"


class FortiZTP:
    """
    FortiZTP Cloud API client.
    
    Main entry point for interacting with the FortiZTP Cloud API v2.0.
    Handles OAuth 2.0 authentication and provides access to all API endpoints.
    
    Authentication:
        Automatically obtains OAuth token using API credentials, accepts
        pre-obtained token, or uses shared CloudSession.
    
    Rate Limits:
        - 2,000 calls per hour
    
    Args:
        api_id: FortiCloud API ID (for auto-login)
        password: FortiCloud password (for auto-login)
        client_id: Client ID for OAuth authentication (default: fortiztp)
        oauth_token: Pre-obtained OAuth token (alternative to api_id/password)
        session: CloudSession for multi-service token management (recommended)
        base_url: API base URL (default: https://fortiztp.forticloud.com/public/api)
        auth_url: OAuth token endpoint (optional - uses FortiCloud default)
        verify: Enable SSL certificate verification (default: True)
        max_retries: Maximum number of retry attempts (default: 3)
        connect_timeout: Connection timeout in seconds (default: 10.0)
        read_timeout: Read timeout in seconds (default: 300.0)
        read_only: Enable read-only mode - simulate write operations (default: False)
        track_operations: Enable operation tracking for audit logging (default: False)
        audit_handler: Handler for audit logging (implements AuditHandler protocol)
        audit_callback: Custom callback function for audit logging
        user_context: Optional dict with user/application context for audit logs
        
    Attributes:
        api: V2 API endpoints (devices, scripts, fortimanagers, system)
        devices: Direct access to devices API
        scripts: Direct access to scripts API
        fortimanagers: Direct access to fortimanagers API
        system: Direct access to system API
    
    Example:
        >>> # Auto-login with credentials
        >>> client = FortiZTP(
        ...     api_id="your_api_id",
        ...     password="your_password"
        ... )
        >>> 
        >>> # Or with CloudSession (recommended for multi-service)
        >>> with CloudSession(api_id="...", password="...") as session:
        ...     fcc = FortiCare(session=session)  # Uses "assetmanagement"
        ...     fztp = FortiZTP(session=session)  # Uses "fortiztp"
        ...     # Both share same session, different tokens
        >>> 
        >>> # Or with pre-obtained token
        >>> client = FortiZTP(oauth_token="your_token")
        >>> 
        >>> # Check system status
        >>> status = client.system.get()
        >>> 
        >>> # List all devices
        >>> devices = client.devices.get()
        >>> 
        >>> # Clean up
        >>> client.logout()
    
    Raises:
        ValueError: If no authentication method provided
    """
    
    # Default OAuth client_id for FortiZTP
    DEFAULT_CLIENT_ID = "fortiztp"
    
    # Type hints for IDE autocomplete
    api: "V2API"
    devices: "DevicesAPI"
    scripts: "ScriptsAPI"
    fortimanagers: "FortiManagersAPI"
    system: "SystemAPI"

    
    def __init__(
        self,
        api_id: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        oauth_token: Optional[str] = None,
        session: Optional[CloudSession] = None,
        base_url: str = "https://fortiztp.forticloud.com/public/api",
        auth_url: Optional[str] = None,
        verify: bool = True,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        read_only: bool = False,
        track_operations: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
        # OLD Rate limiting configuration (set to None by default - configure as needed)
        rate_limit_calls_per_min: Optional[int] = None,
        rate_limit_calls_per_5min: Optional[int] = None,
        rate_limit_calls_per_hour: Optional[int] = None,
        rate_limit_errors_per_min: Optional[int] = None,
        rate_limit_errors_per_5min: Optional[int] = None,
        rate_limit_errors_per_hour: Optional[int] = None,
        # NEW: Rate limiting enforcement parameters
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        circuit_breaker_half_open_calls: int = 3,
    ) -> None:
        """Initialize FortiZTP client with OAuth credentials."""
        # Determine client_id (use provided, or session-specific, or default)
        self._client_id = client_id if client_id is not None else self.DEFAULT_CLIENT_ID
        self._session = session
        
        # If using session and rate limiting params not provided, use session defaults
        if session:
            # Use session's rate limiting settings as defaults (can be overridden by explicit params)
            if rate_limit is False and session._rate_limit:
                rate_limit = session._rate_limit
            if rate_limit_strategy == "queue" and session._rate_limit_strategy != "queue":
                rate_limit_strategy = session._rate_limit_strategy
            if rate_limit_max_requests == 100 and session._rate_limit_max_requests != 100:
                rate_limit_max_requests = session._rate_limit_max_requests
            if rate_limit_window_seconds == 60.0 and session._rate_limit_window_seconds != 60.0:
                rate_limit_window_seconds = session._rate_limit_window_seconds
            if rate_limit_queue_size == 100 and session._rate_limit_queue_size != 100:
                rate_limit_queue_size = session._rate_limit_queue_size
            if rate_limit_queue_timeout == 30.0 and session._rate_limit_queue_timeout != 30.0:
                rate_limit_queue_timeout = session._rate_limit_queue_timeout
            if rate_limit_queue_overflow == "block" and session._rate_limit_queue_overflow != "block":
                rate_limit_queue_overflow = session._rate_limit_queue_overflow
            if circuit_breaker is False and session._circuit_breaker:
                circuit_breaker = session._circuit_breaker
            if circuit_breaker_threshold == 5 and session._circuit_breaker_threshold != 5:
                circuit_breaker_threshold = session._circuit_breaker_threshold
            if circuit_breaker_timeout == 60.0 and session._circuit_breaker_timeout != 60.0:
                circuit_breaker_timeout = session._circuit_breaker_timeout
            if circuit_breaker_half_open_calls == 3 and session._circuit_breaker_half_open_calls != 3:
                circuit_breaker_half_open_calls = session._circuit_breaker_half_open_calls
        
        # Obtain OAuth token based on auth method
        self._auth: Optional[FortiCloudAuth] = None
        
        if session:
            # CloudSession mode - get token from session
            oauth_token = session.get_token(self._client_id)
            
            # Create token callback for auto-refresh before each request
            # Only if check_before_request is enabled (default: True)
            if session._check_before_request:
                def get_fresh_token() -> str:
                    return session.ensure_token_valid(self._client_id)
                
                token_callback = get_fresh_token
            else:
                token_callback = None
        elif not oauth_token:
            # Direct auth mode - create auth client
            if not api_id or not password:
                raise ValueError(
                    "Either session, oauth_token, or (api_id and password) must be provided"
                )
            
            # Auto-login to get token
            self._auth = FortiCloudAuth(
                api_id=api_id,
                password=password,
                client_id=self._client_id,
                auth_url=auth_url,
            )
            oauth_token = self._auth.get_token()
            token_callback = None
        else:
            # Pre-obtained token mode
            token_callback = None
        
        # Initialize HTTP client with OAuth authentication
        self._client = CloudHTTPClient(
            url=base_url,
            oauth_token=oauth_token,
            verify=verify,
            max_retries=max_retries,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            read_only=read_only,
            track_operations=track_operations,
            audit_handler=audit_handler,
            audit_callback=audit_callback,
            user_context=user_context,
            token_callback=token_callback,
            # NEW: Pass rate limiting parameters
            rate_limit=rate_limit,
            rate_limit_strategy=rate_limit_strategy,
            rate_limit_max_requests=rate_limit_max_requests,
            rate_limit_window_seconds=rate_limit_window_seconds,
            rate_limit_queue_size=rate_limit_queue_size,
            rate_limit_queue_timeout=rate_limit_queue_timeout,
            rate_limit_queue_overflow=rate_limit_queue_overflow,
            circuit_breaker=circuit_breaker,
            circuit_breaker_threshold=circuit_breaker_threshold,
            circuit_breaker_timeout=circuit_breaker_timeout,
            circuit_breaker_half_open_calls=circuit_breaker_half_open_calls,
        )
        
        # Rate limit tracking for this client instance
        # Set limits as needed: FortiZTP documented limit is 2000 calls/hour
        self._rate_stats = RateLimitStats(
            calls_per_min=rate_limit_calls_per_min,
            calls_per_5min=rate_limit_calls_per_5min,
            calls_per_hour=rate_limit_calls_per_hour,
            errors_per_min=rate_limit_errors_per_min,
            errors_per_5min=rate_limit_errors_per_5min,
            errors_per_hour=rate_limit_errors_per_hour,
        )
        
        # Initialize API endpoints
        from .api.v2 import V2API
        self.api = V2API(self._client)
        
        # Also expose devices, scripts, etc. directly for cleaner API
        # (client.devices.get() instead of client.api.devices.get())
        self.devices = self.api.devices
        self.scripts = self.api.scripts
        self.fortimanagers = self.api.fortimanagers
        self.system = self.api.system

    
    def get_rate_limit_status(self) -> dict[str, Any]:
        """
        Get rate limit status for this FortiZTP client.
        
        Returns statistics about API calls and errors for this specific
        client instance (not session-wide).
        
        Returns:
            Dictionary containing:
            - calls_last_minute: Call count in last 60 seconds
            - calls_last_hour: Call count in last 3600 seconds
            - errors_last_minute: Error count in last 60 seconds
            - errors_last_hour: Error count in last 3600 seconds
            - total_calls: Total calls since client creation
            - total_errors: Total errors since client creation
            - limits: Configured rate limits (2000 calls/hour for FortiZTP)
            - within_limits: Whether client is within all configured limits
        
        Example:
            >>> fz = FortiZTP(oauth_token="...")
            >>> status = fz.get_rate_limit_status()
            >>> print(f"Calls last hour: {status['calls_last_hour']}/{status['limits']['calls_per_hour']}")
        """
        return self._rate_stats.get_status()
    
    def get_retry_stats(self) -> dict[str, Any]:
        """
        Get retry statistics from HTTP client.
        
        Returns statistics about retry attempts, including total retries,
        reasons for retries, and per-endpoint retry counts.
        
        Returns:
            Dictionary containing:
            - total_retries: Total retry attempts
            - total_requests: Total requests made
            - successful_requests: Successful requests
            - failed_requests: Failed requests
            - retry_by_reason: Retry counts by reason
            - retry_by_endpoint: Retry counts by endpoint
            - last_retry_time: Most recent retry timestamp
        
        Example:
            >>> client = FortiZTP(api_id="...", password="...")
            >>> response = client.devices.list_devices()
            >>> stats = client.get_retry_stats()
            >>> print(f"Total retries: {stats['total_retries']}")
        """
        return self._client.get_retry_stats()
    
    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all tracked API operations.

        Returns all tracked operations (GET/POST/PUT/DELETE) in chronological order.
        Only available when track_operations=True was passed to constructor.

        Returns:
            List of operation dictionaries with keys:
                - timestamp: ISO 8601 timestamp
                - method: HTTP method (GET/POST/PUT/DELETE)
                - path: API endpoint path
                - data: Request payload (for POST/PUT), None otherwise
                - status_code: HTTP response status code
                - read_only_simulated: True if operation was simulated in read-only mode

        Example:
            >>> fztp = FortiZTP(
            ...     oauth_token="...",
            ...     track_operations=True
            ... )
            >>> fztp.api.devices.get()
            >>> ops = fztp.get_operations()
            >>> print(ops[0])
            {
                "timestamp": "2024-01-15T10:30:00.123456",
                "method": "GET",
                "path": "/api/v2/devices",
                "data": None,
                "status_code": 200,
                "read_only_simulated": False
            }
        """
        return self._client.get_operations()
    
    def logout(self) -> None:
        """
        Clean up resources and logout.
        
        Closes HTTP client connections and releases OAuth token.
        
        Note:
            OAuth token revocation should be handled separately.
            This method only closes the HTTP connection.
        
        Example:
            >>> client = FortiZTP(api_id="...", password="...")
            >>> # ... use client ...
            >>> client.logout()
        """
        self._client.logout()
    
    def __enter__(self) -> "FortiZTP":
        """Context manager entry."""
        return self
    
    def __exit__(self, *args: object) -> None:
        """Context manager exit - closes HTTP client."""
        self.logout()
    
    def __repr__(self) -> str:
        """String representation of FortiZTP client."""
        return f"FortiZTP(base_url='{self._client._url}')"


__all__ = [
    # Main client
    "FortiZTP",
    # Version
    "__version__",
    # Response models
    "FortiZTPResponse",
    # Type definitions - Literal types
    "DeviceType",
    "ProvisionStatus",
    "ProvisionSubStatus",
    "ProvisionTarget",
    "ServiceStatus",
    # Type definitions - Data structures
    "DeviceV2Data",
    "PageDtoDeviceData",
    "ScriptMetaData",
    "PageDtoScriptMetaData",
    "FortiManagerMetaData",
    "PageDtoFortiManagerMetaData",
    "SystemData",
    "ErrorData",
]
