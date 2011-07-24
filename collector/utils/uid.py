import random
import string

length = 40
characters = string.ascii_letters + string.digits

def generate():
        return ''.join(random.choice(characters) for x in range(length))

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
