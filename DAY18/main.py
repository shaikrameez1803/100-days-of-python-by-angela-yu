import turtle
import random

# Take inputs first
n = int(input("Enter total number of dots: "))
m = int(input("Enter number of dots per line: "))

# Create screen after input
screen = turtle.Screen()
turtle.colormode(255)
screen.bgcolor("white")

tim = turtle.Turtle()
tim.speed(0)
tim.hideturtle()
tim.penup()

# Colors in SINGLE LINE
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,165,0),(128,0,128),(255,20,147),(0,191,255),(34,139,34),(255,105,180),(75,0,130),(255,215,0),(50,205,50)]

# Move to start position
tim.setheading(225)
tim.forward(200)
tim.setheading(0)

# Draw ALL dots (including remaining)
for i in range(n):
    tim.dot(40, random.choice(colors))
    tim.forward(50)

    # Move to next row after m dots
    if (i + 1) % m == 0:
        tim.backward(50 * m)
        tim.left(90)
        tim.forward(50)
        tim.right(90)

# Keep window open until click
screen.exitonclick()