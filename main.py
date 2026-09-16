from turtle import Screen
import paddles
from ball import Ball
from scoreboard import ScoreBoard
import time

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

screen.onkeypress(computer_paddle.up, "w")
screen.onkeyrelease(computer_paddle.stop, "w")

screen.onkeypress(computer_paddle.down, "s")
screen.onkeyrelease(computer_paddle.stop, "s")


game_on = True

while game_on:

    time.sleep(0.05)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if (ball.distance(computer_paddle) < 100 and ball.xcor() > 330) or (ball.distance(user_paddle) < 100 and ball.xcor() < -330):
        ball.x_bounce()

    if ball.xcor() > 390:
        ball.reset()
    if ball.xcor() < -390:
        ball.reset()



    screen.update()













screen.exitonclick()