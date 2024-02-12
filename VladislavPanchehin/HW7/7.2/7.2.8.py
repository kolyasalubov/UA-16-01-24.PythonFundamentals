def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False
# varian 2


def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# zero_fuel(50, 25, 2), True)    2 * 25 = 50 миль запаса хода.

#  distance_to_pump — distance to the nearest gas station in miles.
#  mpg - Your car's average fuel economy in miles per gallon.
#  fuel_left is the amount of fuel left in gallons.
