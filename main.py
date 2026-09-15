from turtle import Screen
import paddles
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.listen()

screen.tracer(0)

user_paddle = paddles.Paddle(-350, 0)
computer_paddle = paddles.Paddle(350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(user_paddle.up, "Up")
screen.onkeyrelease(user_paddle.stop, "Up")

screen.onkeypress(user_paddle.down, "Down")
screen.onkeyrelease(user_paddle.stop, "Down")



game_on = True

while game_on:
    screen.update()














screen.exitonclick()