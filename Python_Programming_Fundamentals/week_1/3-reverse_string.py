"""Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My"""

def reverse_string(string):
    string = string.split()
    string = string[::-1]
    string = " ".join(string)

    return(string)

if __name__ == '__main__':
    string = input("Enter a sentence or series of words you would like to reverse: ")

    print(reverse_string(string))