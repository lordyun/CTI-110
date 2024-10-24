# Michael Choi
# 10-24-24
# P3HW1
# This program gets a student's grade for multiple modules and displays the lowest grade, highest grade, the sum of the grades, and the average grade, then displays the user's letter grade

'''Get the grades for modules 1-6 from the user and store as a float.
Create a list that holds all the grades
Determine and display to the user the lowest grade
Determine and display to the user the highest grade
Determine and display to the user the sum of the grades
Determine and display to the user the average grade
Determine and display to the user their letter grade'''


grade1 = float(input("Enter your grade for Module 1: "))
grade2 = float(input("Enter your grade for Module 2: "))
grade3 = float(input("Enter your grade for Module 3: "))
grade4 = float(input("Enter your grade for Module 4: "))
grade5 = float(input("Enter your grade for Module 5: "))
grade6 = float(input("Enter your grade for Module 6: "))
print()

gradeList = [grade1, grade2, grade3, grade4, grade5, grade6]

print("----------Results----------")
print(f"{'Lowest Grade:':<20}{min(gradeList):.2f}")
print(f"{'Highest Grade:':<20}{max(gradeList):.2f}")
print(f"{'Sum of Grades:':<20}{sum(gradeList):.2f}")
print(f"{'Average:':<20}{sum(gradeList)/len(gradeList):.2f}")
print("---------------------------")

if (sum(gradeList)/len(gradeList)) > 100:
    print('Your grade is: A+')
elif(sum(gradeList)/len(gradeList)) >= 89.5:
    print('Your grade is: A')
elif (sum(gradeList)/len(gradeList)) >= 79.5:
    print('Your grade is: B')
elif (sum(gradeList)/len(gradeList)) >= 69.5:
    print('Your grade is: C')
elif (sum(gradeList)/len(gradeList)) >= 59.5:
    print('Your grade is: D')
elif (sum(gradeList)/len(gradeList)) >= 49.5:
    print('Your grade is: F')
else:
    print('Your grade is: F')   
    print("You might want to consider getting a tutor...")
    



