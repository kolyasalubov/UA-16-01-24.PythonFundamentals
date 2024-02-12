# Will you make it?
# https://www.codewars.com/kata/will-you-make-it

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else:
        return True
    