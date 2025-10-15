from turtle import Turtle




STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def go_to_start(self):
        """Resets the player to the bottom starting position."""
        self.goto(STARTING_POSITION)
        
    def move_up(self):
        """
        Moves the player forward. 
        If the player crosses the finish line, they are automatically reset to the start.
        """
        if self.ycor() >= FINISH_LINE_Y:
            self.go_to_start()
        else:
            self.forward(MOVE_DISTANCE)
        
    def is_at_finish_line(self):
        """Returns True if the turtle is at or beyond the finish line."""
        return self.ycor() > FINISH_LINE_Y

