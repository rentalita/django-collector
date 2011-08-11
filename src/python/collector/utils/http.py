# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse


class JSONResponse(HttpResponse):

    mimetype = 'application/json'

    def __init__(self, data, *args, **kwargs):
        data = json.dumps(data)
        kwargs['mimetype'] = self.mimetype
        kwargs['status'] = self.status
        HttpResponse.__init__(self, data, *args, **kwargs)


class JSONResponse201(JSONResponse):

    status = 201

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
