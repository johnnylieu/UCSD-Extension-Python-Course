__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']

from DataTypeHelpers import *
from datetime import datetime

min_value = 0
max_value = 100

min_length = 0
max_length = 100

def inputInt():
    
    while True:
        prompt = input("Enter an integer: ")

        if isInt(prompt):
            value = int(prompt)

            if min_value <= value <= max_value:
                return value
            else:
                print("Value is out of range.")
        else:
            print("The entered text needs to be in the int format.")

def inputFloat():
    while True:
        prompt = input("Enter a float: ")

        if isFloat(prompt):
            value = float(prompt)

            if min_value <= value <= max_value:
                return value
            else:
                print("Value is out of range.")
        else:
            print("Entered text needs to be in the float format.")

def inputString():
    while True:
        prompt = input("Enter a string: ")
        prompt_length = len(prompt)

        if min_length <= prompt_length <= max_length:
            return prompt
        else:
            print("The string is out of range.")

def inputDate():
    while True:
        prompt = input("Enter a date in this format (yyyy-mm-dd): ")

        if isDate(prompt):
            return datetime.fromisoformat(prompt)
        else:
            print('The entered text needs to be in the "yyyy-mm-dd" format.')