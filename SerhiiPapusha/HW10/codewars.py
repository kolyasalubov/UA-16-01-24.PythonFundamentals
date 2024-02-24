# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# 2. Color Ghost
import random
class Ghost(object):
    colors_list = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(Ghost.colors_list)

# 3. Basic subclasses - Adam and Eve
class Human(object):
        pass
class Man(Human):
       def __repr__(self):
            return "Adam"
class Woman(Human):
       def __repr__(self):
            return "Eve"
def God():
    man = Man()
    woman = Woman()
    list_people = [man, woman]
    return list_people

# 4. Classy Classes
class Person(object):
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
    def getInfo(self):
        return self.info
    
# 5. Building Spheres
    
import math
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)
        
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        volume = (4/3) * math.pi * math.pow(self.radius, 3)
        return volume
    def get_surface_area(self):
        surface_area = 4 * math.pi * math.pow(self.radius, 2)
        return surface_area
    def get_density(self):
        volume = self.get_volume()
        density = self.mass / volume
        return density
    
# 6. Dynamic Classes
    def class_name_changer(cls, new_name):
        if not (new_name[0].isupper() and new_name.isalnum()):
            raise ValueError("Invalid class name")
            
        cls.__name__ = new_name
        return cls.__name__