import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract("intermediate\day18\colorset.jpg", 300)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
print(random.choice(rgb_colors))
t.colormode(255)
brush = t.Turtle()
brush.penup()
brush.hideturtle()
brush.speed("fast")
brush.setpos(-250, -250)

for i in range(10):
    brush.setpos(-250, -250 + (50* i))
    for j in range(10):
        brush.dot(20, random.choice(rgb_colors))
        brush.fd(50)

screen = t.Screen()
screen.exitonclick()
