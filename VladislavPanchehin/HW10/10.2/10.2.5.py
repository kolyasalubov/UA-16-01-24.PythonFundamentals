import math
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass
#Radius of the sphere.
    def get_radius(self):
        return self.radius
#Mass of the sphere
    def get_mass(self):
        return self.mass
#Volume of the sphere          
    def get_volume(self):
        return round((4/3) * math.pi * pow(self.radius,3))
#Surface of the sphere    
    def get_surface_area(self):
        return round(4 * math.pi * pow(self.radius,2))
#mass of the sphere
    def get_density(self):
         return round(self.mass/self.get_volume())
    
#tested

ball = Sphere(2, 50)
print(ball.get_radius())         
print(ball.get_mass())           
print(ball.get_volume())         
print(ball.get_surface_area())   
print(ball.get_density())        

    