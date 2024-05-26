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