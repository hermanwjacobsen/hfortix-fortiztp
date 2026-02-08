"""FortiZTP Cloud API V2."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.cloud_client import CloudHTTPClient

from .devices import DevicesAPI
from .fortimanagers import FortiManagersAPI
from .scripts import ScriptsAPI
from .system import SystemAPI


class V2API:
    """
    FortiZTP Cloud API V2 endpoints.
    
    Provides access to all API categories:
    - devices: Device provisioning and management (10 endpoints)
    - scripts: Pre-run CLI script management (3 endpoints)
    - fortimanagers: FortiManager integration (3 endpoints)
    - system: System status and health (2 endpoints)
    
    Example:
        >>> from hfortix_fortiztp import FortiZTP
        >>> client = FortiZTP(api_id="...", password="...")
        >>> 
        >>> # Access device endpoints
        >>> devices = client.api.devices.list_devices()
        >>> 
        >>> # Access script endpoints
        >>> scripts = client.api.scripts.list_scripts()
        >>> 
        >>> # Access system status
        >>> status = client.api.system.get_status()
    """

    def __init__(self, client: "CloudHTTPClient") -> None:
        """
        Initialize V2 API with HTTP client.
        
        Args:
            client: CloudHTTPClient instance for making HTTP requests
        """
        self._client = client

        self.devices = DevicesAPI(client)
        self.scripts = ScriptsAPI(client)
        self.fortimanagers = FortiManagersAPI(client)
        self.system = SystemAPI(client)


__all__ = ["V2API"]
