# Write a program that starts with an empty list and takes three inputs from the user to populate the list.

def main():
    my_list = []
    string = input("Write a simple sentence: ")
    integer = input("Choose a whole number: ")
    floating_num = input("Choose a decimal number: ")

    my_list.extend([string, integer, floating_num])

    print(f"Here is your list: {my_list}")

if __name__ == "__main__":
    main()