# Michael Choi
# 11-7-24
# P4LAB1
# This program draws a square and a triangle using a while loop

# import drawing library
import turtle             
win = turtle.Screen()      
t = turtle.Turtle()    

# formatting
t.pensize(3)         
t.pencolor("red")     
t.shape("turtle")

# Draw a square
for thing in range(1,5):
    t.forward(50)          
    t.left(90)             

# Draw a triangle
for thing in range(1,4): 
    t.left(120)            
    t.forward(100)
# End commands
win.mainloop()             

