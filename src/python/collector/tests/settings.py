# -*- coding: utf-8 -*-

from collector.settings import *

import os
import random

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['COLLECTOR_DB'] + os.sep + 'tests.db',
    }
}

ROOT_URLCONF = 'collector.tests.urls'

EMAIL_HOST = 'localhost'
EMAIL_PORT = random.randint(1025, 9999)

COLLECTOR_SEND_EMAIL = True

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
