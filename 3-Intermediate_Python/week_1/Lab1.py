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
    run_program = True
    word_reversed = ''
    while run_program:
        word = input("Please enter a word: ")
        if word.isalpha() == False:
            print(f"'{word}' is not a word.")
        else:
            for i in range(len(word)-1, -1, -1):
                word_reversed += word[i]
            if word == word_reversed:
                print(f"'{word}' is a palindrome!")
            else:
                print(f"Sorry but '{word}' is not a palindrome.")
        run_program = False

if __name__ == "__main__":
    isPalindrome()
