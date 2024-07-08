"""Write a Python class which has two methods get_String and print_String. The function get_String accepts and returns a string passed into a constructor. 
The function print_String prints the string in upper case. The class should have a constructor that returns the string entered by the user as an argument. 
Create an object to test execute the functions from the class."""

class Strings:
    def __init__(self, users_string):
        self.users_string = users_string
    
    def get_String(self):
        return self.users_string

    def print_String(self):
         print(self.users_string.upper())

if __name__ == "__main__":
    users_string = input("Enter a sentence/string: ")
    my_Ojb = Strings(users_string)
    print(my_Ojb.get_String())
    my_Ojb.print_String()