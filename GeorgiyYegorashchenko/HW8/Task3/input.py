from functions import rectangle_area
from functions import triangle_area
from functions import circle_area

def choose_function():
    response = input('Choose your figure: rectangle, triangle of circle: ')
    if response == 'rectangle':
        print(rectangle_area())
    elif response == 'triangle':
        print(triangle_area())
    elif response == 'circle':
        print(circle_area())
    else: print('error') 

print(choose_function())