#!/bin/sh -e

COLLECTOR_HOME="$(dirname $0)"
export COLLECTOR_HOME

PYTHONPATH="${COLLECTOR_HOME}":"${PYTHONPATH}"
export PYTHONPATH

DJANGO_SETTINGS_MODULE=tests.settings
export DJANGO_SETTINGS_MODULE

django-admin syncdb -v 0

nosetests --with-coverage --cover-html --cover-package=collector "$@"
