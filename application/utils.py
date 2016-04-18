import string
import random

from application.models import Entry


def key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Random string generator.
    Some recursion for getting only unique keys.
    Method from http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    """

    key = ''.join(random.choice(chars) for _ in range(size))

    if not Entry.objects.filter(key=string).exists():
        return key
    else:
        key_generator(size, chars)
