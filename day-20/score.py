from turtle import Turtle

with open("data.txt") as file:
    contents = file.read()


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = int(contents)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"score:{self.score} high score: {self.high_score}", False,
                   align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:

                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"score:{self.score} high score: {self.high_score}", False,
                   align="center", font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",
    #                align="center", font=("Arial", 30, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"score:{self.score} high score: {self.high_score}", False,
                   align="center", font=("Arial", 20, "normal"))
