# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        return "Engine Started.."
    
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()
    

eng1 = Engine()

car1 = Car(eng1)

print(car1.start_car())