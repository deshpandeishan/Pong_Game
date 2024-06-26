from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(2, 2)
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.moving_speed *= 0.9
        self.x_move *= -1

    def reset_ball_cor(self):
        self.moving_speed = 0.1
        self.x_move *= -1
        self.goto(0, 0)
