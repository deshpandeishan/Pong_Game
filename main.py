from turtle import Turtle, Screen
from scoreboards import LeftScoreBoard, RightScoreBoard, MiddleLine

screen = Screen()
screen.setup(900, 900)
screen.bgcolor("black")

# middle_line = MiddleLine()

sb_1 = LeftScoreBoard()
sb_2 = RightScoreBoard()

# middle_line.draw_line()

sb_1.increase_scores()
sb_2.increase_scores()

screen.exitonclick()
