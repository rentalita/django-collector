from django.db import models

import collector.utils.uid as UID

class Blob(models.Model):
        uid = models.CharField(default=UID.generate, max_length=UID.length)
        email = models.EmailField(max_length=128)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
