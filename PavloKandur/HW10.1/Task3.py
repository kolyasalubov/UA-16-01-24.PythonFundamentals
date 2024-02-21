class Employee():
    number_of_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees +=1

    @classmethod
    def amount_of_employees(cls):
        return cls.number_of_employees
    
    def employee_info(self):
        print(f'{self.name}\n{self.salary}')

Employee1 = Employee('John',600)
Employee2 = Employee('Emily',800)
Employee3 = Employee('Steve',500)

Employee1.employee_info()
print(Employee.amount_of_employees())


