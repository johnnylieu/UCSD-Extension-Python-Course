"""Write a function or set of functions that asks a user for a number and determine whether the number is prime or not. 
Recall that a prime number is a number that has no divisors."""

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    user_input = abs(int(input("Enter a positive whole number: ")))
    is_prime(user_input)

    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")