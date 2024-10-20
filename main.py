import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

'''Sets up the window size to 600x600 and disables automatic screen updates (tracer(0)), allowing manual updates.
'''
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager =CarManager()
scoreboard =Scoreboard()

'''screen.onkey(player.go_up, "Up"): Binds the "Up" arrow key to the player's movement.'''
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
'''while game_is_on: Runs the game as long as game_is_on is True.
The loop updates the screen every 0.1 seconds.
It calls car_manager.create_car() to potentially create a new car and moves the existing cars with move_cars().'''
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    '''Loops through all cars and checks if any car is close to the player using car.distance(player). 
    If a car is too close (less than 20 units), it ends the game and displays "GAME OVER" on the screen.'''
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #Detect successful crossing
    '''If the player reaches the finish line (player.is_at_finish_line()), 
    the player returns to the starting position, the car speed increases, 
    and the scoreboard updates to show the new level.'''
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
