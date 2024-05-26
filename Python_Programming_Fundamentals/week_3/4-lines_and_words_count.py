"""Write a Python program that counts how many lines and how many words there are in a file."""

if __name__ == "__main__":
    num_lines = 0
    num_words = 0

    with open('About_Python-1.txt', 'r') as file: # don't need to specify r as it is read by default

        for line in file:
            num_lines += 1
            
            words = line.split()
            for word in words:
                num_words += 1

        print(f"There are {num_lines} of lines & {num_words} of words.")