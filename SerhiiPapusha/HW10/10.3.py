class Employee():
    """This class keeps the information about employees"""
    employees_qnt = 0

    def __init__(self, name, salary):
        Employee.employees_qnt += 1
        self.name = name
        self.__salary = salary

    def setSalary(self, salary):
        self.__salary = salary

    def __del__(self):
        Employee.employees_qnt -= 1

    @classmethod
    def show_employee_qnt(cls):
        return cls.employees_qnt
    
    def show_emp_info(self):
        return f"Employee name: {self.name}\nEmployee salary: {self.__salary}"
    
emp1 = Employee("Jack", 2000)
emp2 = Employee("Sara", 2200)

print(emp1.show_employee_qnt())
print(emp1.show_emp_info())

emp1.salary = 2400
print(emp1.show_emp_info())
emp1.setSalary(2499)
print(emp1.show_emp_info())


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
