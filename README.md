# hfortix-fortiztp

Python SDK for the FortiZTP Cloud API v2.0 — zero-touch provisioning for
FortiGate, FortiAP, FortiSwitch, and FortiExtender devices.

Part of the [hfortix](https://github.com/hermanwjacobsen/hfortix) SDK family,
built on the shared [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core)
HTTP foundation (retries, rate limiting, circuit breaker, audit logging).

## Features

- **OAuth 2.0 authentication** — auto-login with FortiCloud API credentials,
  pre-obtained tokens, or a shared `CloudSession`
- **Full type safety** — type hints with `Literal` types and bundled `.pyi`
  stubs (PEP 561) for IDE autocomplete
- **Device lifecycle** — list, inspect, provision/unprovision (single or bulk)
- **Script management** — pre-run CLI script metadata and content
- **FortiManager integration** — manage FortiManager connection settings
- **HTTP metadata** — status codes, response times, and raw data on every response
- **Rate limit tracking** — monitor usage against FortiZTP's 2,000 calls/hour limit

## Installation

```bash
pip install hfortix-fortiztp
```

## Authentication

Three options:

```python
from hfortix_fortiztp import FortiZTP

# 1. FortiCloud IAM API credentials (auto-login)
client = FortiZTP(api_id="your_api_id", password="your_password")

# 2. Pre-obtained OAuth token
client = FortiZTP(oauth_token="your_oauth_token")

# 3. Shared CloudSession (recommended when also using FortiCare)
from hfortix_core.session import CloudSession
from hfortix_forticare import FortiCare

with CloudSession(api_id="your_api_id", password="your_password") as session:
    fcc = FortiCare(session=session)   # uses client_id "assetmanagement"
    fztp = FortiZTP(session=session)   # uses client_id "fortiztp"
    # Both share one session; each gets its own OAuth token
```

## Quick Start

```python
from hfortix_fortiztp import FortiZTP

client = FortiZTP(api_id="your_api_id", password="your_password")

# List devices, optionally filtered
response = client.devices.list(provision_status="provisioned")
print(f"Total devices: {response.total}")
for device in response:
    print(f"{device.deviceSN}: {device.provisionStatus}")

# Get a single device by serial number
device = client.devices.get(device_sn="FGT60FTK19000001")
print(f"Type: {device.deviceType}, status: {device.provisionStatus}")

# Provision a single device to FortiManager
client.devices.put(
    device_sn="FGT60FTK19000001",
    device_type="FortiGate",
    provision_status="provisioned",
    provision_target="FortiManager",
    forti_manager_oid=12345,
)

# Bulk provision/unprovision (wire-format dicts)
client.devices.put_bulk(
    devices=[
        {
            "deviceSN": "FGT60FTK19000001",
            "deviceType": "FortiGate",
            "provisionStatus": "provisioned",
            "provisionTarget": "FortiManager",
        },
    ]
)

client.logout()
```

## API Navigation

`client.<category>` is an alias for `client.api.<category>` — both work.

```python
client.devices.list(provision_status=..., device_type=..., device_sn=..., use_cache=...)
client.devices.get(device_sn=...)          # single device (lists all if omitted)
client.devices.put(device_sn=..., device_type=..., provision_status=..., ...)
client.devices.put_bulk(devices=[...])     # bulk provision/unprovision
client.devices.regions.firmwareprofiles.get(device_sn=..., region=...)

client.scripts.scripts_list()
client.scripts.scripts_get(oid=123)
client.scripts.scripts_post(oid=123, name="script1")
client.scripts.scripts_put(oid=123, name="script1-updated")
client.scripts.scripts_delete(oid=123)
client.scripts.scripts_get_content(oid=123)
client.scripts.scripts_put_content(oid=123)

client.fortimanagers.fortimanagers_list()
client.fortimanagers.fortimanagers_get(oid=789)
client.fortimanagers.fortimanagers_post(sn="FMG-VMTM23010656", ip="192.168.223.20")
client.fortimanagers.fortimanagers_put(oid=789, sn="FMG-VMTM23010656", ip="192.168.223.20")
client.fortimanagers.fortimanagers_delete(oid=789)

client.system.system_get()                 # service status
```

Every call returns a `FortiZTPResponse` with attribute/dict access to the
payload plus `.http_status_code`, `.response_time`, `.raw`, and
`.request_info` metadata.

## Rate Limit Tracking

FortiZTP enforces 2,000 calls/hour. The SDK can track your usage
(monitoring only — enforcement is opt-in via `rate_limit=True`):

```python
client = FortiZTP(
    api_id="...",
    password="...",
    rate_limit_calls_per_hour=2000,
)
status = client.get_rate_limit_status()
print(f"Calls last hour: {status['calls_last_hour']}")
```

## Documentation

- Package docs: https://hfortix.readthedocs.io
- FortiZTP Cloud API reference: https://fndn.fortinet.net/ (Fortinet Developer Network)
- Full IDE autocomplete via bundled `.pyi` stubs

## Requirements

- Python 3.9+
- hfortix-core >= 0.5.161
- httpx >= 0.24.0

## Related Packages

- [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core) — Core HTTP client and utilities
- [hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) — FortiOS REST API
- [hfortix-forticare](https://github.com/hermanwjacobsen/hfortix-forticare) — FortiCare Asset Management API
- [hfortix](https://github.com/hermanwjacobsen/hfortix) — Meta package

## License

MIT License — see [LICENSE](LICENSE).

## Support

- GitHub Issues: https://github.com/hermanwjacobsen/hfortix-fortiztp/issues
- Documentation: https://hfortix.readthedocs.io
