#!/bin/sh

COLLECTOR_HOME="$(dirname $0)"/..
export COLLECTOR_HOME

. "${COLLECTOR_HOME}"/etc/common

FILENAME="$1"

if [ "${FILENAME}" = "" ]; then
    FILENAME="${COLLECTOR_DATA}"/django-load.json
fi

"${COLLECTOR_BIN}"/django-manage.sh loaddata "${FILENAME}"

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
