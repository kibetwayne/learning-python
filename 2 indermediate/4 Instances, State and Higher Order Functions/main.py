from turtle import Turtle, Screen
import random

screen = Screen()

#!functions to move the turtle================= START ============================
#?tim is an instance of the Turtle class
tim = Turtle(shape="turtle")
#?color is a state/attribute of the Turtle class
tim.color("red")

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#event listener
screen.listen()

#?screen.onkey is a higher order function because it takes in another function as an input
screen.onkey(move_forwards, "w") #screen.onkey(function, key)
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
