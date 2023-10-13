from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score1 = 0

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.write(self.score1, align="center", font=("courier", 80, "normal"))

    def add_score(self):
        self.clear()
        self.score1 += 1
        self.write(self.score1, align="center", font=("courier", 80, "normal"))
