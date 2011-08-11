#!/bin/sh

LNDLRD_HOME="$(dirname $0)"/..
export LNDLRD_HOME

. "${LNDLRD_HOME}"/etc/common

"${SQLITE3}" ${SQLITE3FLAGS} ${LNDLRD_SQLITE3FLAGS} "$@"

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
