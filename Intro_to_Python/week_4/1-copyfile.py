"""Write a script named copyfile.py . This script should prompt the user for the names of two text files. 
The contents of the first file should be input and written to the second file. Use the following file: AboutText.txt"""

def copy_file():
    input_file = 'AboutText.txt'
    output_file = 'AboutTextCOPY.txt'

    try:
        # if we use with open, we do not need to tell the program to close the file after it is read.
        with open(input_file, 'r') as input_file:
            file_contents = input_file.read()

            with open(output_file, 'w') as output_file:
                output_file.write(file_contents)

                print(f"New file created.")

    except FileNotFoundError:
        print(f"Error: No file found.")

if __name__ == "__main__":
    copy_file()