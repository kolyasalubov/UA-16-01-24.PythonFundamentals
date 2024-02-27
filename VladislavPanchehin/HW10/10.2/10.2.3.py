#Create God function
def God():
    Adam = Man()
    Eva = Woman()
    return [Adam,Eva]

#Define the base class Human

class Human:
    print('This is Class Human')

# Define a subclass of Man that inherits from Human
class Man(Human):
    print('This is subclass of Man')

# Define a subclass of Woman, inheriting from Human

class Woman(Human):
    print('This is subclass of Woman')

#Tested
test = God()
print(test)
