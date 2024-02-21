class Employee():
    employees_num = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_num += 1
    @classmethod
    def count_employees(cls):
        print(f"Total:{cls.employees}")

    def employee_info(self):
        print(f"Name: {self.name}, salary:{self.salary}")