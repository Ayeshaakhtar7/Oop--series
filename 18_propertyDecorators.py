# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self,new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @price.deleter
    def price(self):
        print("Price deleted!\n")
        del self._price


pdt1 = Product(1000)
print(f"Initial Price: {pdt1.price}")     

pdt1.price = 3000    
print(f"Updated Price: {pdt1.price}")     

del pdt1.price 
