from turtle import Turtle

score1 = Turtle()
score2 = Turtle()


# class MiddleLine(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.goto(0, -900)
#         self.color("red")
#         self.draw_line()
#
#     def draw_line(self):
#         self.color('white')
#         self.fd(100)
#         self.penup()
#         self.fd(100)
#         self.pendown()


class LeftScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.goto(-100, 250)
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
        self.goto(100, 250)
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
