# Write a set of instructions for controlling the turtle to draw a line from the top-left
#corner of the screen to the bottom-right corner, and from the top-right corner to the
#bottom-left corner, thereby making a big X on the screen. There should be no other
#lines drawn on the screen.
import turtle

# Setup turtle window
window = turtle.Screen()
window.setup(500, 500)  # Set the window size
window.title("Big X")

# Create turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Move to top-left corner
pen.penup()
pen.goto(-200, 200)
pen.pendown()

# Draw line from top-left to bottom-right
pen.goto(200, -200)

# Move to top-right corner
pen.penup()
pen.goto(200, 200)
pen.pendown()

# Draw line from top-right to bottom-left
pen.goto(-200, -200)

# Hide the turtle
pen.hideturtle()

# Keep the window open until it's closed manually
turtle.done()