.. Django Collector documentation master file, created by
   sphinx-quickstart on Thu Oct  6 12:00:52 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Collector's documentation!
============================================

Django Collector is a django application that is used to collect email
addresses. The typical use case is a start-up that is in the
pre-launch phase and wants to collect email addresses so that a launch
notice may be sent out.

Django Collector is unique in that is provides a mechanism for people
to delete their email addresses before the launch notice is sent out.

Full data portability at all times!

INSTALLATION
============

* Use the Software 6 PPA::

    sudo add-apt-repository ppa:software6/ppa
    sudo apt-get update
    sudo apt-get install python-django-collector

See also: https://launchpad.net/~software6/+archive/ppa

* Use the Cheese Shop::

    sudo pip install djang-collector

See also: http://pypi.python.org/pypi

SETTINGS
========

These settings are expected to appear in ``settings.py``.

* COLLECTOR_SEND_EMAIL

True or False. Default is False. Requires a working MTA. When True,
Django Collector will send an email with instructions on how to delete
the email address. This is as simple as clicking on a link in the
email.

* COLLECTOR_FROM_EMAIL

Default is the empty string. This email address will be used in the
``From:`` field. For example: ``webmaster@example.com``.

Each template may be localized. ``%s`` will be replaced by the user's
preferred language, e.g. ``es``.

For example, in settings.py::

    LANGUAGE_CODE = 'en'

    _ = lambda x: x

    LANGUAGES = (
        ('en', _(u'English')),
        ('es', _(u'Espanol')),
    )

means that English and Espanol are supported. English is the
default. Users that request other languages will get English.

* COLLECTOR_SUBJECT_TEMPLATE

Default is ``collector-subject.tmpl.%s``.

* COLLECTOR_MESSAGE_TEMPLATE

Default is ``collector-message.tmpl.%s``.

* COLLECTOR_DELETED_TEMPLATE

Default is ``collector-deleted.tmpl.%s``. This template will be
displayed when the user deletes her email address by clicking the link
in the email sent to her.

* COLLECTOR_BLOB404_TEMPLATE

Default is ``collector-blob404.tmpl.%s``. This template will be
displayed when the user attempts to delete an email address that has
already been deleted.

TEMPLATE VARIABLES
==================

These variables are made available to every template.

* COLLECTOR_URL

This is a fully-qualified, hard-to-guess, and unique URL that will
delete the associated email address when clicked. This is expected to
appear in the ``COLLECTOR_MESSAGE_TEMPLATE``.

Examples
========

Sites using Django Collector:

* http://lndlrd.com

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

