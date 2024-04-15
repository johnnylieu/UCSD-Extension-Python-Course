"""A group of statisticians at a local college has asked you to create a set of functions that compute the median
and mode of a set of numbers (recall that the mode is the number that appears the most and the median is the number(2) in the middle of an ordered list of numbers). 
Define these functions in a module named stats.py . Also include a function Named mean , which computes the average of a set of numbers. 
Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty. 
Include a main function that tests the three statistical functions with a given list. Use the list: [2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]"""

def median(list):
    # sort the list
    sorted_list = sorted(list)
    # find the middle index, // returns the floor number without decimal
    middle = len(sorted_list) // 2
    # if the list has an even number of elements then we will add the middle two and dvide by two to get the median
    if len(sorted_list) % 2 == 0:
        median = (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        median = sorted_list[middle]

    return median

def mode(list):
    # sets value for every num in list to zero in a dictionary
    num_count = {num: 0 for num in list}
    most_num = 0

    for num in list:
        if num in list:
            # increment value by 1 if num is in list
            num_count[num] += 1
    
    for num in num_count:
        if num_count[num] > most_num:
            most_num = num_count[num]
    
    return most_num

def mean(list):
    total = sum(list)
    mean = total / len(list)
    
    return mean


if __name__ == "__main__":
    list = sorted([2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3])
    print(f"{median(list)}\n{mode(list)}\n{mean(list)}")