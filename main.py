from turtle import Screen
from scoreboards import LeftScoreBoard, RightScoreBoard, MiddleLine
from paddles import Paddle
# import time

screen = Screen()
screen.setup(900, 900)
screen.title("Pong Game")
screen.bgcolor("black")


sb_1 = LeftScoreBoard()
sb_2 = RightScoreBoard()
middle_line = MiddleLine()
paddle = Paddle()

sb_1.increase_scores()
sb_2.increase_scores()
middle_line.draw_line()
# paddle.setup()

screen.exitonclick()
