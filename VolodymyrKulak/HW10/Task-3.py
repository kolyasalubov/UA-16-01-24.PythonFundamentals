
class Employee:
    """Employee has characteristics such as name and salary.
    The class has a counter that calculates the total number of employees
    Has a method that prints the total number of employees,
     and a method that displays information about each employee in particular"""

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def employee_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")



employee1 = Employee("Alice", 50000)
employee2 = Employee("Robert", 60000)

employee1.employee_info()
employee2.employee_info()

Employee.show_total_employees()

print(f"Base Classes: {Employee.__base__}")
print(f"Class Namespace: {Employee.__dict__}")
print(f"Class Name: {Employee.__name__}")
print(f"Module Name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
