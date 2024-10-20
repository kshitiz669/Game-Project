from turtle import Turtle

STARTING_POSITION =(0,-280)
MOVE_DISTANCE =    10
FINISH_LINE_Y =  280

class Player(Turtle):
    '''Sets up the player’s appearance (a turtle facing upward)
     and places it at the starting position using go_to_start().'''
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    '''Moves the player forward by MOVE_DISTANCE.
    '''
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        '''Moves the player back to the starting position after successfully crossing the finish line.
    '''
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    '''Returns True if the player’s Y-coordinate is greater than 
    FINISH_LINE_Y, indicating that the player has reached the finish line.
'''
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
