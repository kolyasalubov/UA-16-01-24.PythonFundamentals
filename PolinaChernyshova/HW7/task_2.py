PI = 3.14

def calculate_area_rectangle(side_a: float, side_b: float )->float:
    '''
    The function takes to float type arguments: side_a, side_a
    Return the area of a rectangle in float type 
    '''
    return side_a * side_b

def calculate_area_triangle(side_a: float, height: float )->float:
    '''
    The function takes to float type arguments: side_a, height
    Return the area of a triangle in float type 
    '''
    return 0.5 * side_a * height

def calculate_area_circle(radius: float)->float:
    '''
    The function takes to float type argument: radius
    Return the area of a circle in float type 
    '''
    return PI * radius **2




while True:
    print('Hello, I can calculate next area: ')
    print('1.The area of a rectangle. \n2.The area of a triangle. \n3.The area of a circle. \n4. Stop')
    user_choice = int(input('Please choose the proposed number for calculating the area: '))

    result_of_calculate = 0
    match user_choice:
        case 1:
            side_a = float(input('Enter the length of side a: '))
            side_b = float(input('Enter the length of side b: '))
            result_of_calculate = calculate_area_rectangle(side_a, side_b)
            print(f'The area of a rectangle equal = {result_of_calculate}\n\n')
        case 2:
            side_a = float(input('Enter the length of side a: '))
            height = float(input('Enter the height: '))
            result_of_calculate = calculate_area_triangle(side_a, height)
            print(f'The area of a triangle equal = {result_of_calculate}\n\n')
        case 3:
            radius = float(input('Enter the radius: '))
            result_of_calculate = calculate_area_circle(radius)
            print(f'The area of a circle equal = {result_of_calculate}\n\n')
        case 4:
            break
        case _ :
            print('Sorry, but I don\'t have this number\n\n')


