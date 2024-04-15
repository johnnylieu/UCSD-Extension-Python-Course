"""The Payroll Department keeps a list of employee information for each pay period in a text file. The format of each line of the file is the following:

                  <last name> <hours worked> <hourly wage>

 Write a program that inputs data from a list and prints to the terminal a report of the wages paid to the employees for the given period.
 The report should be in tabular format with the appropriate header. Each line should contain an employee’s name, the hours worked,
 and the wages paid for that period. Use the following list or tuples to extract the report information:

             [(“Lambert”, 34, 10.50), (“Osborne”, 22, 6.25), (“Giacometti”, 5, 100.70)]"""

def start_employee_management_sw():
    employees = [('Lambert', 34, 10.50), ('Osborne', 22, 6.25), ('Giacometti', 5, 100.70)]

    # I had to google this, the \t to create tabs.
    print("Employee Name\tHours Worked\tEmployee Hourly Pay")
    for employee in employees:
        employee_name, hours_worked, hourly_wage = employee

        print(f'{employee_name}\t\t{hours_worked}\t\t{hourly_wage}\t\tPaid: ${hours_worked * hourly_wage:.2f}')

if __name__ == "__main__":
    start_employee_management_sw()