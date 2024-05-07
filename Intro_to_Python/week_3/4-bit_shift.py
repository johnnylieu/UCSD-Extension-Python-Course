""" A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right. 
For example, we can shift the bits in the string 1011 two places to the left to produce the string 1100 . 
Note that the leftmost two bits are wrapped around to the right side of the string in this operation. 
Define two scripts, shiftLeft.py and shiftRight.py , that expect a bit string as an input. 
The script shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit to the rightmost position. 
The script shiftRight performs the inverse operation. Each script prints the resulting string."""

def shift_right(bit_string):
    # this grabs the last character in the bit string and puts in the beginning of the string, then grabs all the characters up to the 2nd to the last of the string and concanates it
    # we can use + to concatenate the values because it is a string
    shifted_right = bit_string[-1] + bit_string[:-1]
    return shifted_right

def shift_left(bit_string):
    shifted_left = bit_string[1:] + bit_string[0]
    return shifted_left

def shift():
    bit_string = input("Please enter a bit string (a bit string is a series of zeros and ones, e.g. \"1011\"): ")

    right_shift = shift_right(bit_string)
    left_shift = shift_left(bit_string)

    print(f'Shifted right by one is {right_shift}.\nShifted left by one is {left_shift}.')



if __name__ == "__main__":
    shift()