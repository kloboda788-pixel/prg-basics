###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle, figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Square 1
pen.penup()
pen.goto(-250, 200)
pen.pendown()
figures.draw_square(pen, 80)

# Square 2
pen.penup()
pen.goto(50, 200)
pen.pendown()
figures.draw_square(pen, 50)

# Triangle 1
pen.penup()
pen.goto(-250, 0)
pen.pendown()
figures.draw_triangle(pen, 80)

# Triangle 2
pen.penup()
pen.goto(50, 0)
pen.pendown()
figures.draw_triangle(pen, 120)

# Rectangle 1
pen.penup()
pen.goto(-250, -200)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

# Rectangle 2
pen.penup()
pen.goto(50, -200)
pen.pendown()
figures.draw_rectangle(pen, 60, 100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()