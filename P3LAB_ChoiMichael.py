# Michael Choi
# 10-24-24
# P3LAB
# This program program calculates the most efficient way to divide a dollar amount into dollars and coins

# Get dollar amount from user
total = float(input("Enter a dollar amount: "))

# Multiply dollar amount by 100 to make calculations easier
total = round(total * 100)


# If amount is more than 0, determine the specific amounts of each coin/dollar
if total > 0:
    # Determine how many dollars
    if total >= 100:
        dollars = total // 100
        if dollars > 1:
            print(f"{int(dollars)} dollars")
        elif dollars == 1:
            print(f"{int(dollars)} dollar")
    # Only take the remainder        
    rest = total % 100
    
    # Determine how many quarters
    if rest > 0:
        quarters = rest // 25
        if quarters > 1:
            print(f"{int(quarters)} quarters")
        elif quarters == 1:
            print(f"{int(quarters)} quarter")
    # Only take the remainder 
    rest = rest % 25
    # Determine how many dimes    
    if rest > 0:
        dimes = rest // 10
        if dimes > 1:
            print(f"{int(dimes)} dimes")
        elif dimes == 1:
            print(f"{int(dimes)} dime")
    # Only take the remainder 
    rest = rest % 10
    # Determine how many nickels
    if rest > 0 :
        nickels = rest // 5
        if nickels > 1:
            print(f"{int(nickels)} nickels")
        elif nickels == 1:
            print(f"{int(nickels)} nickel")
    # Only take the remainder 
    rest = rest % 5
    # Determine how many pennies
    if rest > 0:
        pennies = rest / 1
        if pennies > 1:
            print(f"{int(pennies)} pennies")
        elif pennies == 1: 
             print(f"{int(pennies)} penny")
# If amount is 0, display message
elif total == 0:
    print('No change')

# If amount is less than 0, display message
elif total < 0:
    print("Invalid amount, please try again")

  






   
