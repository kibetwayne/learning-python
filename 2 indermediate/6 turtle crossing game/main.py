import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creating instances
tim = Player()
level = Scoreboard()
cars = CarManager()

#move turtle on key press
screen.onkey(tim.move_up, 'Up')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    cars.create_car()
    cars.move_cars()
    
    # Detect collision with cars
    for car in cars.all_cars:
        if tim.distance(car) < 20:
            game_is_on = False
            level.game_over()
            
    # Detect successful crossing
    if tim.is_at_finish_line():
        tim.go_to_start()
        cars.level_up()
        level.increase_level()
    
    
screen.exitonclick()