import random
import string

__length = 40
__string = string.ascii_letters + string.digits


def get_default_length():
    return __length


def get_default_string():
    return __string


def generate(length=None, string=None):
    if not length:
        length = __length
    if not string:
        string = __string

    return ''.join(random.choice(string) for x in range(length))


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
