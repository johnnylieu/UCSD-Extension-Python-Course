import datetime

def one_hundred(name, age):
    current_year = datetime.datetime.now().year
    years_to_one_hundred = 100 - age

    return(f'\nHi {name}, you will be 100 years old in the year {current_year + years_to_one_hundred}\n')


if __name__ == "__main__":
    name = input("Welcome, please input your name to begin: ")
    age = abs(int(input("& what is your age in whole numbers? ")))

    print(one_hundred(name, age))