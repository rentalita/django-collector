import random
import string

from django.db import models

class UID:

        length = 40

        @classmethod
        def generate(klass):
                return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(klass.length))

class Blob(models.Model):
        uid = models.CharField(default=UID.generate, max_length=UID.length)
        email = models.EmailField(max_length=128)
