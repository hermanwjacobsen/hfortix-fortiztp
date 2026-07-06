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
    - devices: Device provisioning and management (5 endpoints)
    - scripts: Pre-run CLI script management (7 endpoints)
    - fortimanagers: FortiManager integration (5 endpoints)
    - system: System status (1 endpoint)

    Example:
        >>> from hfortix_fortiztp import FortiZTP
        >>> client = FortiZTP(api_id="...", password="...")
        >>>
        >>> # Access device endpoints
        >>> devices = client.api.devices.list()
        >>>
        >>> # Access script endpoints
        >>> scripts = client.api.scripts.scripts_list()
        >>>
        >>> # Access system status
        >>> status = client.api.system.system_get()
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
