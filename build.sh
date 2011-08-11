#!/bin/sh

LNDLRD_HOME="$(dirname $0)"
. "${LNDLRD_HOME}"/etc/common

cd "${LNDLRD_HOME}"

if [ ! -f setup.cfg ]; then
        sed -e "s#\@prefix\@#${LNDLRD_HOME}#g;" setup.cfg.in > setup.cfg
fi

"${LNDLRD_BIN}"/python.sh setup.py -q develop
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
