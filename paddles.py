from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(10, 0)
        self.lt(90)

    def setup(self):
        self.color("white")
        self.shape("square")
        self.shapesize(1, 3)

    # def move_left(self):
    #     self.goto(self.x_cor, self.y_cor + 30)
    #
    # def move_right(self):
    #     self.goto(self.x_cor, self.y_cor + -30)
