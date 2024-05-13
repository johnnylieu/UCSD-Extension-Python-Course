"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list."""

def first_and_last(list):
    new_list = []
    new_list = [list[0], list[-1]]
    
    return new_list

if __name__ == "__main__":
    list = [5, 10, 15, 20, 25]

    print(first_and_last(list))