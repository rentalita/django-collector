# -*- coding: utf-8 -*-


import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['COLLECTOR_DB'] + os.sep + 'tests.db',
    }
}

INSTALLED_APPS = ('collector',)

ROOT_URLCONF = 'collector.tests.urls'


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
