from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """Clears and rewrites the current level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}",  align='left', font=FONT)
        
    def increase_level(self):
        """Increments the level and updates the display."""
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        """Writes 'GAME OVER' in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align='left', font=FONT)