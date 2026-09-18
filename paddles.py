from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 0.5)
        self.color("white")
        self.penup()
        self. goto(x, y)

    def up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 22.5)

    def down(self):
        if self.ycor() > - 240:
            self.sety(self.ycor() - 22.5)
