# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from collector.forms import CollectorForm
from collector.models import Blob
from collector.utils.http import JSONResponse201


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
        subject_tmpl = 'collector-subject.tmpl.%s'

    try:
        message_tmpl = settings.COLLECTOR_MESSAGE_TEMPLATE
    except:
        message_tmpl = 'collector-message.tmpl.%s'

    collector_url = request.build_absolute_uri(blob.uid + '/')

    subject = render_to_string(subject_tmpl % (request.LANGUAGE_CODE))
    message = render_to_string(message_tmpl % (request.LANGUAGE_CODE),
                               {'COLLECTOR_URL': collector_url})

    send_mail(subject.rstrip(), message, sender, [blob.email],
              fail_silently=False)


@require_http_methods(['POST'])
def create(request):
    form = CollectorForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    data = form.cleaned_data

    blob = Blob()
    blob.email = data['collectorEmail']

    blob.save()

    send_email(request, blob)

    return JSONResponse201(blob.to_json())


@require_http_methods(['GET'])
def delete(request, uid):
    try:
        blob = Blob.objects.get(uid=uid)
    except Blob.DoesNotExist:
        return HttpResponse(status=404)

    blob.delete()

    return HttpResponse(status=204)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
