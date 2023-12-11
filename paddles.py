from turtle import Turtle, Screen

screen = Screen()
screen.listen()


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def setup(self, x, y):
        self.goto(x, y)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

    def track_left(self):
        screen.onkey(self.go_up, "Left")
        screen.onkey(self.go_down, "Right")

    def track_right(self):
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, "Down")
