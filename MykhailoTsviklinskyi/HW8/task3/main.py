import count_area

while True:

    entered_shape = input("Which area of figure (rectangle, triangle, circle) do you want to calculate? ").lower()

    if entered_shape == 'rectangle':
        width = float(input("Enter width of the rectangle: "))
        length = float(input("Enter length of the rectangle: "))
        print(f"The area of Rectangle is: {count_area.count_area_of_rectangle(width, length):.2f}")
        break

    elif entered_shape == 'triangle':
        height = float(input("Enter height of the triangle: "))
        base = float(input("Enter base of the triangle: "))
        print(f"The area of Triangle is: {count_area.count_area_of_triangle(height, base):.2f}")
        break

    elif entered_shape == 'circle':
        radius = float(input("Enter radius of the circle: "))
        print(f"The area of Circle is: {count_area.count_area_of_circle(radius):.2f}")
        break

    else:
        print(f"'{entered_shape}' is wrong shape. Please enter correct shape from the list")
