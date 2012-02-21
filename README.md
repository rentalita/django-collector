Django Collector -- Collects email addresses.
===

## QUICK START

Please consult [The Django Collector
Documentation](http://django-collector.rtfd.org) to install and use
Django Collector. H@x0rs read on...

## BUILD

This runs `python setup.py develop` (more or less).

    ./build.sh

## TEST

This uses `nosetests` to run the unit tests, and enables the built-in
coverage report.

    ./tests.sh
    sensible-browser ./coverage/index.html

## INSTALL

 * Create a Debian/Ubuntu package:

        debuild -uc -us -i -I
        sudo dpkg -i ../python-django-collector*.deb

 * Link the source code under `${HOME}/.local`:

        PYTHONPATH=${HOME}/.local/lib/python27:${PYTHONPATH}
        export PYTHONPATH

        pip install --user -e .

## DEBUG

The layout used by Django Collector depends on that a particular
environment has been setup (see `etc/common`). For this reason several
wrapper scripts have been provided to help when working on the
command-line. For example:

    $ ./bin/python.sh
    >>> from collector.models import Blob
    >>> Blob.objects.all()

## REQUIREMENTS

As tested on [Ubuntu 11.04](http://ubuntu.com/). See also [Ubuntu
Setup](https://github.com/rentalita/ubuntu-setup).

 * [python 2.7](http://www.python.org/)
 * [python-setuptools 0.6](http://packages.python.org/distribute/)
 * [python-nose 1.0](http://code.google.com/p/python-nose/)
 * [python-coverage 3.4](http://nedbatchelder.com/code/coverage/)
 * [python-django 1.3](http://www.djangoproject.com/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)
 * [python-sphinx 1.0](http://sphinx.pocoo.org/)
 * [python-pip 0.8](http://www.pip-installer.org/)

## CONTRIBUTE

https://github.com/rentalita/django-collector

## LICENSE

Django Collector is brought to you by [Rentalita]
(http://rentalita.com/) under the MIT License.

## CREATED BY

https://github.com/rentalita/django-layout
