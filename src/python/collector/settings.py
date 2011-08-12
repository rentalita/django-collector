# -*- coding: utf-8 -*-

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['COLLECTOR_DB'] + os.sep + 'collector.db',
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DIRS = (
    os.environ['COLLECTOR_WWW'] + '/templates/',
)

LANGUAGE_CODE = 'en'

_ = lambda x: x

LANGUAGES = (
    ('en', _(u'English')),
    ('es', _(u'Español')),
)

APPEND_SLASH = False

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
