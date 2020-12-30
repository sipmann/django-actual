Scaffolding
===========

After installing and configuring the `django_actual` app, you can start scaffolding apps. First let's see the supported field types.

Field types
-----------

* char - CharField (default)
* text - TextField
* int - IntegerField
* decimal -DecimalField
* datetime - DateTimeField
* foreign - ForeignKey
* email - EmailField
* bool - BooleanField

To scaffold an app, you have the following syntax. Where you have an APPNAME (existing or not) and set the MODELNAME (must be a new one) followed by its fields.

.. code-block:: bash

    python manage.py scaffold APPNAME --model MODELNAME [fields]

The fields must follow a strict pattern. Must be FIELDNAME:TYPE. Each field type has its own extended properties like `max length`, `required`, and `digits|precision`. The `char` type is the default one, so you can just write the field name (see the example below). 

Two fields foreign and decimal requires additional parameters:

* "foreign" as the third argument takes foreign model, example:

.. code-block:: bash

    blog:foreign:Blog, post:foreign:Post, added_by:foreign:User

NOTICE: All foreign key models must already exist in the project. User and Group models are imported automatically.

* decimal field requires two more arguments `max_digits` and `decimal_places`, example:

.. code-block:: bash

    total_cost:decimal:10:2


* char field also have a length parameter on the third position

* all fields have a required as the last argument

.. code-block:: bash

    total_cost:deciman:10:2:True name:char:50:True

Example
-------

Let's create a simple forum app. We need Forum, Topic, and Post model.

Forum model
Forum model needs just one field name:

.. code-block:: bash

    python manage.py scaffold forum --model Forum name

Topic model
Topics are created by site users so we need: created_by, title and Forum foreign key (update_date and create_date are always added to models):

.. code-block:: bash

    python manage.py scaffold forum --model Topic created_by:foreign:User title forum:foreign:Forum

Post model
Last one are Posts. Posts are related to Topics. Here we need: title, body, created_by and foreign key to Topic:

.. code-block:: bash

    python manage.py scaffold forum --model Post title body:text created_by:foreign:User topic:foreign:Topic

All data should be in place!

Now you must add forum app to INSTALLED_APPS and include app in urls.py file by adding into urlpatterns:

.. code-block:: python
    :emphasize-lines: 3

    urlpatterns = [
        ...
        path('forum', include('forum.urls')),
    ]

Now syncdb new app and you are ready to go:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

Run your server:

.. code-block:: bash

    python manage.py runserver

And go to forum main page:

http://localhost:8000/forum/

All structures are in place. Now you can personalize models, templates and urls.

At the end you can test the new app by running test:

.. code-block:: bash

    python manage.py test forum

    Creating test database for alias 'default'...
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.884s

    OK

Happy scaffolding!