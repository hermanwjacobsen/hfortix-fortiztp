"""
FortiZTP Devices API.

Auto-generated from schema - contains 5 endpoints.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from hfortix_core.http.cloud_client import CloudHTTPClient

from hfortix_fortiztp.models import FortiZTPResponse
from hfortix_fortiztp.types import (
    DeviceType,
    ProvisionStatus,
    ProvisionTarget,
)


class DevicesAPI:
    """Devices API endpoints."""

    def __init__(self, client: "CloudHTTPClient") -> None:
        """Initialize Devices API."""
        self._client = client

    def list(
        self,
        provision_status: Optional[ProvisionStatus] = None,
        device_type: Optional[DeviceType] = None,
        device_sn: Optional[str] = None,
        use_cache: Optional[bool] = None,
    ) -> FortiZTPResponse:
        """
        Get devices provisioning status.

        Retrieve the provisioning status of devices registered in the account.

        Args:
            provision_status: Filter by provision status (optional)
            device_type: Filter by device type (optional)
            device_sn: Filter by device serial number(s) - comma-separated for multiple (optional)
            use_cache: Use cached data (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.list(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/devices"

        # Build query parameters
        params = {}
        if provision_status is not None:
            params['provisionStatus'] = provision_status
        if device_type is not None:
            params['deviceType'] = device_type
        if device_sn is not None:
            params['deviceSN'] = device_sn
        if use_cache is not None:
            params['useCache'] = use_cache

        # Make HTTP request
        response = self._client.get(path, params=params)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def bulk_provision(
        self,
        devices: List[Dict[str, Any]],
    ) -> FortiZTPResponse:
        """
        Provision/Unprovision devices.

        Provision or unprovision multiple devices in a single request.

        Args:

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.bulk_provision(...)
            >>> print(response.http_status_code)
        """
        path = "/v2/devices"

        # Build request body
        data = devices

        # Make HTTP request
        response = self._client.put(path, data=data)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def get(
        self,
        device_sn: str,
        use_cache: Optional[bool] = None,
    ) -> FortiZTPResponse:
        """
        Get specific device provisioning status.

        Retrieve the provisioning status of specific device registered in the account.

        Args:
            device_sn: Device serial number (required)
            use_cache: Use cached data (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.get(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/devices/{device_sn}"

        # Build query parameters
        params = {}
        if use_cache is not None:
            params['useCache'] = use_cache

        # Make HTTP request
        response = self._client.get(path, params=params)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


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
    ) -> FortiZTPResponse:
        """
        Provision/Unprovision device.

        Provision or unprovision a single device.

        Args:
            device_sn: Device serial number (required)
            device_type: Device type (required)
            provision_status: Set to 'provisioned' to provision, 'unprovisioned' to unprovision (required)
            provision_target: Target system for provisioning (optional)
            region: Region for cloud targets. Not needed for FortiManager, FortiManagerCloud, or ExternalController (optional)
            external_controller_sn: FortiManager serial number. Only for FortiManager provision (optional)
            external_controller_ip: FQDN/IP for FortiManager or AP ExternalController. IPv4 and FQDN supported (optional)
            platform: VM platform (e.g., FortiGate-VM64-KVM). Required for FGT VM to FortiManagerCloud (optional)
            firmware_profile: Firmware profile name created in FortiGateCloud (optional)
            forti_manager_oid: FortiManager object ID. Preferred over externalControllerSn/externalControllerIp (optional)
            script_oid: Pre-run script object ID for FortiManager provision (optional)
            use_default_script: Use FortiManager's default pre-run script (optional)
            provisioning_timestamp: Unix timestamp when provisioning started (optional)
            provisioning_complete_timestamp: Unix timestamp when provisioning completed (optional)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.put(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/devices/{device_sn}"

        # Build request body
        data = {}
        data['deviceSN'] = device_sn
        data['deviceType'] = device_type
        data['provisionStatus'] = provision_status
        if provision_target is not None:
            data['provisionTarget'] = provision_target
        if region is not None:
            data['region'] = region
        if external_controller_sn is not None:
            data['externalControllerSn'] = external_controller_sn
        if external_controller_ip is not None:
            data['externalControllerIp'] = external_controller_ip
        if platform is not None:
            data['platform'] = platform
        if firmware_profile is not None:
            data['firmwareProfile'] = firmware_profile
        if forti_manager_oid is not None:
            data['fortiManagerOid'] = forti_manager_oid
        if script_oid is not None:
            data['scriptOid'] = script_oid
        if use_default_script is not None:
            data['useDefaultScript'] = use_default_script
        if provisioning_timestamp is not None:
            data['provisioningTimestamp'] = provisioning_timestamp
        if provisioning_complete_timestamp is not None:
            data['provisioningCompleteTimestamp'] = provisioning_complete_timestamp

        # Make HTTP request
        response = self._client.put(path, data=data)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


    def firmware_profiles(
        self,
        device_sn: str,
        region: str,
    ) -> FortiZTPResponse:
        """
        Get firmware profiles for specific device.

        Retrieve firmware profiles for specific device.

        Args:
            device_sn: Device serial number (required)
            region: Region identifier (required)

        Returns:
            FortiZTPResponse: Response object with:
            - .http_status_code: HTTP status code
            - .response_time: Request duration
            - .raw: Raw response dict
            - Dict-like access to response fields

        Example:
            >>> response = client.api.devices.firmware_profiles(...)
            >>> print(response.http_status_code)
        """
        # Build path with parameters
        path = f"/v2/devices/{device_sn}/regions/{region}/firmwareprofiles"

        # Make HTTP request
        response = self._client.get(path)

        # Wrap in FortiZTPResponse
        return FortiZTPResponse(response)


__all__ = ["DevicesAPI"]
