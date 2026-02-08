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

from typing import TYPE_CHECKING, Any

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_core.http.oauth import FortiCloudAuth

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
    from typing import Optional


__version__ = "0.1.0"


class FortiZTP:
    """
    FortiZTP Cloud API client.
    
    Main entry point for interacting with the FortiZTP Cloud API v2.0.
    Handles OAuth 2.0 authentication and provides access to all API endpoints.
    
    Authentication:
        Automatically obtains OAuth token using API credentials, or accepts
        pre-obtained token.
    
    Rate Limits:
        - 2,000 calls per hour
    
    Args:
        api_id: FortiCloud API ID (for auto-login)
        password: FortiCloud password (for auto-login)
        client_id: Client ID for OAuth authentication (default: fortiztp)
        oauth_token: Pre-obtained OAuth token (alternative to api_id/password)
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
    
    Example:
        >>> # Auto-login with credentials
        >>> client = FortiZTP(
        ...     api_id="your_api_id",
        ...     password="your_password"
        ... )
        >>> 
        >>> # Or with pre-obtained token
        >>> client = FortiZTP(oauth_token="your_token")
        >>> 
        >>> # Check system status
        >>> status = client.system.get_status()
        >>> print(f"Status: {status['serviceStatus']}")
        >>> 
        >>> # List all devices
        >>> devices = client.devices.list_devices()
        >>> print(f"Total devices: {devices['total']}")
        >>> 
        >>> # Clean up
        >>> client.logout()
    
    Raises:
        ValueError: If neither oauth_token nor (api_id and password) are provided
    """
    
    def __init__(
        self,
        api_id: Optional[str] = None,
        password: Optional[str] = None,
        client_id: str = "fortiztp",
        oauth_token: Optional[str] = None,
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
    ) -> None:
        """Initialize FortiZTP client with OAuth credentials."""
        # Obtain OAuth token if credentials provided
        self._auth: Optional[FortiCloudAuth] = None
        
        if not oauth_token:
            if not api_id or not password:
                raise ValueError(
                    "Either oauth_token or (api_id and password) must be provided"
                )
            
            # Auto-login to get token
            self._auth = FortiCloudAuth(
                api_id=api_id,
                password=password,
                client_id=client_id,
                auth_url=auth_url,
            )
            oauth_token = self._auth.get_token()
        
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
        )
        
        # Initialize API endpoints
        from .api.v2 import V2API
        self.api = V2API(self._client)
    
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
