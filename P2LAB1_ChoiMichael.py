# Michael Choi
# 10-08-24
# P2LAB1
# Calculating the area of a triangle using Python's built-in math library

# import math library
import math

# get radius from user
radius = float(input("Enter the radius of the circle: "))
print()

# calculations
diameter = radius * 2
circum = radius * 2 * math.pi
area = math.pi * math.pow(radius, 2)

# output
print(f"The diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circum:.2f}\n")
print(f"The area of the circle is {area:.3f}\n")

