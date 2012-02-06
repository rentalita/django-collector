# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('collector.views',
    url(r'^blob404/$', 'blob404'),
    url(r'^deleted/$', 'deleted'),
    url(r'^$', 'create'),
    url(r'^(?P<uid>\w+)/$', 'delete'),
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
