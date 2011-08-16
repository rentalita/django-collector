# -*- coding: utf-8 -*-

from collector.settings import *

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['COLLECTOR_DB'] + os.sep + 'tests.db',
    }
}

ROOT_URLCONF = 'collector.tests.urls'

INSTALLED_APPS = ('collector',)

COLLECTOR_SEND_EMAIL = True

EMAIL_HOST = 'localhost'
EMAIL_PORT = 8025

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
