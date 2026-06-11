from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=100, y=250)
        self.write(arg=self.l_paddle_score, align=ALIGNMENT, font=FONT)
        self.goto(x=-100, y=250)
        self.write(arg=self.r_paddle_score, align=ALIGNMENT, font=FONT)

    def add_l_paddle_point(self):
        self.l_paddle_score += 1
        self.update_score()

    def add_r_paddle_point(self):
        self.r_paddle_score += 1
        self.update_score()