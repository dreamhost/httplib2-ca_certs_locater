=================================
 httplib2.ca_certs_locater 0.1.0
=================================

.. tags:: python release

This package provides a plug-in to httplib2 to tell it to use the
certificate authority file from the base OS instead of the one in the
httplib2 package. The file from httplib2 is used as a fallback, if the
expected OS-specific file is not found.

What's New In This Release?
===========================

This is the first public release.

Installation
============

::

  $ pip install httplib2.ca_certs_locater

Supporting Additional Platforms
===============================

If you are on a platform with a different certificate authority file,
please submit a pull request via github_ to add the file to ``get()``.

.. _github: https://github.com/dreamhost/httplib2-ca_certs_locater

More Info
=========

For more details, see the README on github_.
