from turtle import Turtle

class snake_cell(Turtle):
    
    def __init__(self, pos=None):
        self.body = Turtle(shape="square")
        self.body.color("white")
        self.body.penup()
        if pos:
            self.body.setx(10)
            
    def move(self):
        self.body.fd(2)
