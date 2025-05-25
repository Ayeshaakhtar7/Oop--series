# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current
        

count1 = Countdown(10)
for number in count1:
    print(number)