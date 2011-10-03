Django Collector -- Collects email addresses.
===

Django Collector is a django application that is used to collect email
addresses. The typical use case is a start-up that is in the
pre-launch phase and wants to collect email addresses so that a launch
notice may be sent out.

Django Collector is unique in that is provides a mechanism for people
to delete their email addresses before the launch notice is sent out.

Full data portability at all times!

## BUILD

This runs `python setup.py develop` (more or less).

    ./build.sh

## TEST

This uses `nosetests` to run the unit tests, and enables the built-in
coverage report.

    ./tests.sh
    sensible-browser ./src/python/collector/cover/index.html

The unit test results should look like:

    ..............
    Name                    Stmts   Exec  Cover   Missing
    -----------------------------------------------------
    collector                   1      1   100%
    collector.forms             3      3   100%
    collector.models           10     10   100%
    collector.settings          9      9   100%
    collector.urls              2      2   100%
    collector.utils             1      1   100%
    collector.utils.email      25     22    88%   11-13
    collector.utils.http       11     11   100%
    collector.utils.uid        14     14   100%
    collector.views            37     37   100%
    -----------------------------------------------------
    TOTAL                     113    110    97%
    ----------------------------------------------------------------------
    Ran 14 tests in 1.427s

    OK

## INSTALL (suggested)

    pip install --user -e .

## REQUIREMENTS

As tested on [Ubuntu 11.04](http://ubuntu.com/). See also [Ubuntu
Setup](https://github.com/software6/ubuntu-setup)

 * [python 2.7](http://www.python.org/)
 * [python-setuptools 0.6](http://packages.python.org/distribute/)
 * [python-nose 1.0](http://code.google.com/p/python-nose/)
 * [python-coverage 3.4](http://nedbatchelder.com/code/coverage/)
 * [python-django 1.3](http://www.djangoproject.com/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)
 * [python-pip 0.8](http://www.pip-installer.org/)

## SETTINGS

 * `COLLECTOR_SEND_EMAIL`

   True or False. Default is False. Requires a working MTA. When True,
   Django Collector will send an email with instructions on how to
   delete the email address. This is as simple as clicking on a link
   in the email.

 * `COLLECTOR_FROM_EMAIL`

   Default is the empty string. This email address will be used in the
   From: field. For example `webmaster@example.com`.

#### TEMPLATE SETTINGS

 Each template may be localized. `%s` will be replaced by the user's
 preferred language, e.g. `es`.

 For example, in settings.py:

    LANGUAGE_CODE = 'en'

    _ = lambda x: x

    LANGUAGES = (
        ('en', _(u'English')),
        ('es', _(u'Espanol')),
    )

 means that English and Español are supported. English is the
 default. Users that request other languages will get English.

 * `COLLECTOR_SUBJECT_TEMPLATE`

   Default is `collector-subject.tmpl.%s`.

 * `COLLECTOR_MESSAGE_TEMPLATE`

   Default is `collector-message.tmpl.%s`.

 * `COLLECTOR_DELETED_TEMPLATE`

   Default is `collector-deleted.tmpl.%s`. This template will be
   displayed when the user deletes her email address by clicking the
   link in the email sent to her.

 * `COLLECTOR_BLOB404_TEMPLATE`

   Default is `collector-blob404.tmpl.%s`. This template will be
   displayed when the user attempts to delete an email address that
   has already been deleted.

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

## CREATED BY

https://github.com/software6/django-layout
