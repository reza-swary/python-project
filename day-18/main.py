from turtle import Turtle, Screen, colormode
import random as rn
timmy = Turtle()

screen = Screen()
# screen.exitonclick()

colormode(255)
timmy.pensize(3)
timmy.speed("fastest")


def color():
    r = rn.randint(20, 255)
    g = rn.randint(20, 255)
    b = rn.randint(20, 255)
    color = (r, g, b)
    return color


x = 4
for _ in range(100):
    y = 360 / (x - 1)
    for i in range(1, x):

        timmy.forward(100)
        timmy.left(y)
        timmy.color(color())
    x += 1
