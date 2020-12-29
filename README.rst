=====================
django-actual-helpers
=====================

.. image:: https://img.shields.io/pypi/v/django-actual-helpers.svg
   :target: https://pypi.org/project/django-actual-helpers/

.. image:: https://img.shields.io/pypi/dm/django-actual-helpers   
    :alt: PyPI - Downloads

.. image:: https://readthedocs.org/projects/django-actual/badge/?version=latest
    :target: https://django-actual.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Overview
---------

This project is a follow up of the old project django-common from Tivix. The project served as a base to this one but it doesn't mean that we'll keep things like it was before.

Django-actual consists of the following things:

	- A middleware that makes sure your web-app runs either on or without 'www' in the domain.

	- A ``SessionManagerBase`` base class, that helps in keeping your session related  code object-oriented and clean! See session.py for usage details.

	- An ``EmailBackend`` for authenticating users based on their email, apart from username.

	- Some custom db fields that you can use in your models including a ``UniqueHashField`` and ``RandomHashField``.

	- Bunch of helpful functions in helper.py

	- A ``render_form_field`` template tag that makes rendering form fields easy and DRY.

	- A dry response class: ``XMLResponse`` in the django_actual.http that can be used in views that give xml responses.


Installation
-------------

- Install django_actual (ideally in your virtualenv!) using pip or simply getting a copy of the code and putting it in a directory in your codebase.

- Add ``django_actual`` to your Django settings ``INSTALLED_APPS``::

	INSTALLED_APPS = [
        # ...
        "django_actual",
    ]

- Add the following to your settings.py with appropriate values:

	- IS_DEV
	- IS_PROD
	- DOMAIN_NAME
	- WWW_ROOT

- Add ``common_settings`` to your Django settings ``TEMPLATE_CONTEXT_PROCESSORS``::

	TEMPLATE_CONTEXT_PROCESSORS = [
		# ...
		'django_actual.context_processors.common_settings',
	]

- Add ``EmailBackend`` to the Django settings ``AUTHENTICATION_BACKENDS``::

	AUTHENTICATION_BACKENDS = (
		'django_actual.auth_backends.EmailBackend',
		'django.contrib.auth.backends.ModelBackend'
	)

- Add ``WWWRedirectMiddleware`` if required to the list of middlewares::

	MIDDLEWARE_CLASSES = [
		# ...
		"WWWRedirectMiddleware",
	]

Scaffolding feature
-------------------

1. Installing

To get scaffold install it through pip with ``pip install django-actual-helpers`` and add ``django_actual`` to the INSTALLED_APPS.

Default is set to main app directory. However if you use django_base_project you must set up this to ``SCAFFOLD_APPS_DIR = 'apps/'``.

2. Run

To run scaffold type::

    python manage.py scaffold APPNAME --model MODELNAME [fields]

APPNAME is app name. If app does not exists it will be created.
MODELNAME is model name. Just enter model name that you want to create (for example: Blog, Topic, Post etc). It must be alphanumerical. Only one model per run is allowed!

[fields] - list of the model fields.

3. Field types

Available fields::

    char - CharField (default)
    text - TextField
    int - IntegerField
    decimal -DecimalField
    datetime - DateTimeField
    foreign - ForeignKey
    email - EmailField
    bool - BooleanField

All fields requires name that is provided before ``:`` sign, for example::

    title  body:text posts:int create_date:datetime

Two fields ``foreign`` and ``decimal`` requires additional parameters:

- "foreign" as third argument takes foreignkey model, example::

    blog:foreign:Blog, post:foreign:Post, added_by:foreign:User

NOTICE: All foreign key models must already exist in project. User and Group model are imported automatically.

- decimal field requires two more arguments ``max_digits`` and ``decimal_places``, example::

    total_cost:decimal:10:2

- char field also have a length parameter on the third position

- all fields have a required as the last argument

    total_cost:deciman:10:2:True
    name:char:50:True

NOTICE: To all models scaffold automatically adds two fields: update_date and create_date.

4. How it works?

Scaffold creates models, views (CRUD), forms, templates, admin, urls and basic tests (CRUD). Scaffold templates are using two blocks extending from base.html::

    {% extends "base.html" %}
    {% block page-title %} {% endblock %}
    {% block content %} {% endblock %}

So be sure you have your base.html set up properly.

Scaffolding example usage
-------------------------

Let's create simple ``forum`` app. We need ``Forum``, ``Topic`` and ``Post`` model.

- Forum model

Forum model needs just one field ``name``::

    python manage.py scaffold forum --model Forum name

- Topic model

Topics are created by site users so we need: ``created_by``, ``title`` and ``Forum`` foreign key (``update_date`` and ``create_date`` are always added to models)::

    python manage.py scaffold forum --model Topic created_by:foreign:User title forum:foreign:Forum

- Post model

Last one are Posts. Posts are related to Topics. Here we need: ``title``, ``body``, ``created_by`` and foreign key to ``Topic``::

    python manage.py scaffold forum --model Post title body:text created_by:foreign:User topic:foreign:Topic

All data should be in place!

Now you must add ``forum`` app to ``INSTALLED_APPS`` and include app in ``urls.py`` file by adding into urlpatterns::

    urlpatterns = [
        ...
        path('forum', include('forum.urls')),
    ]

Now syncdb new app and you are ready to go::

    python manage.py makemigrations
    python manage.py migrate

Run your server::

    python manage.py runserver

And go to forum main page::

    http://localhost:8000/forum/

All structure are in place. Now you can personalize models, templates and urls.

At the end you can test new app by runing test::

    python manage.py test forum

    Creating test database for alias 'default'...
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.884s

    OK

Happy scaffolding!

Generation of SECRET_KEY
------------------------

Sometimes you need to generate a new ``SECRET_KEY`` so now you can generate it using this command:

    $ python manage.py generate_secret_key

Sample output:

    $ python manage.py generate_secret_key

    SECRET_KEY: 7,=_3t?n@'wV=p`ITIA6"CUgJReZf?s:\`f~Jtl#2i=i^z%rCp-


Optional arguments

1. ``--length`` - is the length of the key ``default=50``
2. ``--alphabet`` - is the alphabet to use to generate the key ``default=ascii letters + punctuation symbols``

Django settings keys
--------------------

- DOMAIN_NAME - Domain name, ``"www.example.com"``
- WWW_ROOT - Root website url, ``"https://www.example.com/"``
- IS_DEV - Current environment is development environment
- IS_PROD - Current environment is production environment


This open-source app is brought to you by Sipmann, Inc. ( http://sipmann.com/ )


Changelog
=========

0.9.3
------
    - Changed the minimum Django version to 3.X. Version 2 might work (but not tested)
    - Removed unused things
    - Add __str__ to generated models
    - Bootstrap layout to the templates