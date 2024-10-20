from turtle import  Turtle
import random

COLORS = ["red","orange", "yellow","green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

'''Initializes the car manager with an empty list (all_cars) to store all the car objects and sets the initial car speed.
'''
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        '''Creates a new car randomly (1 in 6 chance) and gives it a random color and Y-position. It uses the 
        Turtle object to represent a car and then appends the new car to the all_cars list.'''
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    '''Moves all cars in the list backward (leftward on the screen) by their current speed (car_speed).'''
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    '''Increases the speed of the cars when the player reaches a new level.
'''
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
