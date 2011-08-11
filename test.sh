#!/bin/sh

COLLECTOR_HOME="$(dirname $0)"
. "${COLLECTOR_HOME}"/etc/common

cd "${COLLECTOR_HOME}"

DJANGO_SETTINGS_MODULE=tests.settings
export DJANGO_SETTINGS_MODULE

django-admin syncdb -v 0

"${COLLECTOR_BIN}"/nosetests.sh
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
