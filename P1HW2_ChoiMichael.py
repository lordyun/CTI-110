# Michael Choi
# 9-26-24
# P1HW2
# Calculate and display travel expenses
#
# DESIGN OF PROGRAM:
# INPUT:
# Display "Enter Budget: "
# Input real budget

# Display "Enter your travel destination: "
# Input string destination

# Display "How much do you think you will spend on gas?"
# Input real gas

# Display "Aproximately, how much will you need for accomodation/hotel?"
# Input real hotel

# Diplay "Last, how much do you need for food?"
# Input real food

# CALCULATIONS
# balance = budget - gas - hotel - food
# OUTPUT
# Display "------------Travel Expenses-----------"
# Display "Location: ", destination
# Display "Initial Budget: ", budget

# Display "Fuel: ", gas
# Display "Accomodation: ", hotel
# Display "Food: ", food

# Display "Remaining Balance: ", balance

budget = float(input('Enter Budget: '))
print()
destination = str(input('Enter your travel destination: '))
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
hotel = float(input('Approximately, how much will you need for accommodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))

balance = budget - gas - hotel - food

print()
print("------------Travel Expenses-----------")
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accommodation: ", hotel)
print("Food: ", food)
print()
print("Remaining Balance: ", balance)
