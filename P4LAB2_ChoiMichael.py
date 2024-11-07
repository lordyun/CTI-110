# Michael Choi
# 11-7-24
# P4LAB2
# This program gets a number from the user and  displays it's multiplication table up to 12. The program will run as many times as the user wants

# Run at least once and then as many times as the user wants
answer = "Yes"
while answer.lower() == "yes":
# Get number from user
    num = int(input("Enter an integer: "))
# If the number is negative, have the user try again
    while num < 0:
        num = int(input("This program does not handle negative numbers. Please try again: "))
# Multiply the number by values 1-12 and then display the table
    myList = [1,2,3,4,5,6,7,8,9,10,11,12,]
    for thing in myList:
        print(f"{num} * {thing} = {num * thing}")
# Ask user if they want to run the program again    
    answer = input("Would you like to run the program again? Enter 'Yes' or 'No': ")
# Give an exit statement
print()
print("The program has ended.")
    
    
   

    
    
