Django Collector -- collects emails
===

Django Collector is a django application that is used to collect
emails. The typical use case is a start-up that is in the pre-launch
phase and wants to know whom they should send an email to when the
site launches.

Django Collector is unique in that is provides a mechanism for people
to delete their emails from the list of collected e-mails. Full data
portability at all times!

## BUILD

    ./build.sh

## TEST

    ./tests.sh

## REQUIREMENTS

 * [python 2.7](http://www.python.org/)
 * [python-setuptools 0.6](http://packages.python.org/distribute/)
 * [python-nose 1.0](http://code.google.com/p/python-nose/)
 * [python-django 1.3](http://www.djangoproject.com/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)
 * [python-pip 0.8](http://www.pip-installer.org/)

## SETTINGS

 * `COLLECTOR_SEND_EMAIL`

   True or False. Default is False. Requires a working MTA.

 * `COLLECTOR_FROM_EMAIL`

   Default is the empty string. For example "webmaster@example.com".

 * `COLLECTOR_SUBJECT_TEMPLATE`

   Default is 'collector-subject.tmpl.%s'.

 * `COLLECTOR_MESSAGE_TEMPLATE`

   Default is 'collector-message.tmpl.%s'.

 * `COLLECTOR_DELETED_TEMPLATE`

   Default is 'collector-deleted.tmpl.%s'.

 * `COLLECTOR_BLOB404_TEMPLATE`

   Default is 'collector-blob404.tmpl.%s'.

## TEMPLATE VARIABLES

 * `COLLECTOR_URL`

   This is a fully-qualified, hard-to-guess, and unique URL that will
   delete the associated email address when clicked. This is expected
   to appear in the `COLLECTOR_MESSAGE_TEMPLATE`.

## CONTRIBUTE

https://github.com/software6/django-collector

## LICENSE

Django Collector is brought to you by [Software
6](http://software6.net/) under the MIT License.
