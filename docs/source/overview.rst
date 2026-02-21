Overview
========

**HFortix-FortiZTP** provides a fully typed Python SDK for the FortiZTP Cloud API v2.0.

Key Features
------------

**CloudSession Support**
   Integrate with CloudSession for efficient multi-service OAuth token management.

**Rate Limit Tracking**
   Monitor API usage across multiple time windows (last minute, 5 minutes, hour).

**Full Type Safety**
   Complete type hints with Literal types for IDE autocomplete.

**Specialized Responses**
   Property access on response objects for cleaner code.

**OAuth 2.0**
   Automatic token management with refresh support.

What You Can Do
---------------

* **Device Management**: List, provision, unprovision devices (FortiGate, FortiAP, FortiSwitch, FortiExtender)
* **Script Management**: Create, update, delete pre-run CLI scripts
* **FortiManager Integration**: Configure and manage FortiManager connections
* **System Monitoring**: Get system status and health checks

API Coverage
------------

**18 endpoints across 4 categories:**

* **Devices** (5 endpoints): List, get, update, bulk operations, firmware profiles
* **Scripts** (7 endpoints): List, create, update, delete, content management
* **FortiManagers** (5 endpoints): List, create, update, delete configurations
* **System** (1 endpoint): Get system status

Rate Limits
-----------

FortiZTP enforces:

* **2000 calls per hour**

Use the built-in rate limit tracking to monitor your usage.
