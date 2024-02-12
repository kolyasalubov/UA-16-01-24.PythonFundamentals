import task_3_calculate_area 



while True:
    print('Hello, I can calculate next area: ')
    print('1.The area of a rectangle. \n2.The area of a triangle. \n3.The area of a circle. \n4. Stop')
    user_choice = int(input('Please choose the proposed number for calculating the area: '))

    result_of_calculate = 0
    match user_choice:
        case 1:
            side_a = float(input('Enter the length of side a: '))
            side_b = float(input('Enter the length of side b: '))
            result_of_calculate = task_3_calculate_area.calculate_area_rectangle(side_a, side_b)
            print(f'The area of a rectangle equal = {result_of_calculate}\n\n')
        case 2:
            side_a = float(input('Enter the length of side a: '))
            height = float(input('Enter the height: '))
            result_of_calculate = task_3_calculate_area.calculate_area_triangle(side_a, height)
            print(f'The area of a triangle equal = {result_of_calculate}\n\n')
        case 3:
            radius = float(input('Enter the radius: '))
            result_of_calculate = task_3_calculate_area.calculate_area_circle(radius)
            print(f'The area of a circle equal = {result_of_calculate}\n\n')
        case 4:
            break
        case _ :
            print('Sorry, but I don\'t have this number\n\n')

