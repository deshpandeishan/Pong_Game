from turtle import Turtle

score1 = Turtle()
score2 = Turtle()


class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, -350)
        self.color("white")
        self.lt(90)
        self.hideturtle()
        self.draw_middle_line()

    def draw_middle_line(self):
        for _ in range(8):
            self.fd(25)
            self.penup()
            self.fd(25)
            self.pendown()


class LeftScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.tracer(False)
        self.goto(-100, 300)
        self.color("white")
        self.penup()
        self.score_1 = 0
        self.update_left_scores()
        self.hideturtle()

    def increase_scores(self):
        self.score_1 += 1
        self.clear()
        self.update_left_scores()

    def update_left_scores(self):
        self.write(f"{self.score_1}", align='center', font=('Courier', 30, 'normal'))


class RightScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.tracer(False)
        self.goto(100, 300)
        self.color("white")
        self.penup()
        self.score_2 = 0
        self.update_right_scores()
        self.hideturtle()

    def increase_scores(self):
        self.score_2 += 1
        self.clear()
        self.update_right_scores()

    def update_right_scores(self):
        self.write(f"{self.score_2}", align='center', font=('Courier', 30, 'normal'))
