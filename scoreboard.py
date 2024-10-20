from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    '''Initializes the scoreboard with the starting level (1) and hides the turtle icon.
    It places the scoreboard in the top left corner of the screen and calls
     update_scoreboard() to display the level.'''
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
    '''Clears the previous level text and writes the current level on the screen.
    '''
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    '''Increases the level by 1 and updates the scoreboard.
    '''
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    '''Displays "GAME OVER" in the center of the screen when the game ends.
    '''
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
