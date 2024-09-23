from Fraction import *
from decimal import *

pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
iterations = 100

class LeibnizPiIterator:
    def __init__(self):
        pass

    def __iter__(self):
        self.iterated = 0
        # running total for the series
        self.fraction = Fraction(0, 1)
        # denominator to be used in the next iteration
        self.n = 1
        self.add_next = True

        return self
    
    def __next__(self):
        self.next_value = Fraction(4, self.n)

        if self.add_next is True:
            self.fraction += self.next_value
        else:
            self.fraction -= self.next_value

        self.add_next = not self.add_next
        self.n += 2

        self.iterated += 1

        return self.fraction.value
    
    def __str__(self):
        self.decimal_format = Decimal(self.fraction.numerator) / Decimal(self.fraction.denominator)
        self.difference = abs(self.decimal_format - pi50)
        return f"pi after {self.iterated} iterations: {self.fraction.value} \nDifference: {self.difference}"
    
if __name__ == "__main__":
    obj = LeibnizPiIterator()
    obj = iter(obj)
    for i in range(iterations):
        next(obj)
        print(obj)