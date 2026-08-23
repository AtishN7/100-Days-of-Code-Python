import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

def fail_game():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()

def quit_game():
    global game_is_on
    game_is_on = False
    scoreboard.game_quit()

while game_is_on: 
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with player object
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            fail_game()

    # Detect successful crossing
    if player.crossed_car_traffic():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.next_car_traffic()

    #Give an option to player to quit
    screen.onkey(quit_game, "q")

screen.exitonclick()

