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
       devices = client.devices.list()

Auto-Login
~~~~~~~~~~

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   client = FortiZTP(
       api_id="your_api_id",
       password="your_password"
   )

   devices = client.devices.list()
   client.logout()

Common Operations
-----------------

List Devices
~~~~~~~~~~~~

.. code-block:: python

   # List all devices
   devices = client.devices.list()

   # Filter by status
   provisioned = client.devices.list(provision_status="provisioned")

   # Filter by type
   fortigates = client.devices.list(device_type="FortiGate")

Get Device Details
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   device = client.devices.get(device_sn="FGT60FTK19000001")
   print(f"Device: {device.deviceType}")
   print(f"Status: {device.provisionStatus}")

Provision Device
~~~~~~~~~~~~~~~~

.. code-block:: python

   result = client.devices.put(
       device_sn="FGT60FTK19000001",
       device_type="FortiGate",
       provision_status="provisioned",
       provision_target="FortiManager",
       forti_manager_oid=12345
   )

Bulk Operations
~~~~~~~~~~~~~~~

.. code-block:: python

   # Bulk provision/unprovision — list of wire-format dicts
   result = client.devices.put_bulk(
       devices=[
           {
               "deviceSN": "FGT001",
               "deviceType": "FortiGate",
               "provisionStatus": "provisioned",
               "provisionTarget": "FortiManager",
           },
           {
               "deviceSN": "FGT002",
               "deviceType": "FortiGate",
               "provisionStatus": "provisioned",
               "provisionTarget": "FortiManager",
           },
       ]
   )

Firmware Profiles
~~~~~~~~~~~~~~~~~

.. code-block:: python

   profiles = client.devices.regions.firmwareprofiles.get(
       device_sn="FGT60FTK19000001",
       region="global"
   )

Manage Scripts
~~~~~~~~~~~~~~

.. code-block:: python

   # List scripts
   scripts = client.scripts.scripts_list()

   # Create script metadata
   result = client.scripts.scripts_post(
       oid=123,
       name="initial-config"
   )

   # Update script metadata
   result = client.scripts.scripts_put(
       oid=123,
       name="initial-config-v2"
   )

   # Download script content
   content = client.scripts.scripts_get_content(oid=123)

   # Delete script
   client.scripts.scripts_delete(oid=123)

Manage FortiManagers
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # List FortiManager settings
   fortimanagers = client.fortimanagers.fortimanagers_list()

   # Add a FortiManager
   result = client.fortimanagers.fortimanagers_post(
       sn="FMG-VMTM23010656",
       ip="192.168.223.20"
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
