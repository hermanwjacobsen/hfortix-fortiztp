API Reference
=============

FortiZTP Client
---------------

.. autoclass:: hfortix_fortiztp.FortiZTP
   :members:
   :undoc-members:
   :show-inheritance:

API Structure
-------------

.. code-block:: python

   client.api.        # client.<category> is an alias for client.api.<category>
     ├── devices.
     │   ├── list()              # List devices (filter by status/type/SN)
     │   ├── get()               # Get device details by serial number
     │   ├── put()               # Provision/unprovision single device
     │   ├── put_bulk()          # Bulk provision/unprovision
     │   └── regions.firmwareprofiles.get()  # Get firmware profiles
     ├── scripts.
     │   ├── scripts_list()      # List scripts
     │   ├── scripts_post()      # Create script metadata
     │   ├── scripts_get()       # Get script metadata
     │   ├── scripts_put()       # Update script metadata
     │   ├── scripts_delete()    # Delete script
     │   ├── scripts_get_content()  # Download content
     │   └── scripts_put_content()  # Upload content
     ├── fortimanagers.
     │   ├── fortimanagers_list() # List FortiManagers
     │   ├── fortimanagers_post() # Create config
     │   ├── fortimanagers_get()  # Get details
     │   ├── fortimanagers_put()  # Update config
     │   └── fortimanagers_delete() # Delete config
     └── system.
         └── system_get()        # Get system status

Response Models
---------------

.. autoclass:: hfortix_fortiztp.FortiZTPResponse
   :members:
   :undoc-members:
   :show-inheritance:

Type Definitions
----------------

.. autoclass:: hfortix_fortiztp.types.DeviceV2Data
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_fortiztp.types.ScriptMetaData
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_fortiztp.types.FortiManagerMetaData
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_fortiztp.types.SystemData
   :members:
   :undoc-members:
   :show-inheritance:

Enums
-----

.. autoclass:: hfortix_fortiztp.types.DeviceType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_fortiztp.types.ProvisionStatus
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_fortiztp.types.ProvisionTarget
   :members:
   :undoc-members:
   :show-inheritance:
