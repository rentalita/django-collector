#!/bin/sh

COLLECTOR_HOME="$(dirname $0)"/..
export COLLECTOR_HOME

. "${COLLECTOR_HOME}"/etc/common

"${COLLECTOR_BIN}"/python.sh "${COLLECTOR_BIN}"/django-manage.py "$@" --settings="${DJANGO_SETTINGS_MODULE}" -v 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
