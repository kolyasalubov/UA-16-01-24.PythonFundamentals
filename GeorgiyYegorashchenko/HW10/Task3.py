class Employee:
    employee_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_counter += 1

    def employee_info(self):
        return f"{self.name}'s salary is {self.salary}"

    @classmethod
    def employees_total(cls):
        return f"Total employees: {cls.employee_counter}" 
    
    @staticmethod
    def extra_info():
        print(f"class name: {Employee.__name__}")
        print(f"parent class: {Employee.__base__}")
        print(f"class namespace: {Employee.__dict__}")
        print(f"modulename where defined: {Employee.__module__}")
        print(f"documentation bar: {Employee.__doc__}")
    

new_employee = Employee('Andrew', 3000)

# print(new_employee.employee_info())
# print(new_employee.employee_counter)

print(new_employee.extra_info())