import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CREATION_CHANCE = 6 # New car created every 6th time the main loop runs

class CarManager:
    """Manages the creation, movement, and speed of all cars."""
    def __init__(self):
        # CarManager is NOT a Turtle, it MANAGES a list of Turtle objects (cars)
        self.all_cars = [] 
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        """Randomly creates a new car at the right edge of the screen."""
        random_chance = random.randint(1, CAR_CREATION_CHANCE)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            # Position the car randomly on the Y-axis
            new_car.goto(300, random.randint(-250, 250))
            
            self.all_cars.append(new_car)
            
    def move_cars(self):
        """Moves every car in the list to the left."""
        for car in self.all_cars:
            car.backward(self.car_speed)
        
        # Remove cars that have moved off the screen
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]


    def level_up(self):
        """Increases the speed of all cars for the next level."""
        self.car_speed += MOVE_INCREMENT