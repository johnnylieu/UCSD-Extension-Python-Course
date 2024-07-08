"""Write a program that inherits from the class below and adds a modulus division function to the child class 
(test your code by creating an object and printing out the results for each function):

class Calc():

    def add(self, a, b):
        return  a + b

    def subtract(self, a, b):
        return a - b
        
    def multiply(self,a,b):
        return a * b
        
    def divide(self, a, b):
        if b==0:
            raise ValueError('Cannot divide by zero!')
        return a / b
"""

class Calc():

    def add(self, a, b):
        return  a + b

    def subtract(self, a, b):
        return a - b
        
    def multiply(self,a,b):
        return a * b
        
    def divide(self, a, b):
        return a / b

class Cal_Inheritance_Division(Calc): # it's now inheriting everything from the class Calc
    def division(self, a, b):
        return self.divide(a, b) # using the divide method from the parent class

if __name__ == "__main__":
    my_obj = Cal_Inheritance_Division()
    print(my_obj.add(2, 3))
    print(my_obj.subtract(2, 3))
    print(my_obj.multiply(2, 3))
    print(my_obj.divide(2, 3))