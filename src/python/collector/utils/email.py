# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(request, blob):
    try:
        if not settings.COLLECTOR_SEND_EMAIL:
            return
    except:
        return

    try:
        sender = settings.COLLECTOR_FROM_EMAIL
    except:
        sender = ''

    try:
        subject_tmpl = settings.COLLECTOR_SUBJECT_TEMPLATE
    except:
        subject_tmpl = 'collector/subject.txt'

    try:
        message_tmpl = settings.COLLECTOR_MESSAGE_TEMPLATE
    except:
        message_tmpl = 'collector/message.txt'

    collector_url = request.build_absolute_uri(blob.uid + '/')

    subject = render_to_string(subject_tmpl)
    message = render_to_string(message_tmpl,
                               {'COLLECTOR_URL': collector_url})

    send_mail(subject.strip(), message, sender, [blob.email],
              fail_silently=False)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
