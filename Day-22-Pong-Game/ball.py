from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_shift = 6
        self.y_shift = 6
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_shift
        new_y = self.ycor() + self.y_shift
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_shift *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_shift *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.05
