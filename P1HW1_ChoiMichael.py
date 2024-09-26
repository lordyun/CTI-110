# Michael Choi
# 9/24/2024
# P1HW1
# get input frorm user and perform calculations

print("-------Calculating Exponents------")
print()
print()

# get exponent input from user
baseValue = int(input("Enter an integer as the base value: "))
exponentValue = int(input("Enter an integer as the exponent value: "))

# calculations
exponentResult = baseValue ** exponentValue

print()
print()

# display output to the user
print(baseValue, "raised to the power of", exponentValue, "is", exponentResult, "!!")
                
print()
print()
print('-----Addition and Subtraction-----')
print()
print()
# get input from user
num1 = int(input('Enter a starting integer: '))
num2 = int(input('Enter an integer to add: '))
num3 = int(input('Enter an integer to subtract: '))

# calculations
num4 = num1 + num2 - num3

# display output to the user
print()
print()
print(num1, '+', num2, '-', num3, 'is equal to', num4)
