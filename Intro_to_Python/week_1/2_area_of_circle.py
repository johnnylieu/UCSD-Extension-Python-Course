import math

def calculate_area(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input('What is the radius? '))
    area = calculate_area(radius)
    print(f'The area of a circle with radius of {radius} is {area}')

if __name__ == "__main__":
    main()