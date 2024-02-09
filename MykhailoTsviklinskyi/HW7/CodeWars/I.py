# Jenny's secret message
# https://www.codewars.com/kata/55225023e1be1ec8bc000390

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    