from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


RPAD_POS=(450,0)
LPAD_POS=(-450,0)

# Setup screen for the Pong game
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RPAD_POS)
l_paddle = Paddle(LPAD_POS)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick() 