# The variables x and y refer to numbers.
# Write a code segment that prompts the user for an arithmetic operator
# and prints the value obtained by applying that operator to x and y.

def main():
    a = 2
    b = 3

    operation = input("Please choose an arithmetic opration (+, -, or x): ")

    if operation == "+":
        total = a + b
        print(total)
    elif operation == "-":
        total = a - b
        print(total)
    elif operation == "x":
        total = a * b
        print(total)
    else:
        print("You did not choose +, -, or x.")

if __name__ == "__main__":
    main()