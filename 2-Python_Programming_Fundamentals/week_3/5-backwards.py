"""Write a Python program that reads in the file from the problem above and writes the document completely backward to a new text file 
(the last letter of the entire document becomes the first and so on so the document can be read from bottom to top and from right to left)"""

if __name__ == "__main__":
    with open('About_Python-1.txt') as file:
        content = file.read()

    reversed_lines = content[::-1]

    with open('reversed.txt', 'w') as file:
        for line in reversed_lines:
            file.write(line)
