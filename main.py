from turtle import Screen
import paddles
import scoreboard
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

game_score = ScoreBoard()


#paddle movement
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.down, "Down")

screen.onkeypress(computer_paddle.up, "w")
screen.onkeypress(computer_paddle.down, "s")


game_on = True

while game_on:

    game_score.update_scoreboard()

    time.sleep(ball.move_speed)
    ball.move()

    #bounce physics from both paddles and walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if (ball.distance(computer_paddle) < 100 and ball.xcor() > 330) or (ball.distance(user_paddle) < 100 and ball.xcor() < -330):
        ball.x_bounce()

    #ball goes out of bounds, assign points
    if ball.xcor() > 390:
        game_score.add_user_point()
        ball.reset()
    if ball.xcor() < -390:
        game_score.add_user_point()
        ball.reset()

    #first to 5 points wins, game over
    if game_score.user_score >= 5:
        game_score.update_scoreboard()
        print("user wins !")
        game_on = False
    elif game_score.computer_score >= 5:
        game_score.update_scoreboard()
        print("computer wins\nur asscheeks")
        game_on = False

    screen.update()













screen.exitonclick()