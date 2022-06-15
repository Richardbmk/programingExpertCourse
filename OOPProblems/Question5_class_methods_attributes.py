"""My Wrong solution"""

class Employee:
    # Write your code here
    total_employees = 0
    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.total_employees += 1
        Employee.average_age = (Employee.average_age + age) / Employee.total_employees
        Employee.average_salary = (Employee.average_salary + salary) / Employee.total_employees

e1 = Employee("George", 34, 65000)
print(Employee.average_age)
print(Employee.average_salary)

e1 = Employee("Sarah", 25, 95000)
print(Employee.average_age)
print(Employee.average_salary)


"""TIM SOlution"""
class Employee:
    number_of_employees = 0
    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1
