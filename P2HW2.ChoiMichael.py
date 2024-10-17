# Michael Choi
# 10-17-24
# P2HW2
# This program gets a student's grade for multiple modules and displays the lowest grade, highest grade, the sum of the grades, and the average grade

'''Get the grades for modules 1-6 from the user and store as a float.
Create a list that holds all the grades
Determine and display to the user the lowest grade
Determine and display to the user the highest grade
Determine and display to the user the sum of the grades
Determine and display to the user the average grade'''


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




