# Creating Employee class with name and salary. The class should have counter of number of employees,
# method returning quantity of employees and method that returns all info about employees

class Employee:
    '''
    Employee class contains hidden info about names, salaries and positions of employees
    '''
    employee_counter = 0
    def __init__(self, name, salary, position):
        Employee.employee_counter += 1
        self._name = name
        self.__salary = salary
        self.__position = position

        if self.__salary == 0:
            raise ValueError("Salary can't be 0")
        elif self.__salary < 0:
            raise ValueError("Salary can't be less than 0")
        
        if self.__position == False:
            raise ValueError("Position can't be empty")

    def __del__(self):
        if Employee.employee_counter > 0:
            Employee.employee_counter -= 1
        else:
            Employee.employee_counter = 0

    @staticmethod
    def calculate_employee_number():
        return f"Total employees number: {Employee.employee_counter}"
    
    def employee_info(self):
        return f"Employee name: {self._name}, salary: {self._Employee__salary}, position: {self._Employee__position}"
    

employee_1 = Employee("Edward Smith", 2000, "Accountant")
employee_2 = Employee("Peter Parker", 1000, "Spider man")
employee_3 = Employee("Amanda Seftor", 5464, "Singer")
employee_4 = Employee("Ben Reilly", 3566, "Super hero")
print("==== Employees number before deletion ====")
# employee_5 = Employee("Charlie Campion", 0, "Accountant")     # broken data employee to check Exception raising with 0 salary
# employee_6 = Employee("Dakota North", 1000, 0)                # broken data employee to check Exception raising with empty position
# employee_7 = Employee("Dexter Bennett", -10, "Scientist")     # broken data employee to check Exception raising with salary < 0 
print(Employee.calculate_employee_number())
del employee_3
print("==== Employee number after deletion ====")
print(Employee.calculate_employee_number())
print("==== Employees' info: ====")
print(employee_1.employee_info())
print(employee_2.employee_info())
print(employee_4.employee_info())
print("======= All employees deletion ========")
del employee_1, employee_2, employee_4
print(Employee.calculate_employee_number())




    

    


