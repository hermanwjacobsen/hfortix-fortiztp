CloudSession Integration
========================

FortiZTP integrates seamlessly with CloudSession for efficient multi-service OAuth management.

Basic Usage
-----------

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_fortiztp import FortiZTP

   with CloudSession(api_id="...", password="...") as session:
       client = FortiZTP(session=session)  # Auto-uses "fortiztp" client_id
       devices = client.devices.get()

Multi-Service Example
---------------------

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_forticare import FortiCare
   from hfortix_fortiztp import FortiZTP

   with CloudSession(api_id="...", password="...") as session:
       fc = FortiCare(session=session)    # Uses "assetmanagement"
       fz = FortiZTP(session=session)     # Uses "fortiztp"
       
       # Both share the session, each with their own token
       products = fc.api.products.list.post()
       devices = fz.devices.get()

Benefits
--------

* **Token sharing**: Efficient token reuse across services
* **Automatic refresh**: Tokens stay valid without manual intervention
* **Thread-safe**: Concurrent access from multiple services
* **Clean code**: Context manager handles cleanup

See Also
--------

* :doc:`ratelimit` - Rate limit tracking
* hfortix-core CloudSession documentation
