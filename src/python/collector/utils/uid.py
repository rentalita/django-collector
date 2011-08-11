# -*- coding: utf-8 -*-

import random
import string

__NUMCHARS__ = 40
__USECHARS__ = string.ascii_letters + string.digits


def get_default_numchars():
    return __NUMCHARS__


def get_default_usechars():
    return __USECHARS__


def generate(numchars=None, usechars=None):
    if not numchars:
        numchars = __NUMCHARS__
    if not usechars:
        usechars = __USECHARS__

    return ''.join(random.choice(usechars) for x in range(numchars))

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
