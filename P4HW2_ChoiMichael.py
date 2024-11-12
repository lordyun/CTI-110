# Michael Choi
# 10-29-24
# P3HW2
# This program let's the user calculate the pay, including overtime, of any amount of employee's they want. Then upon terminating, displays the totals of all the employees. 


name = input("Enter employee's name or 'Done' to terminate: ")
employees = 0
overtimePayTotal = 0
regularPayTotal = 0
grossPayTotal = 0

while name.lower() != "done":
    hours = float(input(f"Enter the amount of hours {name} worked this week: "))
    while hours < 0:
        print("Invalid input. Entries must be zero or greater. Please try again.")
        hours = float(input(f"Enter the amount of hours {name} worked this week: "))
    payRate = float(input(f"Enter {name}'s hourly pay rate: "))
    while payRate < 7.50:
        print("Invalid input. Entries must be 7.50 or greater. Please try again.")
        payRate = float(input(f"Enter {name}'s hourly pay rate: "))
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

    employees += 1
    overtimePayTotal += overtimePay
    regularPayTotal += regularPay
    grossPayTotal += grossPay
        
    print("----------------------------------------------")
    print(f"Employee name: {name}")
    print()
    print("Hours Worked    Pay Rate    Overtime    Overtime Pay    Regular Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours:<16.1f}{payRate:<12.1f}{overtime:<12.1f}${overtimePay:<16.2f}${regularPay:<15.2f}${grossPay:.2f}")
    print()
    name = input("Enter employee's name or 'Done' to terminate: ")


print(f"Total number of employees entered: {employees}")
print(f"Total amount paid for overtime: {overtimePayTotal:.2f}")
print(f"Total amount paid for regular hours: {regularPayTotal:.2f}")
print(f"Total amount paid in gross: {grossPayTotal:.2f}")
print("The program has terminated.")