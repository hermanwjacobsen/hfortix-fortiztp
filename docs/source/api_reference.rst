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

   client.api.
     ├── devices.
     │   ├── list()              # List devices
     │   ├── bulk_provision()    # Bulk operations
     │   ├── get()               # Get device details
     │   ├── update()            # Provision/unprovision
     │   └── firmware_profiles() # Get firmware profiles
     ├── scripts.
     │   ├── scripts_list()      # List scripts
     │   ├── scripts_post()      # Create script
     │   ├── scripts_get()       # Get script metadata
     │   ├── scripts_put()       # Update script
     │   ├── scripts_delete()    # Delete script
     │   ├── scripts_content_get()  # Download content
     │   └── scripts_content_put()  # Upload content
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
