#!/bin/sh -e

COLLECTOR_HOME="$(dirname $0)"
export COLLECTOR_HOME

PYTHONPATH="${COLLECTOR_HOME}":"${PYTHONPATH}"
export PYTHONPATH

DJANGO_SETTINGS_MODULE=tests.settings
export DJANGO_SETTINGS_MODULE

nosetests --with-coverage --cover-html "$@"
