#!/bin/sh

COLLECTOR_TESTS=
export COLLECTOR_TESTS

COLLECTOR_HOME="$(dirname $0)"
. "${COLLECTOR_HOME}"/etc/common

cd "${COLLECTOR_HOME}"

TARGET="$@"
TARGET="${TARGET:-develop}"

"${COLLECTOR_BIN}"/python.sh setup.py -q ${TARGET}
[ $? != 0 ] && echo "ERROR!!!" && exit 1

"${COLLECTOR_BIN}"/django-migrate.sh

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
