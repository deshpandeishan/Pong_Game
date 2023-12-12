from turtle import Turtle, Screen

screen = Screen


class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.screen.tracer(False)
        self.goto(0, -350)
        self.color("white")
        self.lt(90)
        self.draw_middle_line()

    def draw_middle_line(self):
        for _ in range(8):
            self.fd(25)
            self.penup()
            self.fd(25)
            self.pendown()


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.screen.tracer(False)
        self.goto(x, y)
        self.color("white")
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        self.scores = 0
        self.update_scores(self.scores)
        self.hideturtle()

    def update_scores(self, scores):
        self.write(f"{self.scores}", align='center', font=('Courier', 30, 'normal'))

