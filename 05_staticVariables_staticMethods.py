# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(f"\n\tThe Sum of 5 and 10 is: '{MathUtils.add(5, 10)}'\n")
