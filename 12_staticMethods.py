# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c): 
        return (c * 9/5) + 32


calc1 = TemperatureConverter()
print(f"Temperature in Fahrenheit: {calc1.celsius_to_fahrenheit(39)}")
