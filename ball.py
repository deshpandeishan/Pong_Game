from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(2, 2)
        self.color("blue")

    def move(self):
        x_cor = self.xcor() + 10
        y_cor = self.ycor() + 10
        self.goto(x_cor, y_cor)
