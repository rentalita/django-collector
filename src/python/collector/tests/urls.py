# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

import collector.urls

urlpatterns = patterns('',
    url(r'^collector/', include(collector.urls)),
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
