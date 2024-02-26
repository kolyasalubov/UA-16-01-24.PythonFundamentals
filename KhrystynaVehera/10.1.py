class Ball():
    def __init__(self, type = "regular"):
        self.ball_type = type


import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])        




def God():
    return [Man(), Woman()]
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass
#code       















class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"











from math import pi
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return (4 / 3) * pi * (self.radius ** 3)
    
    def get_surface_area(self):
        return 4  * pi * (self.radius ** 2)
    
    def get_density(self):
        return self.mass / self.get_volume()






def class_name_changer(self, name):
    if name[0].isupper() and name.isalnum():
        self.__name__ = name
    else:
        return Error