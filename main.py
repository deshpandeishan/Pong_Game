from turtle import Screen
from scoreboards import LeftScoreBoard, RightScoreBoard, MiddleLine
from paddles import Paddle

screen = Screen()
screen.setup(900, 900)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(False)
sb_1 = LeftScoreBoard()
sb_2 = RightScoreBoard()
middle_line = MiddleLine()

paddle1 = Paddle()
paddle2 = Paddle()

paddle1.setup(-400, 0)
paddle1.track_left()

paddle2.setup(400, 0)
paddle2.track_right()
screen.tracer(True)

sb_1.increase_scores()
sb_2.increase_scores()
middle_line.draw_middle_line()

screen.exitonclick()
