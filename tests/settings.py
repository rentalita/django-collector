DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.db',
    }
}

INSTALLED_APPS = ('collector',)

ROOT_URLCONF = 'tests.urls'


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
