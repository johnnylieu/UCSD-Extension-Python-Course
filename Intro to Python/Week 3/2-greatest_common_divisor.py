# The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers. You can use this algorithm in the following manner:
#              a.     Compute the remainder of dividing the larger number by the smaller number.
#              b.    Replace the larger number with the smaller number and the smaller number with the remainder.
#              c.     Repeat this process until the smaller number is zero.
# The larger number at this point is the GCD of A and B. Write a program that lets the user enter two integers and then prints each step in the process of using the Euclidean algorithm to find their GCD.

def gcd_finder(a, b):
    large_num = a
    small_num = b

    # this ensures the gcd is 0 if b is zero
    gcd = 0

    # this ensures a and b are whole positive numbers
    if a >= 0 and b >= 0:
        # this ensures a is always greater than or equal to b
        if b > a:
            a, b = b, a
        # if the small num is 0 then the gcd will print zero
        while small_num != 0:
            # now we began using Euclid's formula to find the gcd
            remainder = large_num % small_num
            large_num = small_num
            small_num = remainder
            gcd = large_num

        print(f"The greatest common divisor of {a} and {b} is {gcd}")

    else:
        print("You did not enter positive whole numbers.")

if __name__ == "__main__":
    num1 = int(input("Please enter first positive whole number: "))
    num2 = int(input("Please enter second positive whole number: "))

    gcd_finder(num1, num2)