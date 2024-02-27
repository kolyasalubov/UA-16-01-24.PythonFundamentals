# Basic subclasses - Adam and Eve
# https://www.codewars.com/kata/547274e24481cfc469000416

class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        super().__init__()

class Woman(Human):
    def __init__(self):
        super().__init__()

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]
