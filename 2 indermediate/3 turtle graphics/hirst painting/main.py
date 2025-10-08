import colorgram #package: pip install colorgram.py
import turtle as t
import random

#extract colours from the image
rgb_colors = []
colors = colorgram.extract('Damien_Hirst.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)    
    
    
# rgb_colors = [
#     (26, 188, 156),   # Turquoise
#     (46, 204, 113),   # Emerald
#     (52, 152, 219),   # Bright Blue
#     (155, 89, 182),   # Amethyst
#     (241, 196, 15),   # Sunflower
#     (230, 126, 34),   # Carrot
#     (231, 76, 60),    # Alizarin Red
#     (149, 165, 166),  # Grayish Blue
#     (243, 156, 18),   # Orange Peel
#     (52, 73, 94),     # Dark Slate
#     (255, 99, 71),    # Tomato
#     (135, 206, 250),  # Light Sky Blue
#     (255, 140, 0),    # Dark Orange
#     (144, 238, 144),  # Light Green
#     (218, 112, 214),  # Orchid
#     (123, 104, 238),  # Medium Slate Blue
#     (220, 20, 60),    # Crimson
#     (0, 206, 209),    # Dark Turquoise
#     (255, 215, 0),    # Gold
#     (72, 61, 139),    # Dark Slate Blue
#     (60, 179, 113),   # Medium Sea Green
#     (199, 21, 133),   # Medium Violet Red
#     (100, 149, 237),  # Cornflower Blue
#     (176, 224, 230),  # Powder Blue
#     (210, 105, 30),   # Chocolate
#     (240, 230, 140),  # Khaki
#     (255, 20, 147),   # Deep Pink
#     (0, 191, 255),    # Deep Sky Blue
#     (186, 85, 211),   # Medium Orchid
#     (205, 133, 63),   # Peru
#     (139, 69, 19),    # Saddle Brown
#     (255, 160, 122),  # Light Salmon
#     (127, 255, 0),    # Chartreuse
#     (34, 139, 34),    # Forest Green
#     (70, 130, 180),   # Steel Blue
#     (255, 228, 181),  # Moccasin
#     (152, 251, 152),  # Pale Green
#     (255, 105, 180),  # Hot Pink
#     (176, 48, 96),    # Maroon
#     (189, 183, 107),  # Dark Khaki
# ]


tim = t.Turtle()
t.colormode(255)    
tim.speed("fastest")
tim.penup()
tim.hideturtle()

#set the starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

#draw the lines of dots
for _ in range(10):
    for _ in range(10):
        #pick a colour and size for the dot
        tim.dot(20, random.choice(rgb_colors))
        #draw the dots in a line
        tim.forward(50)

    #move the turtle to starting point of the next line
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    

screen = t.Screen()
screen.exitonclick()