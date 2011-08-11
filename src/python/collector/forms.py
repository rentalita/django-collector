# -*- coding: utf-8 -*-

from django.forms import Form, EmailField


class CollectorForm(Form):
    collectorEmail = EmailField()

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
