from turtle import Turtle, Screen
import random

screen = Screen()

# #!functions to move the turtle================= START ============================
# #?tim is an instance of the Turtle class
# tim = Turtle(shape="turtle")
# #?color is a state/attribute of the Turtle class
# tim.color("red")

# def move_forwards():
#     tim.forward(10)
    
# def move_backwards():
#     tim.backward(10)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# #event listener
# screen.listen()

# #?screen.onkey is a higher order function because it takes in another function as an input
# screen.onkey(move_forwards, "w") #screen.onkey(function, key)
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# #!functions to move the turtle============= END ================================

#! Turtle racing game ======================= START ============================
#set screen dimensions
screen.setup(width=500, height=400)

is_race_on = False

#get input 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "yellow", "indigo", "green", "purple"]
y_positions = [120, 80, 40, 0, -40, -80, -120]

#creating and moving turtles to the starting line
all_turtles = []
for num in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[num])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10) #random distance to move forward
        turtle.forward(rand_distance)
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor() #get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            
#! Turtle racing game ======================= END ============================

screen.exitonclick()
