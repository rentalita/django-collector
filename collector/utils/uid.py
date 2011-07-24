import random
import string

length = 40

def generate():
        return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))
