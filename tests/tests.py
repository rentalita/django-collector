import string

from collector.models import Blob
import collector.utils.uid as UID

import django.db
from django.test.client import Client

import nose.tools

uid_default_length = 40
uid_default_string = string.ascii_letters + string.digits


def test_uid_defaults():
        assert UID.get_default_length() == \
            uid_default_length

        assert UID.get_default_string() == \
            uid_default_string


def test_uid_generate():
        uid = UID.generate()
        assert len(uid) == uid_default_length
        for x in uid:
                assert x in uid_default_string

        uid = UID.generate(length=128)
        assert len(uid) == 128
        for x in uid:
                assert x in uid_default_string

        uid = UID.generate(string='xYz')
        assert len(uid) == uid_default_length
        for x in uid:
                assert x in 'xYz'

        uid = UID.generate(length=128, string='xYz')
        assert len(uid) == 128
        for x in uid:
                assert x in 'xYz'


def test_uid_is_unique():
        count = {}

        for uid in [UID.generate() for i in range(1, 100)]:
                count[uid] = count.get(uid, 0) + 1

        for uid in count:
                assert count[uid] == 1


@nose.tools.raises(django.db.IntegrityError)
def test_blob_model_uid_is_unique():
        blob1 = Blob()
        blob2 = Blob()

        blob1.uid = blob2.uid = UID.generate()

        blob1.save()
        blob2.save()


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

        __blob_model(blob, email)


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

        # Moved Permanently
        rc = client.get('/collector')
        assert rc.status_code == 301

        # Method Not Allowed
        rc = client.get('/collector/')
        assert rc.status_code == 405

        # Moved Permanently
        rc = client.post('/collector')
        assert rc.status_code == 301

        # Bad Request
        rc = client.post('/collector/')
        assert rc.status_code == 400

        # Bad Request
        rc = client.post('/collector/', {'collectorEmail': 'example example.com'})
        assert rc.status_code == 400

        # Bad Request
        rc = client.post('/collector/', {'collectorEmail': 'example@example com'})
        assert rc.status_code == 400

        # Bad Request
        rc = client.post('/collector/', {'collectorEmail': 'example example com'})
        assert rc.status_code == 400


@nose.tools.raises(Blob.DoesNotExist)
def test_delete_view():
        client = Client()

        email = 'example@example.com'

        blob = Blob()
        blob.email = email
        blob.uid = 'xYz'
        blob.save()

        # No Content
        rc = client.get('/collector/xYz/')
        assert rc.status_code == 204

        # Not Found
        rc = client.get('/collector/xYz/')
        assert rc.status_code == 404

        Blob.objects.get(email=email)


def test_delete_view_errors():
        client = Client()

        # Moved Permanently
        rc = client.post('/collector/xYz')
        assert rc.status_code == 301

        # Method Not Allowed
        rc = client.post('/collector/xYz/')
        assert rc.status_code == 405

        # Moved Permanently
        rc = client.get('/collector/xYz')
        assert rc.status_code == 301

        # Not Found
        rc = client.get('/collector/xYz/')
        assert rc.status_code == 404


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
