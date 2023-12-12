from turtle import Turtle, Screen
screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_cor = 0
        self.y_cor = 0
        self.goto(self.x_cor, self.y_cor)
        self.penup()
        self.shape("circle")
        self.shapesize(2, 2)
        self.color("blue")


screen.exitonclick()
