
# Creare class Employee
class Employee:
    """Class with information about employees and their salaries
    """
    # Create starter counter Employee
    COUNT_EMPLOYEE = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
# Counter increase
        Employee.COUNT_EMPLOYEE += 1

    def employee_info(self):
        return f'Employee {self.name} receives a salary {self.salary}$'

    @classmethod
    def employee_total(cls):
        return '\n'f'Total employees {cls.COUNT_EMPLOYEE} and Total Salarys All Employees'
# display information about the base classes from which the employee class


class About_base_classes(Employee):
    """Information about base classes
    """
    @staticmethod
    def base_class_information():
        print('\n'"Base classes:", Employee.__base__, '\n')
        print("Class namespace:", Employee.__dict__, '\n')
        print("Class name:", Employee.__name__, '\n')
        print("Module name:", Employee.__module__, '\n')
        print("Documentation:", Employee.__doc__)


# Test
Employee_1 = Employee("Vika", 3000)
Employee_2 = Employee("Oleg", 100)
Employee_3 = Employee("Serg", 30000)
Employee_4 = Employee("Andrew", 2000)
Employee_5 = Employee("Max", 232)

# Info about Employee
print(Employee_1.employee_info())
print(Employee_2.employee_info())
print(Employee_3.employee_info())
print(Employee_4.employee_info())
print(Employee_5.employee_info())

# Total Employee
print(Employee.employee_total())
#print()
#
About_base_classes.base_class_information()
