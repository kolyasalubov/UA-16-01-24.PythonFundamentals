class Employee():

    '''This is a class for counting employees.
    In this class every employee has their own name and salary.
    Methods: all_information displays the specified information;
    count_all_employees displays number of specified employees.'''
    
    
    count_employees = 0
    
    def __init__(self, person, salary):
        self.employee = person
        self.salary = salary
        Employee.count_employees +=1
    
    
    def all_information(self):
        return f"{self.employee} has a salary amoung {self.salary}." 
    
    @classmethod
    def count_all_employees(self):
        return f"Total employees: {self.count_employees}"



employee1 = Employee("Samanta", 40)
employee2 = Employee("Olha", 4000)
employee3 = Employee("veronika", 70000)

print(employee1.all_information())
print(employee2.all_information())

print(Employee.count_all_employees())

print(f"Type: {Employee.__base__} ")
print(f"The class namespaces: {Employee.__dict__}")
print(f"Name of our Class: {Employee.__name__}")
print(f"The module name: {Employee.__module__}")
print(f"The documantation: {Employee.__doc__}")
