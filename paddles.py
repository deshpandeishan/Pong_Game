from turtle import Turtle, Screen

screen = Screen()
screen.listen()


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

    def move_left(self):
        screen.onkey(self.go_up, "Left")
        screen.onkey(self.go_down, "Right")

    def move_right(self):
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, "Down")
