"""
FortiZTP Devices API.

Auto-generated from schema - contains 5 endpoints.
"""

from hfortix_core.http.cloud_client import CloudHTTPClient
from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import DeviceType, ProvisionStatus, ProvisionTarget
from typing import Optional, List, Dict, Any
from .regions import Regions

class DevicesAPI:
    """Devices API endpoints."""
    
    _client: CloudHTTPClient
    regions: Regions
    
    def __init__(self, client: CloudHTTPClient) -> None: ...
    
    def list(
        self,
        provision_status: Optional[ProvisionStatus] = None,
        device_type: Optional[DeviceType] = None,
        device_sn: Optional[str] = None,
        use_cache: Optional[bool] = None,
    ) -> FortiZTPResponse: ...
    
    def put_bulk(
        self,
        devices: List[Dict[str, Any]],
    ) -> FortiZTPResponse: ...
    
    def get(
        self,
        device_sn: Optional[str] = None,
        use_cache: Optional[bool] = None,
    ) -> FortiZTPResponse: ...
    
    def put(
        self,
        device_sn: str,
        device_type: DeviceType,
        provision_status: ProvisionStatus,
        provision_target: Optional[ProvisionTarget] = None,
        region: Optional[str] = None,
        external_controller_sn: Optional[str] = None,
        external_controller_ip: Optional[str] = None,
        platform: Optional[str] = None,
        firmware_profile: Optional[str] = None,
        forti_manager_oid: Optional[int] = None,
        script_oid: Optional[int] = None,
        use_default_script: Optional[bool] = None,
        provisioning_timestamp: Optional[int] = None,
        provisioning_complete_timestamp: Optional[int] = None,
    ) -> FortiZTPResponse: ...
    