# Task 2

def rectangle_area():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    return length * width

def triangle_area():
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    return (base * height)/2

def circle_area():
    radius = float(input('Enter radius: '))
    return 3,14 * radius ** 2

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