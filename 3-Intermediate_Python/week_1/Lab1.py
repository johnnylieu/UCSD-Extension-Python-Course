# Part 1 - Johnny Lieu
"""Part I
Create a python script to determine if a user-entered string is a palindrome. A palindrome is text that
reads the same forwards and backwards. Examples:
MOM
DAD
LEVEL
REDIVIDER
Requirements:
• The text to be scanned must be user-entered. Suggestion: input() function.
• You must use a loop to scan the characters.
• Do not use a prebuilt “reverse” function. This includes slicers. I know you can do this with a
VERY simple command, but I want to see your use of loops.
Sample Run (User-entered data in RED):
Enter a string: REDIVIDER
Is 'REDIVIDER' a palindrome? True"""

def is_palindrome():
    user_string = input("Enter a string: ")
    # the below will tell the user whether or not they entered a word
    # but since you are asking for a string, i'm assuming that includes sentences as well so i removed it
    # if word.isalpha() == False:
    #     print(f"'{word}' is not a word.")
    # the below would have been an elif if the above was used
    # user_string would have been word and user_string_reversed would have been word_reversed
    user_string_reversed = ''
    for i in range(len(user_string)-1, -1, -1):
        user_string_reversed += user_string[i]
    print(f"Is '{user_string}' a palindrome? {user_string == user_string_reversed}")


# Part 2 - Johnny Lieu
"""Part II
Create a Python script that grades the strength of a password.
Requirements:
• You will prompt the user for a password. Do not worry about “hiding” the input text, this is just
an academic exercise.
• The score is an integer value between 0 and 5, where 0 is a weak password 5 is a strong
password.
• For each of the following conditions, add 1 to the score if true:
o Password length is greater than or equal to 8
o The password contains at least one upper-case letter
o The password contains at least one lower-case letter
o The password contains at least one numeric digit (0-9)
o The password contains one of the following symbols: !@#$%^&*
• Use a loop to “visit” all of the characters (do not use regular expressions or other pattern
matching libraries)
• Indicate the score as output
Sample Run (User-entered data in RED):
Enter a password: Cougar1!
Your password score is: 5"""

def password_scoring():
    found_upper_case = False
    found_lower_case = False
    found_number = False
    found_symbols = False
    symbols = ('!@#$%^&*')
    points = 0
    user_password = input('Enter a password: ')

    if len(user_password) >= 8:
        points += 1

    for char in user_password:
        if not found_upper_case and char.isupper():
            points += 1
            found_upper_case = True
        elif not found_lower_case and char.islower():
            points += 1
            found_lower_case = True
        elif not found_number and char.isnumeric():
            points += 1
            found_number = True
        elif not found_symbols and char in symbols:
            points += 1
            found_symbols = True

    print(f"Your password score is: {points}")

if __name__ == "__main__":
    # is_palindrome()
    password_scoring()