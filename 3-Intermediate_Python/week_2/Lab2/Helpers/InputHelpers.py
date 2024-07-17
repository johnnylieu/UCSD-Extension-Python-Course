__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']

from Helpers.DataTypeHelpers import *
from datetime import datetime

def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    
    while True:
        user_input = input(prompt)

        if isInt(user_input):
            value = int(user_input)

            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}")
        else:
            print("The entered text needs to be in the int format.")

def inputFloat(prompt="Enter a float: ", min_value=0, max_value=100):
    while True:
        user_input = input(prompt)

        if isFloat(user_input):
            value = float(user_input)

            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}")
        else:
            print("Entered text needs to be in the float format.")

def inputString(prompt="Enter a string: ", min_length=0, max_length=100):
    while True:
        user_input = input(prompt)
        prompt_length = len(user_input)

        if min_length <= prompt_length <= max_length:
            return user_input
        else:
            print(f'Text must be between {min_length} and {max_length} in length')

def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): "):
    while True:
        user_input = input(prompt)

        if isDate(user_input):
            return datetime.fromisoformat(user_input)
        else:
            print('The entered text needs to be in the "yyyy-mm-dd" format.')