# hfortix-fortiztp

Python SDK for FortiZTP Cloud API v2.0 - Device provisioning and management for FortiGate, FortiAP, FortiSwitch, and FortiExtender.

> **⚠️ PRE-ALPHA:** This package is under active development. Code generation not yet complete.

## Features (Planned)

- 🔒 **OAuth 2.0 Authentication** - Automatic token management and refresh
- 📝 **Full Type Safety** - Type hints with Literal types for IDE autocomplete
- 🎯 **Specialized Responses** - Property access on response objects
- 🔄 **Smart Defaults** - Sensible defaults for optional parameters
- ⚡ **HTTP Metadata** - Access status codes, response times, raw data
- 🛡️ **Error Handling** - Comprehensive exception hierarchy

## Installation

```bash
# Not yet published to PyPI
pip install hfortix-fortiztp
```

## Quick Start

```python
from hfortix import FortiZTP

# Initialize client with OAuth credentials
client = FortiZTP(
    client_id="your_client_id",
    api_key="your_api_key",
    password="your_password"
)

# List all provisioned devices
response = client.v2.devices.list.get(provision_status="provisioned")
print(f"Total devices: {response.total}")

for device in response.data:
    print(f"{device['deviceSN']}: {device['provisionStatus']}")

# Get specific device
device = client.v2.devices.get.get(device_sn="FGT60D4615067214")
print(f"Device type: {device.deviceType}")
print(f"Status: {device.provisionStatus}")
```

## API Coverage

### Devices (5 endpoints)
- List devices with filters
- Bulk provision/unprovision
- Get single device details
- Provision/unprovision single device
- Get firmware profiles by region

### Settings - Scripts (7 endpoints)
- CRUD operations for script metadata
- Upload/download script content
- List all scripts

### Settings - FortiManagers (5 endpoints)
- CRUD operations for FortiManager configurations
- Support for HA setups
- Script association

### System (1 endpoint)
- Get system status

## Documentation

- [API Documentation](https://github.com/hermanwjacobsen/hfortix-fortiztp/blob/main/dev/internal-docs/API_DOCUMENTATION.md)
- [Schema Documentation](https://github.com/hermanwjacobsen/hfortix-fortiztp/blob/main/dev/internal-docs/SCHEMA_FORMAT.md)
- [Implementation Roadmap](https://github.com/hermanwjacobsen/hfortix-fortiztp/blob/main/dev/internal-docs/IMPLEMENTATION_ROADMAP.md)

## Development Status

**Schema:** ✅ 100% Complete (18/18 endpoints)  
**Code Generation:** ⏳ In Progress  
**Testing:** ❌ Not Started

See [SCHEMA_GAPS_ANALYSIS.md](https://github.com/hermanwjacobsen/hfortix-fortiztp/blob/main/dev/internal-docs/SCHEMA_GAPS_ANALYSIS.md) for detailed status.

## Requirements

- Python 3.9+
- hfortix-core >= 0.1.0
- httpx >= 0.24.0

## License

MIT License - See [LICENSE](LICENSE) file for details

## Contributing

This package is part of the hfortix SDK family:
- [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core) - Core HTTP client and utilities
- [hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) - FortiOS REST API
- [hfortix-forticare](https://github.com/hermanwjacobsen/hfortix-forticare) - FortiCare Asset Management API
- [hfortix-fortiztp](https://github.com/hermanwjacobsen/hfortix-fortiztp) - FortiZTP Cloud API (this package)
- [hfortix](https://github.com/hermanwjacobsen/hfortix) - Meta package

## Support

- GitHub Issues: https://github.com/hermanwjacobsen/hfortix-fortiztp/issues
- Documentation: https://hfortix.readthedocs.io

## Author

FortiX Development Team  
Email: herman.w.jacobsen@gmail.com

---

**Last Updated:** February 6, 2026  
**Version:** 0.1.0-dev  
**Status:** Pre-Alpha
