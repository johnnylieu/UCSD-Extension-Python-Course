# The German mathematician Gottfried Leibniz developed the following method to approximate the value of pi :   p i/4  =  1  -  1/3  + 1/5  - 1/7 + . . .
# Write a program that allows the user to specify the number of iterations used in this approximation and that displays the resulting value.

def main():
    pi = 0
    denominator = 1

    iterations = int(input("Enter number of iterations (1 or greater): "))

    for i in range(iterations):
        if i % 2==0:
            pi += 4/denominator
            denominator += 2
        else:
            pi -= 4/denominator
            denominator += 2

    print(pi)


if __name__ == "__main__":
    main()