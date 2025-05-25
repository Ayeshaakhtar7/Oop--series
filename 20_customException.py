# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print(f"Access granted for age {age}")

try:
    check_age(16)

except InvalidAgeError as e:
    print(f"Invalid age: {e}")

try:
    check_age(22)

except InvalidAgeError as e:
    print(f"Invalid age: {e}")