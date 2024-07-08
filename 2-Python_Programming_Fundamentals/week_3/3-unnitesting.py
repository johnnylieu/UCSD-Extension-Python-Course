"""Given the following code below saved as a file named calc.py, import the file into a new file named test_calc.py and write a unittest to test each function:

def add(x, y):

    return x + y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x / y;

 

*Note: To test out the exception you will need to run the context manager:  

with self.assertRaises(ValueError):

 calc.divide(1, 0)

                 ** Use the following EvenNum.py Download EvenNum.pyand EvenNum_test.py Download EvenNum_test.pyas a guide.
In your unittest you may want to try various options such as using two positive numbers, a positive and negative number and two negative numbers for each test."""

import calc
import unittest

class Test_Calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)

        # nothing can be divded by zero
        with self.assertRaises(ValueError):
            calc.divide(1, 0)

if __name__ == "__main__":
    unittest.main()
