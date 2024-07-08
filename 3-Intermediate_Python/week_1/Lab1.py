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

def isPalindrome():
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

if __name__ == "__main__":
    isPalindrome()