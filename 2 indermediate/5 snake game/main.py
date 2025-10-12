from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) # Turn off the screen updates. changes will be shown only when screen.update() is called

snake = Snake() # Create an instance of the Snake class

screen.listen() # move snake on key press
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update() # Update the screen to show the new positions of all the segments
    time.sleep(0.1) # Pause for 0.1 seconds and them move the whole snake forward
    
    snake.move() # Move the snake forward




screen.exitonclick()    