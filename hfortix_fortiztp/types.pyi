"""Type stubs for FortiZTP Cloud API type definitions."""

from typing import Literal
from typing_extensions import NotRequired, TypedDict

# Literal type definitions
DeviceType = Literal["FortiGate", "FortiAP", "FortiSwitch", "FortiExtender"]
ProvisionStatus = Literal["provisioned", "unprovisioned", "hidden", "incomplete"]
ProvisionSubStatus = Literal["waiting", "provisioning", "provisioningtoolong"]
ProvisionTarget = Literal["FortiManager", "FortiGateCloud", "FortiEdgeCloud", "ExternalController"]
ServiceStatus = Literal["Operational", "Degraded performance", "Partial outage", "Major outage"]

# Device data structures
class DeviceV2Data(TypedDict, total=False):
    deviceSN: str
    deviceType: DeviceType
    provisionStatus: ProvisionStatus
    provisionTarget: NotRequired[ProvisionTarget]
    region: NotRequired[str]
    externalControllerSn: NotRequired[str]
    externalControllerIp: NotRequired[str]
    platform: NotRequired[str]
    firmwareProfile: NotRequired[str]
    fortiManagerOid: NotRequired[int]
    scriptOid: NotRequired[int]
    useDefaultScript: NotRequired[bool]
    provisioningTimestamp: NotRequired[int]
    provisioningCompleteTimestamp: NotRequired[int]
    provisionSubStatus: NotRequired[ProvisionSubStatus]
    message: NotRequired[str]

class PageDtoDeviceData(TypedDict, total=False):
    total: int
    data: list[DeviceV2Data]
    hasCache: bool

# Script data structures
class ScriptMetaData(TypedDict, total=False):
    oid: int
    name: str
    updateTime: int

class PageDtoScriptMetaData(TypedDict, total=False):
    total: int
    data: list[ScriptMetaData]

# FortiManager data structures
class FortiManagerMetaData(TypedDict, total=False):
    oid: int
    sn: str
    ip: str
    scriptOid: NotRequired[int]
    updateTime: NotRequired[int]

class PageDtoFortiManagerMetaData(TypedDict, total=False):
    total: int
    data: list[FortiManagerMetaData]

# System data structures
class SystemData(TypedDict, total=False):
    serviceName: str
    serviceRegion: str
    serviceStatus: ServiceStatus
    serverTime: str

# Error structures
class ErrorData(TypedDict, total=False):
    error: str
    error_description: str

__all__: list[str]
