# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student's Name: {self.name}")
        print(f"Student's Marks: {self.marks}")

student1 = Student("Amraha", 92)
student1.display()
student2 = Student("Sara", 87)
student2.display()
