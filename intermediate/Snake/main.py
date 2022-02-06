from turtle import Turtle, Screen, turtles
import snake

screen = Screen()
screen.bgcolor('black')

test = snake.snake_cell()
test2 = snake.snake_cell(1)

while True:
    test.move()
    test2.move()


screen.exitonclick()
