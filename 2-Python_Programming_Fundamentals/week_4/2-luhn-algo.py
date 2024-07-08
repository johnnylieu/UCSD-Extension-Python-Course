"""The Luhn algorithm is used to verify whether a credit card number is valid or not. 
You will need to create a program that uses regular expressions to find the credit card information from a string and then runs the Luhn Algorithm to verify the credit card number. 
Use the test below.

 

"Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."

 

The Luhn algorithm is as follows:

Assume you have a number as: 3 - 7 - 5 - 6 - 2 - 1 - 9 - 8 - 6 - 7 - 3
Now starting from the rightmost digit i.e. check digit, double every second digit. New number will be: 3 - 14 - 5 - 12 - 2 - 2 - 9 - 16 - 6 - 14 - 3
If double of a digit is more then 9, then subtract 9 to that number. Then add the digits so the number will become: 3 - 5 - 5 - 3 - 2 - 2 - 9 - 7 - 6 - 5 - 3
Sum all the numbers together and find the modulus (%10). If the modulus is equal to zero, the number is valid"""

import re

text = "Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."
pattern = r"\bVisa #\s*(\d+)\b"
match = re.search(pattern, text)

if __name__ == "__main__":
    print(f"The credit card number is: {match.group(1)}")
    # question why does printing match alone return Visa # in front of the cc number?
    # print(match)

    # converting to list so i can use lambda function
    nums_list = list(match.group(1))
    # converts every value to an integer
    nums_list = [int(x) for x in nums_list]
    # i had to add 1 to the index because indexing started at 0 instead of 1
    doubled_nums_list = list(map(lambda x : int(x) *2 if (nums_list.index(x) + 1) % 2 == 0 else x, nums_list))
    print(f"Doubled is {doubled_nums_list}")

    # If double of a digit is more then 9, then subtract 9 to that number
    double_digits = list(map(lambda x: int(x)-9 if int(x)>9 else x, doubled_nums_list))
    print(f"If double of a digit is more then 9, then subtract 9 to that number: {double_digits}")

    # Sum all the numbers together and find the modulus (%10). If the modulus is equal to zero, the number is valid
    sum_of_nums_list = sum(nums_list)
    sum_of_doubled_nums_list = sum(doubled_nums_list)
    sum_of_double_digits = sum(double_digits)
    print(
    f"The sum of original with modulus 10 is: {sum_of_nums_list % 10}.\n"
    f"The sum of doubled with modulus 10 list is: {sum_of_doubled_nums_list % 10}.\n"
    f"The sum of double digits with modulus 10 is: {sum_of_double_digits % 10}."
    )