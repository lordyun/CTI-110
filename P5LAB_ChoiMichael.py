# Michael Choi
# 11-26-24
# P5LAB
# This program program calculates the most efficient way to divide a dollar amount into dollars and coins

import random


def main():
    # generate random number
    num = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${round(num, 2)}")

    # Get how much money the customer will pay
    payment = float(input("How much cash will you put into the self-checkout? "))
    change = payment - num

    # If not enough money, display error message
    if change < 0:
        payment = float(input(f"You still owe ${round(num - payment, 2)}! Enter how much more money you will pay: "))
        change = payment + change
        
    
    # Display change
    print(f"Your change is ${round(change, 2)}")

    # Multiply dollar amount by 100 to make calculations easier
    change = round(change * 100)
    disperse_change(change)


def disperse_change(change):
    # If amount is more than 0, determine the specific amounts of each coin/dollar
    if change > 0:
        # Determine how many dollars
        if change >= 100:
            dollars = change // 100
            if dollars > 1:
                print(f"{int(dollars)} dollars")
            elif dollars == 1:
                print(f"{int(dollars)} dollar")
        # Only take the remainder        
        rest = change % 100
        
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
    elif change == 0:
        print('No change')

if __name__ == "__main__":
    main()

