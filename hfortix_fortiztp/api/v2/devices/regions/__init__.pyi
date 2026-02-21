"""
FortiZTP API - Regions

Wrapper for regions-specific endpoints.
"""

from hfortix_core.http.interface import IHTTPClient
from .firmwareprofiles import Firmwareprofiles

class Regions:
    """Regions endpoints wrapper."""
    
    _client: IHTTPClient
    firmwareprofiles: Firmwareprofiles
    