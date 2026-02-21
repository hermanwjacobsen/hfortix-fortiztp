"""
FortiZTP System API.

Auto-generated from schema - contains 1 endpoints.
"""

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import DeviceType, ProvisionStatus, ProvisionTarget
from typing import Any

class SystemAPI:
    """System API endpoints."""
    
    _client: CloudHTTPClient
    
    def __init__(self, client: CloudHTTPClient) -> None: ...
    
    def system_get(
        self,
    ) -> FortiZTPResponse: ...
    