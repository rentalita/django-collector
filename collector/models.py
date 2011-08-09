from django.db import models

import collector.utils.uid as UID

uid_length = UID.get_default_length()


class Blob(models.Model):
    uid = models.CharField(max_length=uid_length, unique=True,
                           default=UID.generate)
    email = models.EmailField(max_length=128, unique=False)

    def __unicode__(self):
        return self.email

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
