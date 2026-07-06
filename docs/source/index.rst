HFortix-FortiZTP Documentation
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   overview
   quickstart
   session
   ratelimit
   api_reference

Installation
------------

.. code-block:: bash

   pip install hfortix-fortiztp

Quick Start
-----------

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   # Initialize client
   client = FortiZTP(
       api_id="your_api_id",
       password="your_password"
   )

   # List devices
   devices = client.devices.list()

   # Clean up
   client.logout()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
