"""Fibonacci Sequence is the series of positive numbers that is created by add the previous two numbers to create the next number in a sequence. 
For example, A Fibonacci sequence starts with the number 1. 
Then next number adds the two that number plus the previous number which happens to be 0+1 so the sequence would now be 0+1 = 1 giving us the sequence 1, 1, 
The next number is created by add these two 1+1 = 2 giving us 1,1,2 
and so on until we have 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...
Write a recursive function that asks the user how many Fibonacci numbers to generate and then generates them."""

def generate_fib():
    count = abs(int(input("How many Fibonacci numbers do you want to generate? ")))
    fib = [0, 1]

    if type(count) != int:
        return "You did not choose a number."

    if count == 0:
        return "Number has to be greater than zero."
    elif count == 1:
        return 0
    else:
        for i in range(2, count):
            total = fib[i-2] + fib[i-1]
            fib.append(total)

        return fib

if __name__ == '__main__':
    print(generate_fib())