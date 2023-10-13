from turtle import Turtle, Screen
STARTING = [(0, 0), (-20, 0), (-40, 0)]
position = [0, 90, 180, 270]


class Snake:

    def __init__(self) -> None:
        self.seg = []
        self.cr_snake()

    def cr_snake(self):
        for i in STARTING:
            self.add_turtle(i)

    def add_turtle(self, i):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.speed("fastest")
        tim.goto(i)
        self.seg.append(tim)

    def extend(self):
        self.add_turtle(self.seg[-1].position())

    def reset(self):
        for se in self.seg:
            se.goto(1000, 1000)
        self.seg.clear()
        self.cr_snake()

    def move(self):
        for timmy in range(len(self.seg) - 1, 0, -1):
            tim_x = self.seg[timmy - 1].xcor()
            tim_y = self.seg[timmy - 1].ycor()
            self.seg[timmy].goto(tim_x, tim_y)
        self.seg[0].forward(20)

    def up(self):
        if self.seg[0].heading() != 270:
            self.seg[0].setheading(90)

    def down(self):
        if self.seg[0].heading() != 90:
            self.seg[0].setheading(270)

    def left(self):
        if self.seg[0].heading() != 0:
            self.seg[0].setheading(180)

    def right(self):
        if self.seg[0].heading() != 180:
            self.seg[0].setheading(0)

    #     add_x = self.seg[-1].xcor() - 20
    #     add_y = self.seg[-1].ycor() - 20
    #     STARTING.append((add_x, add_y))
