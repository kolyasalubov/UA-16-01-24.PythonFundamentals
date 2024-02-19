class Employee:
    """
    This class has all information about employee
    including name, salary and total employees number
    """
    employee_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1

    def display_info_about_employee(self):
        """This function prints information about employee's name and salary"""
        return f"Employee {self.name} has ${self.salary} salary"
    
    @classmethod
    def display_employees_number(cls):
        """This function prints the total number of employees"""
        return f"Total number of employees: {cls.employee_counter}"
    

class Additional(Employee):
    """This class display all info about parent class"""
    
    @staticmethod
    def display_additional_info():
        print(f"Inherited class is: {Employee.__base__}")
        print(f"Class namespace is: {Employee.__dict__}")
        print(f"Class name is: {Employee.__name__}")
        print(f"Module name in which the class is defined is: {Employee.__module__}")
        print(f"Documentation of inherited class: {Employee.__doc__}")


employee1 = Employee("Mykhailo", 1000)
employee2 = Employee("Yanina", 2000)

print(employee1.display_info_about_employee())
print(employee2.display_info_about_employee())

print(Employee.display_employees_number())

Additional.display_additional_info()
