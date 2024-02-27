# Color Ghost
# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])
