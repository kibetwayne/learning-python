import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) # Turn off the screen updates. changes will be shown only when screen.update() is called

#creating instances
snake = Snake() 
food = Food() 
Scoreboard = Scoreboard() 

# move snake on key press
screen.listen() 
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update() # Update the screen to show the new positions of all the segments
    time.sleep(0.1) # Pause for 0.1 seconds and them move the whole snake forward
    
    #detect collision with food
    if snake.head.distance(food) < 15: # If the distance between the head of the snake and the food is less than 15
        food.refresh() # Move the food to a new random location
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(snake.segments[-1].position()) # Position the new segment at the position of the last segment
        snake.segments.append(new_segment)
        
        Scoreboard.increase_score() # Increase the score by 1
        
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over()
    
    #detect collision with tail
    for segment in snake.segments[1:]: # Loop through all the segments except the head
        if snake.head.distance(segment) < 10: # If the distance between the head and any segment is less than 10
            game_is_on = False
            Scoreboard.game_over()

    snake.move() # Move the snake forward




screen.exitonclick()    