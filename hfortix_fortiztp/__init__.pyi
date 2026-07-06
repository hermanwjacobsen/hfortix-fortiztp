"""Type stubs for FortiZTP Cloud API SDK."""

from typing import Any, Optional

from hfortix_core.http import CloudHTTPClient
from hfortix_core.http.oauth import FortiCloudAuth
from hfortix_core.session import CloudSession
from .api.v2 import V2API
from .api.v2.devices import DevicesAPI
from .api.v2.scripts import ScriptsAPI
from .api.v2.fortimanagers import FortiManagersAPI
from .api.v2.system import SystemAPI
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
    DEFAULT_CLIENT_ID: str
    _auth: Optional[FortiCloudAuth]
    _client: CloudHTTPClient
    api: V2API
    devices: DevicesAPI
    scripts: ScriptsAPI
    fortimanagers: FortiManagersAPI
    system: SystemAPI
    
    def __init__(
        self,
        api_id: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        oauth_token: Optional[str] = None,
        session: Optional[CloudSession] = None,
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
        rate_limit_calls_per_min: Optional[int] = None,
        rate_limit_calls_per_5min: Optional[int] = None,
        rate_limit_calls_per_hour: Optional[int] = None,
        rate_limit_errors_per_min: Optional[int] = None,
        rate_limit_errors_per_5min: Optional[int] = None,
        rate_limit_errors_per_hour: Optional[int] = None,
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        circuit_breaker_half_open_calls: int = 3,
    ) -> None: ...
    
    def get_rate_limit_status(self) -> dict[str, Any]: ...
    def get_retry_stats(self) -> dict[str, Any]: ...
    def get_operations(self) -> list[dict[str, Any]]: ...
    def logout(self) -> None: ...
    def __enter__(self) -> FortiZTP: ...
    def __exit__(self, *args: object) -> None: ...
    def __repr__(self) -> str: ...

__all__: list[str]
