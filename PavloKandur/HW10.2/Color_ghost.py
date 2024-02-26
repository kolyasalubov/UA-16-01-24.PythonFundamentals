from random import choice
class Ghost(object):
    colors = ["white", "red", "yellow", "purple"]
    def __init__(self):
        self.color = choice(Ghost.colors)