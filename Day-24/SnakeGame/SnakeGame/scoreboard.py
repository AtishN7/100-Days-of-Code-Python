from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hiscore = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("hiscore_data.txt", mode="r") as read_file:
            self.hiscore = int(read_file.read())
        self.write(f"Score: {self.score} High Score: {self.hiscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hiscore:
            self.hiscore = self.score
            with open("hiscore_data.txt", mode="w") as file_edit:
                file_edit.write(f"{str(self.hiscore)}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
