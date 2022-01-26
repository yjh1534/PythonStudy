# #W = Forwards
# s = Backwards
# A = counter-Clockwise
# d = clockwise
# c = clear

import turtle as t

brush = t.Turtle()
screen = t.Screen()
def pressW():
    brush.fd(10)

def pressS():
    brush.backward(10)

def pressA():
    brush.left(5)

def pressD():
    brush.right(5)
    
def pressC():
    screen.resetscreen()


screen.listen()
screen.onkeypress(key="w", fun=pressW)
screen.onkeypress(key="s", fun=pressS)
screen.onkeypress(key="a", fun=pressA)
screen.onkeypress(key="d", fun=pressD)
screen.onkeypress(key="c", fun=pressC)

screen.exitonclick()