#!/bin/sh

LNDLRD_HOME="$(dirname $0)"
. "${LNDLRD_HOME}"/etc/common

cd "${LNDLRD_HOME}"

"${LNDLRD_BIN}"/python.sh setup.py -q clean
[ $? != 0 ] && echo "ERROR!!!" && exit 1

find . -name "*~" | xargs rm -f
find . -name "*.pyc" | xargs rm -f
rm -f .coverage setup.py
rm -f "${LNDLRD_LIB}"/python/*

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
