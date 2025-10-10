from turtle import Turtle, Screen
import random

screen = Screen()

#! Turtle racing game ======================= START ============================


#set screen dimensions
screen.setup(width=500, height=400)

is_race_on = False

#get input 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "yellow", "indigo", "green", "purple"]
y_positions = [120, 80, 40, 0, -40, -80, -120]

# Create a turtle to draw the finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(218, -150)  # position to start drawing (right side)
finish_line.pendown()
finish_line.pensize(3)
finish_line.color("black")

# Draw vertical finish line
finish_line.left(90)
finish_line.forward(300)

#creating and moving turtles to the starting line
all_turtles = []
for num in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[num])
    all_turtles.append(new_turtle)
    
#racing the turtles
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



