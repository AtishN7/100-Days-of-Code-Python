from turtle import Turtle
FONT = ("Georgia", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-260, 280)
        self.increase_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align="CENTER", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\n Final Level: {self.level}", align="CENTER", font=FONT)

    def game_quit(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Final Level: {self.level}", align="CENTER", font=FONT)
