import turtle

#create a turtle object
my_turtle = turtle.Turtle()

#Set the turtle speed (optional)
my_turtle.speed(1)

#Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-100,0) 
my_turtle.pendown()

# Draw the character 'A'
my_turtle.goto(-50,100)
my_turtle.goto(0,0)
my_turtle.goto(0,50)
my_turtle.goto(0,50)
my_turtle.goto(-50,100)

#Hide the turtle
my_turtle.hideturtle()

turtle.done()