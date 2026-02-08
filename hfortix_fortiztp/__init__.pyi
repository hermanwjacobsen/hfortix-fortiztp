"""Type stubs for FortiZTP Cloud API SDK."""

from typing import Any, Optional

from hfortix_core.http import CloudHTTPClient
from hfortix_core.http.oauth import FortiCloudAuth
from .models import FortiZTPResponse
from .types import (
    DeviceType,
    DeviceV2Data,
    ErrorData,
    FortiManagerMetaData,
    PageDtoDeviceData,
    PageDtoFortiManagerMetaData,
    PageDtoScriptMetaData,
    ProvisionStatus,
    ProvisionSubStatus,
    ProvisionTarget,
    ScriptMetaData,
    ServiceStatus,
    SystemData,
)

__version__: str

class FortiZTP:
    _auth: Optional[FortiCloudAuth]
    _client: CloudHTTPClient
    
    def __init__(
        self,
        api_id: Optional[str] = None,
        password: Optional[str] = None,
        client_id: str = "fortiztp",
        oauth_token: Optional[str] = None,
        base_url: str = "https://fortiztp.forticloud.com/public/api",
        auth_url: Optional[str] = None,
        verify: bool = True,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        read_only: bool = False,
        track_operations: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
    ) -> None: ...
    
    def get_retry_stats(self) -> dict[str, Any]: ...
    def logout(self) -> None: ...
    def __enter__(self) -> FortiZTP: ...
    def __exit__(self, *args: object) -> None: ...
    def __repr__(self) -> str: ...

__all__: list[str]
