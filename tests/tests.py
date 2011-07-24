import collector.utils.uid as UID

def test_uid():
        uid = UID.generate()
        assert len(uid) == UID.length

# Local Variables:
# indent-tabs-mode: nil
# End:
# exrc: ai et sw=4 ts=4
