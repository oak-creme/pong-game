from turtle import Screen
import paddles
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)

screen.tracer(0)

user_paddle = paddles.Paddle(-350, 0)

computer_paddle = paddles.Paddle(350, 0)

ball = Ball()

scoreboard = ScoreBoard()

game_on = True

while game_on:
    screen.update()














screen.exitonclick()