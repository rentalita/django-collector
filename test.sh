#!/bin/sh

COLLECTOR_TESTS=1
export COLLECTOR_TESTS

COLLECTOR_HOME="$(dirname $0)"
. "${COLLECTOR_HOME}"/etc/common

cd "${COLLECTOR_HOME}"

django-admin syncdb -v 0

"${COLLECTOR_BIN}"/nosetests.sh
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
