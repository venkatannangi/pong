from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# screen.screensize(600, 600)
screen.title("Pong")
# To turn of the animation
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    # When animation turnoff then we need to update the screen to show the
    screen.update()
    ball.move()

    # collide with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # collision with the right_paddle and left_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # if left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
