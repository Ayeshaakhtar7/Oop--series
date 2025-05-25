# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  
        self._salary = salary
        self.__ssn = ssn

emp1 = Employee("Emma", 50000, "123-45-6789")
print(f"\n\tEmployee Name: '{emp1.name}'")
print(f"\tEmployee Salary: '{emp1._salary}'")
print(f"\tEmployee SSN: '{emp1._Employee__ssn}'\n")

emp2 = Employee("Zara", 60000, "987-65-4321")
print(f"\tEmployee Name: '{emp2.name}'")
print(f"\tEmployee Salary: '{emp2._salary}'")
print(f"\tEmployee SSN: '{emp2._Employee__ssn}'\n")