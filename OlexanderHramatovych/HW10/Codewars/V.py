import math
from math import pi,pow


class Sphere(object):
        def __init__(self,radius:float,mass:float):
            self.radius = radius
            self.mass = mass
        def get_radius(self):
            return self.radius
        def get_mass(self):
            return self.mass
        def get_volume(self):
            return round(4/3 * pi * pow(self.radius, 3),5)
        def get_surface_area(self):
            return round((4*pi)*(2*self.radius),5)
        def get_density(self):
            return round(self.mass / (4/3 * pi * pow(self.radius, 3)),5)
        

ball = Sphere(2,50)
print(ball.get_radius() )
print(ball.get_mass() )
print(ball.get_volume() )
print(ball.get_surface_area() )
print(ball.get_density())