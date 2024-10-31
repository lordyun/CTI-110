# Michael Choi
# 10-29-24
# P3HW2
# This program calculates an employee's gross pay for a week, including overtime
'''
Display "Enter name:"
input name
Display "Enter hours worked: "
input hours
if hours < 0
    display "Invalid"
else
    Display "Enter pay rate: "
    input payRate
    if payRate < 7.50
        display "Invalid"
    else
        if hours < 0
            display "invalid"
        if hours > 40
            overtime = hours - 40
            overtimeRate = 1.5 * payRate
            overtimePay = overtime * overtimeRate
            regularPay = (hours - overtime) * payRate
        else:
            overtimePay = 0.0
            overtime = 0.0
            regularPay = hours * payRate
                    
        grossPay = overtimePay + regularPay
        Display name, hours, payRate, overimte, overtimePay, regularPay, grossPay
'''

name = input("Enter your name: ")
hours = float(input("Enter the amount of hours worked this week: "))
if hours < 0:
    print("Invalid input. Entries must be zero or greater. Please start the program again.")
else: 
    payRate = float(input("Enter your hourly pay rate: "))
    if payRate < 7.50:
        print("Invalid input. Entries must be 7.50 or greater. Please start the program again.")
    else:
        if hours < 0:
            print("Invalid input. Entries must be zero or greater. Please start the program again.")
        if hours > 40:
            overtime = hours - 40
            overtimeRate = 1.5 * payRate
            overtimePay = overtime * overtimeRate
            regularPay = (hours - overtime) * payRate
        else:
            overtimePay = 0.0
            overtime = 0.0
            regularPay = hours * payRate

        grossPay = overtimePay + regularPay
        
        print("----------------------------------------------")
        print(f"Employee name: {name}")
        print()
        print("Hours Worked    Pay Rate    Overtime    Overtime Pay    Regular Pay    Gross Pay")
        print("--------------------------------------------------------------------------------")
        print(f"{hours:<16.1f}{payRate:<12.1f}{overtime:<12.1f}${overtimePay:<16.2f}${regularPay:<15.2f}${grossPay:.2f}")
