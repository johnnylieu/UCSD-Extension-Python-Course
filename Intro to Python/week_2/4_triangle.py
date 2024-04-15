# Write a program that accepts the lengths of three sides of a triangle as inputs.
# The program output should indicate whether or not the triangle is an equilateral
# triangle (e.g. all three sides are equal).

def main():
    side_a = int(input("Use an integer to determin the lengh of side A of a triangle: "))
    side_b = int(input("Use an integer to determin the lengh of side B of a triangle: "))
    side_c = int(input("Use an integer to determin the lengh of side C of a triangle: "))

    if side_a == side_b == side_c:
        print("This triangle is an equilateral.")
    else:
        print("This triangle is not an equilateral.")

if __name__ == "__main__":
    main()