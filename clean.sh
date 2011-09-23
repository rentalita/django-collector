#!/bin/sh

COLLECTOR_TESTS=
export COLLECTOR_TESTS

COLLECTOR_HOME="$(dirname $0)"
. "${COLLECTOR_HOME}"/etc/common

cd "${COLLECTOR_HOME}"

"${COLLECTOR_BIN}"/python.sh setup.py -q clean "$@"
[ $? != 0 ] && echo "ERROR!!!" && exit 1

find . -name "*~" | xargs rm -f
find . -name "*.pyc" | xargs rm -f

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
