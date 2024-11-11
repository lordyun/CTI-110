# Michael Choi
# 11-11-24
# P4HW1
# This program uses loops to calculate the letter grade for a user specified number of grades

'''
Get the number of grades the user wants to enter
create an empty list for the grades
create a for loop with a range of 1 to the number of grades the user wants to enter plus one
get each grade from the user
if a grade is less than 0 or great than 100, display an error/retry message
add each grade to the grade list
display the lowest grade in the list and then remove it from the list
display the new list
display the average of the list
use if else statements to determine the letter grade based off the average of the list
'''


num = int(input("Enter how many grades you want to enter: "))
gradeList = []
for grade in range(1, num + 1):
    var = float(input(f"Enter grade {grade}: "))
    if var < 0 or var > 100:
            var = float(input(f"Invalid entry. Please enter another grade between 0 and 100 for grade {grade}: "))
    gradeList.append(var)

print("-------------Results------------")
print(f"{'Lowest Grade:':<20}{min(gradeList):.2f}")
gradeList.remove(min(gradeList))
print(f"{'Modified List: ':<20}{gradeList}")
print(f"{'Average Grade:':<20}{sum(gradeList)/len(gradeList):.2f}")                             

if (sum(gradeList)/len(gradeList)) > 100:
    print(f"{'Grade: ':<20}{'A+'}")
elif(sum(gradeList)/len(gradeList)) >= 89.5:
    print(f"{'Grade: ':<20}{'A'}")
elif (sum(gradeList)/len(gradeList)) >= 79.5:
    print(f"{'Grade: ':<20}{'B'}")
elif (sum(gradeList)/len(gradeList)) >= 69.5:
    print(f"{'Grade: ':<20}{'C'}")
elif (sum(gradeList)/len(gradeList)) >= 59.5:
    print(f"{'Grade: ':<20}{'D'}")
elif (sum(gradeList)/len(gradeList)) >= 49.5:
    print(f"{'Grade: ':<20}{'F'}")
else:
    print(f"{'Grade: ':<20}{'F'}")  
    print("You might want to consider getting a tutor...")
