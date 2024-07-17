__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']

from DataTypeHelpers import *
from datetime import datetime

def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    
    while True:
        prompt = input(prompt)

        if isInt(prompt):
            value = int(prompt)

            if min_value <= value <= max_value:
                return value
            else:
                print("Value is out of range.")
        else:
            print("The entered text needs to be in the int format.")

def inputFloat(prompt="Enter a float: ", min_value=0, max_value=100):
    while True:
        prompt = input(prompt)

        if isFloat(prompt):
            value = float(prompt)

            if min_value <= value <= max_value:
                return value
            else:
                print("Value is out of range.")
        else:
            print("Entered text needs to be in the float format.")

def inputString(prompt="Enter a string: ", min_length=0, max_length=100):
    while True:
        prompt = input(prompt)
        prompt_length = len(prompt)

        if min_length <= prompt_length <= max_length:
            return prompt
        else:
            print("The string is out of range.")

def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): "):
    while True:
        prompt = input(prompt)

        if isDate(prompt):
            return datetime.fromisoformat(prompt)
        else:
            print('The entered text needs to be in the "yyyy-mm-dd" format.')