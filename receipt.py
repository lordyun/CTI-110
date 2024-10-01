# Michael Choi
# 10-1-24
# In class Assignment
# Create a receipt, calculate total cost from purchase

# DESIGN OR PROGRAM

# INPUT:
# Display "Enter the name of Item 1: "
# input string item1
# Display "What is the price of Item 1?"
# input float price1
# Display "What quantity of Item 1 did you buy?"
# input int quantity1
# Display "Enter the name of Item 2: "
# input string item2
# Display "What is the price of Item 2?"
# input float price2
# Display "What quantity of Item 2 did you buy?"
# input int quantity2
# Display "Enter the name of Item 3: "
# input string item3
# Display "What is the price of Item 3?"
# input float price3
# Display "What quantity of Item 3 did you buy?"
# input int quantity3

# CALCULATIONS
# subtotal = price1 * quantity1 + price2 * quantity2 + quantity3 * price3
# tax = subtotal * 0.07
# total = subtotal + tax

# OUTPUT
# Display top of the receipt


item1 = input('Enter the name of Item 1: ')
price1 = float(input(f"Enter the price of {item1}: "))
quantity1 = int(input(f"Enter the quantity of {item1}: "))
print()
item2 = input('Enter the name of Item 2: ')
price2 = float(input(f"Enter the price of {item2}: "))
quantity2 = int(input(f"Enter the quantity of {item2}: "))
print()
item3 = input('Enter the name of Item 3: ')
price3 = float(input(f"Enter the price of {item3}: "))
quantity3 = int(input(f"Enter the quantity of {item3}: "))

subtotal = price1 * quantity1 + price2 * quantity2 + quantity3 * price3
tax = subtotal * 0.07
total = subtotal + tax
print()
print()
print("Thanks for shopping at Choi's Toys!")
print("-" * 34)
item = "ITEM"
quantity = "QUANTITY"
itemTotal = "ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{itemTotal}")
print()
print(f"{item1:<20}{quantity1:<15}${price1 * quantity1:.2f}\n")
print(f"{item2:<20}{quantity2:<15}${price2 * quantity2:.2f}\n")
print(f"{item3:<20}{quantity3:<15}${price3 * quantity3:.2f}\n")
print()
print(f"Your subtotal is: ${subtotal:.2f}")
print(f"Your tax is: ${tax}")
print(f"Your total is: ${total:.2f}")


