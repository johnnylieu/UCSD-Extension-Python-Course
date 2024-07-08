"""Write a program that creates a random number from 0 to 100 and asks a user to guess it. The user, 
should be able to modify the number of attempts at guessing what the number is. 
The program should tell the user whether the number is lower or greater than the user's guess. 
When the user guesses the correct answer the program should tell the user he/she had won. 
At the end of this exchange, your program should print out how many guesses it took to get the number.

Use the following code snippet to create the random number:   NUMBER = random.randint(MINIMUM, MAXIMUM)"""

import random

def guessing_game():
    random_number = random.randint(0, 100)
    num_of_attempts = int(input('How many attempts do you want? '))

    while num_of_attempts > 0:
        num_of_attempts -= 1
        user_num = int(input("What is your guess? "))

        if user_num > random_number:
            print(f"{user_num} is larger than the correct number.")
        elif user_num < random_number:
            print(f"{user_num} is smaller than the correct number.")
        elif user_num == random_number:
            print("That's correct!")
            break
    print(f"The correct number is {random_number}.")

if __name__ == "__main__":
    guessing_game()