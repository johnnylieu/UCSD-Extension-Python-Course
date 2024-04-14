# Write a statement that counts the number of space characters in a string. Recall that the space character is represented as ' '.

def main():
    user_string = input('Please type a sentence to count spaces: ')
    number_of_empty_spaces = user_string.count(" ")
    print(number_of_empty_spaces)

if __name__ == "__main__":
    main()