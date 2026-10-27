# Davidson Michaud
# 10/22/2026
# Use loops to draw a square and a triangle
import turtle

# Set up the window
window = turtle.Screen()

# Make the turtle object
bob = turtle.Turtle()

# Change the size and color of the lines
bob.pensize(5)
bob.pencolor("Blue")

# Draw the square
for side in range(4):
    bob.forward (100)
    bob.right (90)
    
# While loop to draw the roof
num = 0
while num < 3:
    num = num + 1
    bob.forward(100)
    bob.left(120)
    

window.mainloop()