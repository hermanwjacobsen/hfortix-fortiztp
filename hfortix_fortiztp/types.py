"""
Type definitions for FortiZTP Cloud API.

Provides TypedDict classes and Literal types for:
- API request/response structures
- Enum-like values (device types, statuses)

Auto-generated from schema - DO NOT EDIT MANUALLY
"""

from typing import Literal, TypedDict
from typing_extensions import NotRequired


# ============================================================================
# Literal Type Definitions (Enum-like values)
# ============================================================================

DeviceType = Literal["FortiGate", "FortiAP", "FortiSwitch", "FortiExtender"]
"""Supported device types for provisioning."""

ProvisionStatus = Literal["provisioned", "unprovisioned", "hidden", "incomplete"]
"""Device provision status values."""

ProvisionSubStatus = Literal["waiting", "provisioning", "provisioningtoolong"]
"""Sub-status for incomplete provisioning."""

ProvisionTarget = Literal["FortiManager", "FortiGateCloud", "FortiEdgeCloud", "ExternalController"]
"""Provisioning target type."""

ServiceStatus = Literal["Operational", "Degraded performance", "Partial outage", "Major outage"]
"""System service status values."""


# ============================================================================
# Device Data Structures
# ============================================================================

class DeviceV2Data(TypedDict, total=False):
    """
    Device data structure for FortiZTP API v2.
    
    Contains device provisioning information and status.
    """
    
    deviceSN: str
    """Device serial number (required)"""
    
    deviceType: DeviceType
    """Device type: FortiGate, FortiAP, FortiSwitch, or FortiExtender (required)"""
    
    provisionStatus: ProvisionStatus
    """Current provision status (required)"""
    
    provisionTarget: NotRequired[ProvisionTarget]
    """Target system for provisioning (optional)"""
    
    region: NotRequired[str]
    """Device region. Required for cloud targets, not needed for FortiManager (optional)"""
    
    externalControllerSn: NotRequired[str]
    """FortiManager serial number. Only needed for FortiManager provision (optional)"""
    
    externalControllerIp: NotRequired[str]
    """FQDN/IP for FortiManager or ExternalController. IPv4 and FQDN supported (optional)"""
    
    platform: NotRequired[str]
    """VM platform (e.g., FortiGate-VM64-KVM). Required for FMC provision (optional)"""
    
    firmwareProfile: NotRequired[str]
    """Firmware profile name from FortiGateCloud (optional)"""
    
    fortiManagerOid: NotRequired[int]
    """FortiManager OID. Preferred over externalControllerSn/Ip (optional)"""
    
    scriptOid: NotRequired[int]
    """Pre-run script OID for FortiManager provision (optional)"""
    
    useDefaultScript: NotRequired[bool]
    """Use FortiManager's default pre-run script (optional)"""
    
    provisioningTimestamp: NotRequired[int]
    """Unix timestamp when provisioning started (optional)"""
    
    provisioningCompleteTimestamp: NotRequired[int]
    """Unix timestamp when provisioning completed (optional)"""
    
    provisionSubStatus: NotRequired[ProvisionSubStatus]
    """Sub-status for incomplete provisioning (optional)"""
    
    message: NotRequired[str]
    """Description of substatus (optional)"""


class PageDtoDeviceData(TypedDict, total=False):
    """Paginated response for device list."""
    
    total: int
    """Total number of devices"""
    
    data: list[DeviceV2Data]
    """Array of device data"""
    
    hasCache: bool
    """Whether cached data is available"""


# ============================================================================
# Script Data Structures
# ============================================================================

class ScriptMetaData(TypedDict, total=False):
    """
    Script metadata structure.
    
    Contains script information (excluding content).
    """
    
    oid: int
    """Unique identifier for script"""
    
    name: str
    """Script name"""
    
    updateTime: int
    """Update time in milliseconds since Jan 01 1970 (UTC)"""


class PageDtoScriptMetaData(TypedDict, total=False):
    """Paginated response for script list."""
    
    total: int
    """Total number of scripts"""
    
    data: list[ScriptMetaData]
    """Array of script metadata"""


# ============================================================================
# FortiManager Data Structures
# ============================================================================

class FortiManagerMetaData(TypedDict, total=False):
    """
    FortiManager metadata structure.
    
    Supports HA configurations with comma-separated values.
    """
    
    oid: int
    """Unique identifier for FortiManager setting data"""
    
    sn: str
    """FortiManager serial number(s). Comma-separated for HA (required)"""
    
    ip: str
    """FortiManager IP/hostname(s). Comma-separated for HA (required)"""
    
    scriptOid: NotRequired[int]
    """Pre-run CLI script OID (optional)"""
    
    updateTime: NotRequired[int]
    """Update time in milliseconds since Jan 01 1970 (UTC)"""


class PageDtoFortiManagerMetaData(TypedDict, total=False):
    """Paginated response for FortiManager list."""
    
    total: int
    """Total number of FortiManagers"""
    
    data: list[FortiManagerMetaData]
    """Array of FortiManager metadata"""


# ============================================================================
# System Data Structures
# ============================================================================

class SystemData(TypedDict, total=False):
    """
    System status data structure.
    
    Contains FortiZTP service status information.
    """
    
    serviceName: str
    """Service name (e.g., FortiZTP)"""
    
    serviceRegion: str
    """Service region"""
    
    serviceStatus: ServiceStatus
    """Service status: Operational, Degraded performance, Partial outage, or Major outage"""
    
    serverTime: str
    """Server timestamp (ISO format)"""


# ============================================================================
# Error Response Structure
# ============================================================================

class ErrorData(TypedDict, total=False):
    """
    Error response structure.
    
    Returned for HTTP error status codes (401, 403, 404, 500).
    """
    
    error: str
    """Error code"""
    
    error_description: str
    """Error description"""


__all__ = [
    # Literal types
    "DeviceType",
    "ProvisionStatus",
    "ProvisionSubStatus",
    "ProvisionTarget",
    "ServiceStatus",
    # Device structures
    "DeviceV2Data",
    "PageDtoDeviceData",
    # Script structures
    "ScriptMetaData",
    "PageDtoScriptMetaData",
    # FortiManager structures
    "FortiManagerMetaData",
    "PageDtoFortiManagerMetaData",
    # System structures
    "SystemData",
    # Error structures
    "ErrorData",
]
