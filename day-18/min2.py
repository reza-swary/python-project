from turtle import Turtle, Screen, colormode, pensize
import random as rn
timmy = Turtle()

screen = Screen()
# screen.exitonclick()

colormode(255)
timmy.pensize(10)
timmy.speed("fastest")


def color():
    r = rn.randint(30, 255)
    g = rn.randint(30, 255)
    b = rn.randint(30, 255)
    color = (r, g, b)
    return color


dir = [0, 90, 180, 270]


for _ in range(1000):
    timmy.color(color())
    timmy.forward(30)
    timmy.setheading(rn.choice(dir))
