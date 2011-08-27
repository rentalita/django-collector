# -*- coding: utf-8 -*-

import json
import string

import django.db
from django.test.client import Client

import nose.tools

from collector.models import Blob
from collector.utils.http import JSONResponse201
import collector.utils.uid as UID

__UID_DEFAULT_NUMCHARS__ = 40
__UID_DEFAULT_USECHARS__ = string.ascii_letters + string.digits


def test_uid_defaults():
    assert UID.get_default_numchars() == \
        __UID_DEFAULT_NUMCHARS__

    assert UID.get_default_usechars() == \
        __UID_DEFAULT_USECHARS__


def test_uid_generate():
    uid = UID.generate()
    assert len(uid) == __UID_DEFAULT_NUMCHARS__
    for x in uid:
        assert x in __UID_DEFAULT_USECHARS__

    uid = UID.generate(numchars=128)
    assert len(uid) == 128
    for x in uid:
        assert x in __UID_DEFAULT_USECHARS__

    uid = UID.generate(usechars='xYz')
    assert len(uid) == __UID_DEFAULT_NUMCHARS__
    for x in uid:
        assert x in 'xYz'

    uid = UID.generate(numchars=128, usechars='xYz')
    assert len(uid) == 128
    for x in uid:
        assert x in 'xYz'


def test_uid_is_unique():
    count = {}

    for uid in [UID.generate() for i in range(1, 100)]:
        count[uid] = count.get(uid, 0) + 1

    for uid in count:
        assert count[uid] == 1


def test_json_response():
    response = JSONResponse201({'answer': 42})
    assert response.status == 201
    content = json.loads(response.content)
    assert content['answer'] == 42


def __blob_model(blob, email):
    blob = Blob.objects.get(email=email)

    assert blob.email == email
    assert blob.email == str(blob)

    blob.delete()
    Blob.objects.get(email=email)


@nose.tools.raises(Blob.DoesNotExist)
def test_blob_model():
    email = 'example@example.com'

    blob = Blob()

    assert len(blob.uid) > 0
    assert blob.email == ''

    blob.email = email
    blob.save()

    content = blob.to_json()
    assert content['email'] == email

    __blob_model(blob, email)


@nose.tools.raises(django.db.IntegrityError)
def test_blob_model_uid_is_unique():
    blob1 = Blob()
    blob2 = Blob()

    blob1.uid = blob2.uid = UID.generate()

    blob1.save()
    blob2.save()


@nose.tools.raises(Blob.DoesNotExist)
def test_create_view():
    client = Client()

    email = 'example@example.com'

    # Created
    rc = client.post('/collector/', {'collectorEmail': email})
    assert rc.status_code == 201

    blob = Blob.objects.get(email=email)

    __blob_model(blob, email)


def test_create_view_errors():
    client = Client()

    # Not Found
    rc = client.get('/collector')
    assert rc.status_code == 404

    # Method Not Allowed
    rc = client.get('/collector/')
    assert rc.status_code == 405

    # Not Found
    rc = client.post('/collector')
    assert rc.status_code == 404

    # Bad Request
    rc = client.post('/collector/')
    assert rc.status_code == 400

    # Bad Request
    rc = client.post('/collector/',
                     {'collectorEmail': 'example example.com'})
    assert rc.status_code == 400

    # Bad Request
    rc = client.post('/collector/',
                     {'collectorEmail': 'example@example com'})
    assert rc.status_code == 400

    # Bad Request
    rc = client.post('/collector/',
                     {'collectorEmail': 'example example com'})
    assert rc.status_code == 400


@nose.tools.raises(Blob.DoesNotExist)
def test_delete_view():
    client = Client()

    email = 'example@example.com'

    blob = Blob()
    blob.email = email
    blob.uid = 'xYz'
    blob.save()

    # Moved Temporarily
    rc = client.get('/collector/xYz/')
    assert rc.status_code == 302

    # Moved Temporarily
    rc = client.get('/collector/xYz/')
    assert rc.status_code == 302

    Blob.objects.get(email=email)


def test_delete_view_errors():
    client = Client()

    # Not Found
    rc = client.post('/collector/xYz')
    assert rc.status_code == 404

    # Method Not Allowed
    rc = client.post('/collector/xYz/')
    assert rc.status_code == 405

    # Not Found
    rc = client.get('/collector/xYz')
    assert rc.status_code == 404


def test_blob404_view():
    client = Client()

    # OK
    rc = client.get('/collector/blob404/')
    assert rc.status_code == 200


def test_blob404_view_errors():
    client = Client()

    # Not Found
    rc = client.post('/collector/blob404')
    assert rc.status_code == 404

    # Method Not Allowed
    rc = client.post('/collector/blob404/')
    assert rc.status_code == 405

    # Not Found
    rc = client.get('/collector/blob404')
    assert rc.status_code == 404


def test_deleted_view():
    client = Client()

    # OK
    rc = client.get('/collector/deleted/')
    assert rc.status_code == 200


def test_deleted_view_errors():
    client = Client()

    # Not Found
    rc = client.post('/collector/deleted')
    assert rc.status_code == 404

    # Method Not Allowed
    rc = client.post('/collector/deleted/')
    assert rc.status_code == 405

    # Not Found
    rc = client.get('/collector/deleted')
    assert rc.status_code == 404

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
