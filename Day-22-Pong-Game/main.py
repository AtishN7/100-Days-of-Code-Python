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
    time.sleep(0.05)
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor() > 385 or ball.ycor() < -385:
        ball.bounce_y()

    #detect collision with Paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    #detect ball out of bounds right side
    if ball.xcor() > 450:
        print("Ball out of range")
        ball.reset_position()

    # detect ball out of bounds right side
    if ball.xcor() < -450:
        print("Ball out of range")
        ball.reset_position()


screen.exitonclick() 