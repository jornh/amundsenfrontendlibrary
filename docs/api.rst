.. _api:

Developer Interface
===================

Rest endpointz
--------------

Overview:

.. qrefflask:: amundsen_application.wsgi:app
   :undoc-static:


Longer:


.. autoflask:: amundsen_application.wsgi:app
   :undoc-static:







API metadata
------------

.. amundsen_application:



.. automodule:: amundsen_application.api.metadata.v0
   :inherited-members:




.. module:: amundsen_application

the whole thing TODO 

API exposed to the React app ......

autofunction
------------

.. autofunction:: amundsen_application.api.metadata.v0.popular_tables

pointing to a class   :class:`LocalConfig <amundsen_application.config.LocalConfig>` 


## from Sphinx Auto summary https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

.. currentmodule:: amundsen_application.api

.. autosummary::

   metadata.v0
   metadata.v0.popular_tables
   metadata.v0.get_table_metadata
   metadata.v0.update_table_owner
   metadata.v0.get_last_indexed
   metadata.v0.get_table_description
   metadata.v0.get_column_description
   metadata.v0.put_column_description
   metadata.v0.get_tags
   metadata.v0.update_table_tags
   metadata.v0.get_user
   search.v0
   search.v0


API metadata
------------

xxxx.. amundsen_application:

xxxx.. automodule:: amundsen_application.api.metadata.v0
xxxx   :inherited-members:




LocalConfig
-----------

.. amundsen_application.config:

.. currentmodule:: amundsen_application.config

.. autoclass:: Config
   :inherited-members:


.. autoclass:: LocalConfig
   :inherited-members:




Kennethreitz
============


.. module:: requests

This part of the documentation covers all the interfaces of Requests. For
parts where Requests depends on external libraries, we document the most
important right here and provide links to the canonical documentation.


Main Interface
--------------

All of Requests' functionality can be accessed by these 7 methods.
They all return an instance of the :class:`Response <Response>` object.

.. autofunction:: request

.. autofunction:: head
.. autofunction:: get
.. autofunction:: post
.. autofunction:: put
.. autofunction:: patch
.. autofunction:: delete

Exceptions
----------

.. autoexception:: requests.RequestException
.. autoexception:: requests.ConnectionError
.. autoexception:: requests.HTTPError
.. autoexception:: requests.URLRequired
.. autoexception:: requests.TooManyRedirects
.. autoexception:: requests.ConnectTimeout
.. autoexception:: requests.ReadTimeout
.. autoexception:: requests.Timeout

Request Sessions
----------------

.. _sessionapi:

.. autoclass:: Session
   :inherited-members: