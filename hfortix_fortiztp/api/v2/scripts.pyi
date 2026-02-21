"""
FortiZTP Scripts API.

Auto-generated from schema - contains 7 endpoints.
"""

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import DeviceType, ProvisionStatus, ProvisionTarget
from typing import Optional, Any

class ScriptsAPI:
    """Scripts API endpoints."""
    
    _client: CloudHTTPClient
    
    def __init__(self, client: CloudHTTPClient) -> None: ...
    
    def scripts_get(
        self,
        oid: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def scripts_put(
        self,
        oid: int,
        name: str,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def scripts_delete(
        self,
        oid: int,
    ) -> FortiZTPResponse: ...
    
    def scripts_list(
        self,
    ) -> FortiZTPResponse: ...
    
    def scripts_post(
        self,
        oid: int,
        name: str,
        update_time: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def scripts_get_content(
        self,
        oid: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    
    def scripts_put_content(
        self,
        oid: int,
    ) -> FortiZTPResponse: ...
    