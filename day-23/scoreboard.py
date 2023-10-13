from turtle import Turtle


FONT = ("Courier", 15, "normal")
FONT2 = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.write(f"level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over", align="center", font=FONT2)
