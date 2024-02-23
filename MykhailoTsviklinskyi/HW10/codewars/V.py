# Building Spheres
# https://www.codewars.com/kata/55c1d030da313ed05100005d

from math import pi, pow

class Sphere:
    def __init__(self, radius: int | float, mass: int | float):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = 4/3 * pi * pow(self.radius, 3)
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * pi * pow(self.radius, 2)
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / (4/3 * pi * pow(self.radius, 3))
        return round(density, 5)
    