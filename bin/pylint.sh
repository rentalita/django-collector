#!/bin/sh

COLLECTOR_HOME="$(dirname $0)"/..
export COLLECTOR_HOME

. "${COLLECTOR_HOME}"/etc/common

"${COLLECTOR_BIN}"/python.sh "${PYLINT}" ${PYLINTFLAGS} ${COLLECTOR_PYLINTFLAGS} "$@"

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
