# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    brand = "Toyota"

    def start(self):
        print("The car has started!")


my_car = Car()

print(f"Car brand is {my_car.brand}")

my_car.start()
