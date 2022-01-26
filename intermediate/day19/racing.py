from operator import indexOf
from turtle import Turtle, Screen, turtles
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=y_positions[i])
    
if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles():
        t.fd(random.randint(0, 10))
        #turtle의 크기 40*40
        if t.xcor() >= 230:
            winner = t.pencolor()
            is_race_on = False
            break


if user_bet == winner:
    screen.textinput(title="You Win!", prompt=f"You win, winner is {winner}")
else:
    screen.textinput(title="You Lose!", prompt=f"You Lose, winner is {winner}")

screen.exitonclick()