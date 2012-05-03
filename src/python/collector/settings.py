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
    'django.template.loaders.app_directories.Loader',
    )

LANGUAGE_CODE = 'en'

_ = lambda x: x

LANGUAGES = (
    ('en', _(u'English')),
    ('es', _(u'Espanol')),
    )

APPEND_SLASH = False

INSTALLED_APPS = ('collector',)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
