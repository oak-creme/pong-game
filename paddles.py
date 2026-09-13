from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 0.5)
        self.color("white")
        self.penup()
        self. goto(x, y)
