"""Type stubs for FortiZTP Cloud API V2."""

from hfortix_core.http.cloud_client import CloudHTTPClient
from .devices import DevicesAPI
from .fortimanagers import FortiManagersAPI
from .scripts import ScriptsAPI
from .system import SystemAPI

class V2API:
    """FortiZTP Cloud API V2 endpoints."""
    
    _client: CloudHTTPClient
    devices: DevicesAPI
    scripts: ScriptsAPI
    fortimanagers: FortiManagersAPI
    system: SystemAPI
    
    def __init__(self, client: CloudHTTPClient) -> None: ...
