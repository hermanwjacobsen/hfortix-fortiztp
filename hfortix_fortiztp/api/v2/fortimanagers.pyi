"""
FortiZTP Fortimanagers API.

Auto-generated from schema - contains 5 endpoints.
"""

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import DeviceType, ProvisionStatus, ProvisionTarget
from typing import Optional, Any

class FortiManagersAPI:
    """Fortimanagers API endpoints."""
    
    _client: CloudHTTPClient
    
    def __init__(self, client: CloudHTTPClient) -> None: ...
    
    def fortimanagers_get(
        self,
        oid: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def fortimanagers_put(
        self,
        oid: int,
        sn: str,
        ip: str,
        script_oid: Optional[int] = None,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def fortimanagers_delete(
        self,
        oid: int,
    ) -> FortiZTPResponse: ...
    
    def fortimanagers_list(
        self,
    ) -> FortiZTPResponse: ...
    
    def fortimanagers_post(
        self,
        sn: str,
        ip: str,
        oid: Optional[int] = None,
        script_oid: Optional[int] = None,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    