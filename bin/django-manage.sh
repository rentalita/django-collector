#!/bin/sh

LNDLRD_HOME="$(dirname $0)"/..
export LNDLRD_HOME

. "${LNDLRD_HOME}"/etc/common

"${LNDLRD_BIN}"/python.sh "${LNDLRD_BIN}"/django-manage.py "$@" -v 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
