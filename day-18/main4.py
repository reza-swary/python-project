from turtle import Turtle, Screen, colormode, pensize
import random as rn
timmy = Turtle()


colormode(255)
timmy.speed("fastest")
timmy.penup()


def color():
    r = rn.randint(30, 255)
    g = rn.randint(30, 255)
    b = rn.randint(30, 255)
    color = (r, g, b)
    return color


timmy.setheading(219)
timmy.forward(570)
timmy.setheading(0)
for _ in range(19):
    for _ in range(19):
        timmy.dot(20, color())
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(950)
    timmy.setheading(0)
