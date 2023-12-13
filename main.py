from turtle import Screen
from scoreboards import ScoreBoard, MiddleLine
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(900, 900)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(0)
left_sb = ScoreBoard(-100, 300)
right_sb = ScoreBoard(100, 300)
middle_line = MiddleLine()

left_paddle = Paddle(-400, 0)
right_paddle = Paddle(400, 0)

left_paddle.move_left()
right_paddle.move_right()
ball = Ball()
middle_line.draw_middle_line()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # This code will detect the ball's collision with wall (Top)
    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.y_bounce()

    # This code will detect and bounce back after the ball has collided with any of two paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()
        if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
            right_sb.update_scores()
        else:
            left_sb.update_scores()

screen.exitonclick()
