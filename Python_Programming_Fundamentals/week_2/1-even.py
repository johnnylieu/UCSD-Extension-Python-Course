"""Give a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
write one line of Python that takes this list and makes a new list that has only the even elements of this list in it."""

def get_evens(li):
    evens_list = list(filter(lambda x: x%2==0, li))
    return evens_list

if __name__ == '__main__':
    li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(get_evens(li))