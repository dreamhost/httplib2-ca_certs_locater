===========================
 httplib2.ca_certs_locater
===========================

This package provides a plug-in to httplib2 to tell it to use the
certificate authority file from the base OS instead of the one in the
httplib2 package. The file from httplib2 is used as a fallback, if the
expected OS-specific file is not found.

Installation
============

::

  $ pip install httplib2.ca_certs_locater

Supporting Additional Certificate Files
=======================================

If you are on a platform with a different certificate authority file,
please submit a pull request via github_ to add the file to ``get()``.

.. _github:: https://github.com/dreamhost/httplib2-ca_certs_locater
