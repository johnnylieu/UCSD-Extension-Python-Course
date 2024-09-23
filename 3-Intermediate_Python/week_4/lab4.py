from fractions import Fraction
from decimal import *

getcontext().prec = 70

pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
iterations = 100000

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

        return self.fraction
    
    def __str__(self):
        self.decimal_format = Decimal(self.fraction.numerator) / Decimal(self.fraction.denominator)
        self.difference = abs(self.decimal_format - pi50)
        return f"pi after {self.iterated} iterations: {self.decimal_format:.50f} \nDifference: {self.difference:.50f}"
    

def NilakanthaPiGenerator():
    fraction = Fraction(3, 1)
    num = 2
    add_next = True
    iterated = 0

    while True:
        operand = Fraction(4, num * (num + 1) * (num + 2))

        if add_next:
            fraction += operand
        else:
            fraction -= operand

        num += 2
        iterated += 1

        yield fraction
    
if __name__ == "__main__":
    ## Leibniz method
    obj = LeibnizPiIterator()
    obj = iter(obj)
    for i in range(iterations):
        next(obj)
    print(obj)

    ## Nilakantha's method
    obj2 = NilakanthaPiGenerator()
    for i in range(iterations):
        approx_pi = next(obj2)
    print(f"After {iterations} iterations, pi ≈ {approx_pi:.50F}")