"""The Luhn algorithm is used to verify whether a credit card number is valid or not. You will need to create a program that uses regular expressions to find the credit card information from a string and then runs the Luhn Algorithm to verify the credit card number. Use the test below.

 

"Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."

 

The Luhn algorithm is as follows:

Assume you have a number as: 3 - 7 - 5 - 6 - 2 - 1 - 9 - 8 - 6 - 7 - 3
Now starting from the rightmost digit i.e. check digit, double every second digit. New number will be: 3 - 14 - 5 - 12 - 2 - 2 - 9 - 16 - 6 - 14 - 3
If double of a digit is more then 9, then subtract 9 to that number. Then add the digits so the number will become: 3 - 5 - 5 - 3 - 2 - 2 - 9 - 7 - 6 - 5 - 3
Sum all the numbers together and find the modulus (%10). If the modulus is equal to zero, the number is valid"""

if __name__ == "__main__":
    pass