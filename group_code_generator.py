import random
import string

def group_id(size=6, chars=(string.ascii_uppercase+string.digits)):
    """This function returns a randomized alphanumeric code of length 6. Length can be
    overwritten by passing in integer argument of different value."""
    return ''.join(random.choice(chars) for _ in range(size))