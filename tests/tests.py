import collector.utils.uid as UID

def __uid(length, characters):
        __length = UID.length
        __characters = UID.characters

        UID.length = length
        UID.characters = characters

        uid = UID.generate()

        UID.length = __length
        UID.characters = __characters

        return uid

def test_uid():
        __length = UID.length
        __characters = UID.characters

        uid = __uid(UID.length, UID.characters)

        assert len(uid) == UID.length

        for x in uid:
                assert x in UID.characters

        uid = __uid(128, UID.characters)

        assert len(uid) == 128

        for x in uid:
                assert x in UID.characters

        uid = __uid(UID.length, 'xX')

        assert len(uid) == UID.length

        for x in uid:
                assert x in 'xX'

        uid = __uid(128, 'xX')

        assert len(uid) == 128

        for x in uid:
                assert x in 'xX'

        assert __length == UID.length
        assert __characters == UID.characters

# Local Variables:
# indent-tabs-mode: nil
# End:
# exrc: ai et sw=4 ts=4
