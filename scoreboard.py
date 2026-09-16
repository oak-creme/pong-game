from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.user_score = 0
        self.computer_score = 0
        self.goto(-100, 200)
        self.write(self.user_score, False, "center", ("Arial", 32, "bold"))
        self.goto(100, 200)
        self.write(self.computer_score, False, "center", ("Arial", 32, "bold"))

    def add_user_point(self):
        self.user_score += 1

    def add_computer_point(self):
        self.computer_score += 1
