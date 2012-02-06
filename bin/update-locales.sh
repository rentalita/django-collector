#!/bin/sh

COLLECTOR_HOME="$(dirname $0)"/..
export COLLECTOR_HOME

. "${COLLECTOR_HOME}"/etc/common

LOCALES="es"

for locale in ${LOCALES}; do
    (
        cd "${COLLECTOR_SRC}"/python/collector
        "${COLLECTOR_BIN}"/django-manage.sh makemessages -l "${locale}" -e .html -e .txt -e .js
        "${COLLECTOR_BIN}"/django-manage.sh compilemessages -l "${locale}"
    )
done

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
