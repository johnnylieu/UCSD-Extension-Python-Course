"""Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. 
After the user presses the enter key, the program should print the sum of the numbers and their average. 
You can also choose to have the user enter a keyword such as 'q' or simply ENTER without a number to finalize the entering of input values instead of just pressing enter."""
def ask():
    user_input = input("Enter a number: ")
    return user_input

def find_sum_avg():
    user_input = ask()

    if user_input.strip() != "":
        nums.append(float(user_input))
        print(nums)
        find_sum_avg()

    elif user_input.strip() == "" and len(nums) == 0:
        print(f"You did not enter a value.")

    else:
        print(f"The sum of {nums} is {sum(nums)} and its average is {(sum(nums)) /  len(nums)}")

if __name__ == "__main__":
    nums = []
    user_input = None

    find_sum_avg()