# Michael Choi
# 10-10-24
# P2LAB2
# Creat a dictionary and use the key value pairs to compare mpg of cars

# Create the dictionary
carMPG = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# print the keys for the user
print(carMPG.keys())
print()

# ask the user to enter a key
answer = (input("Enter a vehicle to see its gas mileage: "))
print()

# display the key and its value
print(f"The {answer} gets {(carMPG[answer])} mpg.")
print()

# get how many miles the user will drive
miles = float(input(f"How many miles will you drive the {answer}? "))
print()

# calculate and display how many gallons needed

gallonsNeeded = miles / carMPG[answer]

print(f"{gallonsNeeded:.2f} gallon(s) of gas are need to drive the {answer} {miles} miles.")
          



