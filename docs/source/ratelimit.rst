Rate Limit Tracking
===================

FortiZTP includes built-in rate limit tracking to monitor API usage.

Overview
--------

FortiZTP API enforces:

* **2000 calls per hour**

The tracking system monitors usage but does **not enforce** limits.

Basic Usage
-----------

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   client = FortiZTP(
       api_id="...",
       password="...",
       rate_limit_calls_per_hour=2000
   )

   devices = client.devices.get()
   status = client.get_rate_limit_status()

Status Response
---------------

.. code-block:: python

   {
       "calls_last_min": 10,
       "calls_last_5min": 45,
       "calls_last_hour": 180,
       "errors_last_min": 0,
       "errors_last_5min": 0,
       "errors_last_hour": 0,
       "total_calls": 523,
       "total_errors": 2,
       "limits": {
           "calls_per_min": None,
           "calls_per_5min": None,
           "calls_per_hour": 2000,
           "errors_per_min": None,
           "errors_per_5min": None,
           "errors_per_hour": None
       },
       "within_limits": True
   }

Monitoring Example
------------------

.. code-block:: python

   client = FortiZTP(
       api_id="...",
       password="...",
       rate_limit_calls_per_hour=2000
   )

   # Check before batch operation
   status = client.get_rate_limit_status()
   
   if status['calls_last_hour'] > 1800:
       print("Approaching hourly limit, waiting...")
       time.sleep(3600)  # Wait an hour
   
   # Continue with operations
   devices = client.devices.get()

Session-Wide Tracking
---------------------

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_forticare import FortiCare
   from hfortix_fortiztp import FortiZTP

   with CloudSession(api_id="...", password="...") as session:
       fc = FortiCare(session=session)
       fz = FortiZTP(session=session)
       
       # Per-client stats
       fz_status = fz.get_rate_limit_status()
       
       # Session-wide stats
       session_status = session.get_rate_limit_status()

See Also
--------

* :doc:`session` - CloudSession integration
* hfortix-core rate limiting documentation
