from turtle import Screen
from scoreboards import ScoreBoard, MiddleLine
from paddles import Paddle

screen = Screen()
screen.setup(900, 900)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(False)
sb_1 = ScoreBoard(-100, 300)
sb_2 = ScoreBoard(100, 300)
middle_line = MiddleLine()

paddle1 = Paddle(-400, 0)
paddle2 = Paddle(400, 0)

paddle1.move_left()

paddle2.move_right()
screen.tracer(True)

middle_line.draw_middle_line()

screen.exitonclick()
