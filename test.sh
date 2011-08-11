#!/bin/sh

LNDLRD_HOME="$(dirname $0)"
. "${LNDLRD_HOME}"/etc/common

cd "${LNDLRD_HOME}"

"${LNDLRD_BIN}"/nosetests.sh
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
