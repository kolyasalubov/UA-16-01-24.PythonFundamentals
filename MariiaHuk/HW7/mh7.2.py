
def calculate_area(name):
   
  # check for the conditions
  if name == "rectangle":
    l = int(input("Enter rectangle's length: "))
    w = int(input("Enter rectangle's width: "))
     
    rectangle_area = l * w
    print(f"The area of rectangle is {rectangle_area}.")
   
  elif name == "triangle":
    h = int(input("Enter triangle's height: "))
    w = int(input("Enter triangle's width: "))
       
    triangle_area = 0.5 * w * h
    print(f"The area of triangle is {triangle_area}.")
 
  elif name == "circle":
    r = int(input("Enter circle's radius: "))
    pi = 3.14
         
    circle_area = pi * r * r
    print(f"The area of circle is {circle_area}.")
     
  else:
    print("Sorry! This shape is unknown")
 
if __name__ == "__main__" :
   
  print("Calculate Shape Area")
  shape_name = input("Enter the name of shape to find area: ")
   
  calculate_area(shape_name)
  