# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render_to_response
from django.views.decorators.http import require_http_methods

from collector.forms import CollectorForm
from collector.models import Blob
from collector.utils.email import send_email
from collector.utils.http import JSONResponse201


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
        raise Http404

    blob.delete()

    return redirect(deleted)


@require_http_methods(['GET'])
def deleted(request):
    try:
        deleted_tmpl = settings.COLLECTOR_DELETED_TEMPLATE
    except:
        deleted_tmpl = 'collector-deleted.tmpl.%s'

    return render_to_response(deleted_tmpl % (request.LANGUAGE_CODE))

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
