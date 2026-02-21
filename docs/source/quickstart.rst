Quick Start
===========

Installation
------------

.. code-block:: bash

   pip install hfortix-fortiztp

Basic Usage
-----------

CloudSession (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_fortiztp import FortiZTP

   with CloudSession(api_id="your_api_id", password="your_password") as session:
       client = FortiZTP(session=session)
       devices = client.devices.get()

Auto-Login
~~~~~~~~~~

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   client = FortiZTP(
       api_id="your_api_id",
       password="your_password"
   )

   devices = client.devices.get()
   client.logout()

Common Operations
-----------------

List Devices
~~~~~~~~~~~~

.. code-block:: python

   # List all devices
   devices = client.devices.get()

   # Filter by status
   provisioned = client.devices.get(provision_status="provisioned")

   # Filter by type
   fortigates = client.devices.get(device_type="FortiGate")

Get Device Details
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   device = client.devices.get(device_sn="FGT60FTK19000001")
   print(f"Device: {device.deviceType}")
   print(f"Status: {device.provisionStatus}")

Provision Device
~~~~~~~~~~~~~~~~

.. code-block:: python

   result = client.devices.update(
       device_sn="FGT60FTK19000001",
       provision_target="FortiManager",
       fortimanager_oid=12345
   )

Bulk Operations
~~~~~~~~~~~~~~~

.. code-block:: python

   result = client.devices.bulk_provision(
       devices=[
           {"deviceSN": "FGT001", "provisionTarget": "FortiManager"},
           {"deviceSN": "FGT002", "provisionTarget": "FortiManager"}
       ]
   )

Manage Scripts
~~~~~~~~~~~~~~

.. code-block:: python

   # List scripts
   scripts = client.scripts.scripts_list()

   # Create script
   result = client.scripts.scripts_post(
       script_name="initial-config",
       description="Initial configuration"
   )

   # Upload script content
   client.scripts.scripts_content_put(
       script_id=123,
       content="config system global\\nset hostname FG-001\\nend"
   )

System Status
~~~~~~~~~~~~~

.. code-block:: python

   status = client.system.system_get()
   print(f"System status: {status.serviceStatus}")

Rate Limit Tracking
-------------------

.. code-block:: python

   client = FortiZTP(
       api_id="...",
       password="...",
       rate_limit_calls_per_hour=2000
   )

   status = client.get_rate_limit_status()
   print(f"Calls: {status['calls_last_hour']}/2000")
