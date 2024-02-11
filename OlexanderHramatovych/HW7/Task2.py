pi = 3.141592653589793                 # definition of pi
def rectangle_area(number1,number2):   # the function of rectangle
    return r1*r2

def triangle_area(num1,num2):          # the function of triangle                     
    return num1/2 * num2

def circle_area(num1):                 # the function of circel 
    return (num1 ** 2)*pi

# user inputs sides of rectangle
r1 = int(input("Enter the first side of rectagle: "))  
r2 = int(input("Enter the second side of rectagle: ")) 

# user inputs sides of triangle
t1 = int(input("Enter the first side of triangle: ")) 
t2 = int(input("Enter the second side of triangle: "))

# user inputs radius of circle
s1 = int(input("Enter the radius of circle: ")) 

# outputing the result
print(f"The area of rectagle is: {rectangle_area(r1,r2)}") 
print(f"The area of triangle is: {triangle_area(t1,t2)}") 
print(f"The area of circle is: {circle_area(s1)}")