from django.db import models

import collector.utils.uid as UID


class Blob(models.Model):
    uid = models.CharField(max_length=UID.length, unique=True,
                           default=UID.generate)
    email = models.EmailField(max_length=128, unique=False)


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
