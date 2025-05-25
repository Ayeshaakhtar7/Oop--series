# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name , breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof!")

breed1 = Dog("Addy", "white shepherd")
breed1.bark()
breed2 = Dog("Max", "Bulldog")
breed2.bark()