def minutes_in_year():
    minutes_per_hour = 60
    hours_per_day = 24
    days_per_year = 365

    minutes = minutes_per_hour * hours_per_day * days_per_year
    return minutes

def main():
    minutes = minutes_in_year()
    print(f"The number of minutes in a year is {minutes}")

if __name__ == "__main__":
    main()