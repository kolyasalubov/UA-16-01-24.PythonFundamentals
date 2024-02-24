import random


class Ghost:
    def __init__(self):
        self.colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(self.colors)
