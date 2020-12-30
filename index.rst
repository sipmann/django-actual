.. Django Actual documentation master file, created by
   sphinx-quickstart on Tue Dec 29 07:01:24 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Actual's documentation!
=========================================


Overview
--------

This project is a follow up of the old project django-common from Tivix. The project served as a base to this one but it doesn't mean that we'll keep things like it was before.

Django-actual consists of the following things:

   * A middleware that makes sure your web-app runs either on or without 'www' in the domain.
   * A SessionManagerBase base class, that helps in keeping your session related code object-oriented and clean! See session.py for usage details.
   * An EmailBackend for authenticating users based on their email, apart from username.
   * Some custom db fields that you can use in your models including a UniqueHashField and RandomHashField.
   * Bunch of helpful functions in helper.py
   * A render_form_field template tag that makes rendering form fields easy and DRY.
   * A dry response class: XMLResponse in the django_actual.http that can be used in views that give xml responses.

Installation
-------------

First run the pip install command like the following

.. code-block:: bash

   pip install django-actual-helpers

Then add the `django_actual` app to your `INSTALLED_APPS` inside django `settings.py`.

.. toctree::
   :maxdepth: 3
   :caption: Topics:

   scaffold
   license
   help



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
