from Task1 import Rectangle
from Task2 import Human
from Task3 import Employee


#task1
rectang = Rectangle(3, 5)

rectang.calculateSquare()
print('--------------------------------')

#task2
human1 = Human("Rico")

human1.welcomeToHuman()
print(f'{human1.name} is the kind of {human1.returnKind()}')
print(human1.returnSomeString())
print('--------------------------------')

#task3
employee1 = Employee("Sam", 3434.40)
employee1.printInformation()

employee2 = Employee("Catty", 4000.00)
employee2.printInformation()
employee2.name = 'Ell'
employee2.printInformation()

Employee.printAmount()

print('--------------------------------')
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
