Welcome to Django Collector's documentation!
============================================

Django Collector is a django application that is used to collect email
addresses. The typical use case is a start-up that is in the
pre-launch phase and wants to collect email addresses so that a launch
notice may be sent out.

Django Collector is unique in that is provides a mechanism for people
to delete their email addresses before the launch notice is sent out.

Full data portability at all times!

Django Collector is all over teh internets...

* https://github.com/rentalita/django-collector
* https://launchpad.net/django-collector
* http://django-collector.rtfd.org
* http://pypi.python.org/pypi/django-collector
* http://djangopackages.com/packages/p/django-collector

INSTALLATION
============

* Use the Rentalita PPA::

    sudo add-apt-repository ppa:rentalita/ppa
    sudo apt-get update
    sudo apt-get install python-django-collector

See also: https://launchpad.net/~rentalita/+archive/ppa

* Use the Cheese Shop::

    sudo pip install djang-collector

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

Each template has been localized.

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

Default is ``collector/subject.txt``.

* COLLECTOR_MESSAGE_TEMPLATE

Default is ``collector/message.txt``.

* COLLECTOR_DELETED_TEMPLATE

Default is ``collector/deleted.html``. This template will be
displayed when the user deletes her email address by clicking the link
in the email sent to her.

* COLLECTOR_BLOB404_TEMPLATE

Default is ``collector/blob404.html``. This template will be
displayed when the user attempts to delete an email address that has
already been deleted.

TEMPLATE VARIABLES
==================

These variables are made available to every template.

* COLLECTOR_URL

This is a fully-qualified, hard-to-guess, and unique URL that will
delete the associated email address when clicked. This is expected to
appear in the ``COLLECTOR_MESSAGE_TEMPLATE``.

EXAMPLES
========

Sites using Django Collector:

* https://www.rentalita.com

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

