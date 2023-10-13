from turtle import Turtle, Screen, shape
from pandas import *

screen = Screen()
screen.title("U.S._states_game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)
guessed = []
while len(guessed) < 50:
    data = read_csv("50_states.csv")
    all_states = data.state.to_list()

    answer = screen.textinput(title=f"{len(guessed)}/50 guess the state",
                              prompt="whats another states name? ").title()
    if answer == "Exit":
        break
    elif answer in all_states:
        t = Turtle()
        t.penup()
        position = data[data.state == answer]
        t.goto(int(position.x), int(position.y))
        t.write(answer)
        guessed.append(answer)


screen.exitonclick()
