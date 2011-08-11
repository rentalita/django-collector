# -*- coding: utf-8 -*-

from django.db import models

import collector.utils.uid as UID

__UID_NUMCHARS__ = UID.get_default_numchars()


class Blob(models.Model):
    uid = models.CharField(max_length=__UID_NUMCHARS__, unique=True,
                           default=UID.generate)
    email = models.EmailField(max_length=128, unique=False)

    def to_json(self):
        return {'uid': self.uid, 'email': self.email}

    def __unicode__(self):
        return self.email

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
