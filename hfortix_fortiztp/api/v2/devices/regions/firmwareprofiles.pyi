"""
FortiZTP API - Firmwareprofiles

Endpoint for firmwareprofiles resources.

API Endpoints:
    GET /v2/devices/{deviceSN}/regions/{region}/firmwareprofiles

Example Usage:
    >>> from hfortix_fortiztp import FortiZTP
    >>> client = FortiZTP(api_key="your-api-key")
    >>>
    >>> response = client.devices.regions.firmwareprofiles.get(...)
"""

from hfortix_core.http.interface import IHTTPClient
from hfortix_fortiztp.models import FortiZTPResponse

class Firmwareprofiles:
    """Firmwareprofiles Operations."""
    
    _client: IHTTPClient
    
    def get(
        self,
        device_sn: str,
        region: str,
    ) -> FortiZTPResponse: ...
    