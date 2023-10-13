from turtle import Turtle , Screen
import random as r

all_turtle=[]

is_rase= False
tom =Turtle()
screen = Screen()
colors=["red","blue","green","black","orange","purple"]
y_pos=[-70,-40,-10,20,50,80]
user_bet = screen.textinput(title="Make your bet"  , prompt="which turtle will win?inter a color: ")
for num in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[num])
    tim.goto(-400,y=y_pos[num])
    all_turtle.append(tim)

if user_bet:
    is_rase = True
while is_rase:
    for tur in all_turtle:
        if tur.xcor() > 400 :
            is_rase = False
            wining_color = tur.pencolor()
            if wining_color == user_bet :
                print("you win")
            else:
                print(f"you lost! the {wining_color}")
        
        rand_dis=r.randint(0,10)
        tur.forward(rand_dis)
# def move_forwards():
#     tim.forward(10)
# def move_forwards1():
#     tom.forward(10)
# def clear():
#     tim.home()
#     tim.clear()
#     tom.home()
#     tom.clear()


# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="o", fun=move_forwards1)

# screen.onkey(key="c", fun=clear)
screen.exitonclick()
