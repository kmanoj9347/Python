#Write the python code to create character ‘A’ on the screen using turtle graphics with
#absolute positioning
import turtle

# Setup turtle window
window = turtle.Screen()
window.setup(500, 500)  # Set the window size
window.title("Character 'A'")

# Create turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Absolute positioning of the turtle
pen.penup()
pen.goto(-100, 0)  # Starting position of 'A'
pen.pendown()

# Draw the character 'A'
pen.left(75)
pen.forward(200)
pen.right(150)
pen.forward(200)
pen.backward(80)
pen.right(105)
pen.forward(62)

# Hide the turtle
pen.hideturtle()

# Keep the window open until it's closed manually
turtle.done()