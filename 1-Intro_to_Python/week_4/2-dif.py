"""Write a script named dif.py. 
This script should prompt the user for the names of two text files and compare the contents of the two files to see if they are the same. 
If they are, the script should simply output " Yes" . If they are not, the script should output " No" , 
followed by the first lines of each file that differ from each other. The input loop should read and compare lines from each file. 
The loop should break as soon as a pair of different lines is found. Use the following files to do the comparison: AboutText.txt Download AboutText.txt, NotAboutText.txt"""

def difference(file1, file2):
    try:
        with open(file1, 'r') as file1, open(file2, 'r') as file2:
            for line1, line2 in zip(file1, file2):
                    if line1.strip() != line2.strip():
                        print("No")
                        return
            print("Yes")

    except FileNotFoundError:
        print("Either one or both of these files were not found.")

if __name__ == "__main__":
    print("Please enter two text files you wish to compare.")
    file1 = input("First file: ")
    file2 = input("Second file: ")

    difference(file1, file2)