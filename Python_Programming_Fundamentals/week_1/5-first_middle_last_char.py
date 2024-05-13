"""Exercise Question 3: Given 2 strings, s1, and s2, return a new string made of the first, middle and last char each input string
Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan"""

def first_middle_last_char(s1, s2):
    new_str = ""
    new_str = new_str + s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]

    return new_str

if __name__ == "__main__":
    s1 = "America"
    s2 = "Japan"

    print(first_middle_last_char(s1, s2))