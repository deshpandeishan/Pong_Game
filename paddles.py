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
        self.goto(400, 0)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

    def track_instructions(self):
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, "Down")

