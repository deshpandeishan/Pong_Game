import turtle
from turtle import Turtle, Screen
from scoreboards import LeftScoreBoard, RightScoreBoard, MiddleLine
# from paddles import Paddle
# import time

screen = Screen()
screen.setup(900, 900)
screen.title("Pong Game")
screen.bgcolor("black")


# sb_1 = LeftScoreBoard()
# sb_2 = RightScoreBoard()
# middle_line = MiddleLine()

screen.tracer(False)


def go_up():
    y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y)


def go_down():
    y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y)


paddle = Turtle()
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)
screen.tracer(True)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


# sb_1.increase_scores()
# sb_2.increase_scores()
# middle_line.draw_line()


screen.exitonclick()
