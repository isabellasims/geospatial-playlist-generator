import random
import string

class GroupCode:
    """Generates randomized alphanumeric code of length 6 by default. 
    Length can be overwritten by passing in integer argument of different
    value to build method."""
    
    def __init__(self):
        pass
        
    def build(self, length=6):
        chars=(string.ascii_uppercase+string.digits)
        return ''.join(random.choice(chars) for _ in range(length))
