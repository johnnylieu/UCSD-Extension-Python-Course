"""Write a program that inputs a text file. The program should print the unique words in the file in alphabetical order."""

def unique_words():
    try:
        text_file=input("Which text file do you want to use? ")

        with open(text_file, 'r') as text_file:
            file_contents = text_file.read()
            words = file_contents.split()
            num_of_words = len(words)

            return f"{num_of_words} words."

    except FileNotFoundError:
        print(f"Error: No file found.")

if __name__ == "__main__":
    print(unique_words())