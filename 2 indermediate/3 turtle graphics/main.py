from turtle import Turtle, Screen, colormode
import random
#using an alias incase of modules with large names
#import turtle as t

tim = Turtle()
colormode(255)
tim.shape("turtle")
tim.color("coral")
tim.speed("fastest")
colours = ['red', 'blue', 'green', 'yellow', 'black', 'orange', 'purple', 'gold']

#random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

#!=====================================================
#draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#!=====================================================

# #draw a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()    

#!=====================================================

# #drawing shapes of different colours

# for number_of_sides in range(3, 11):
#     angle = 360/number_of_sides
#     tim.color(random.sample(colours, k=1))
#     for i in range(number_of_sides):
#         tim.forward(50)
#         tim.right(angle)
        

#!=====================================================
#random direction movement
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# screen = Screen()
# screen.exitonclick()

#!=====================================================
#drawing a spirograph
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)            # radius of circle
        tim.setheading(tim.heading() + gap_size)  # turn by gap size


draw_spirograph(5)  # try smaller gap for denser design
