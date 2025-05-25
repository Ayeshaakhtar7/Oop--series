# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"Name: {self.name}\nPosition: {self.position}"
    
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def get_department_info(self):
        return f"\nDepartment: {self.name}\nEmployee: {self.employee.get_employee_info()}\n"
    
employee1 = Employee("Amraha", "Software Engineer")
depart = Department("IT", employee1)
print(depart.get_department_info())