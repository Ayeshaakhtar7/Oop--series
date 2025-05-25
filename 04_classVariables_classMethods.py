# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Bank Al Habib"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
print(f"\n\tThe Old Bank Name: '{bank1.bank_name}'")
bank1.change_bank_name("Meezan Bank")
print(f"\tThe New Bank Name: '{bank1.bank_name}'\n") 