import turtle

screen = turtle.Screen()
screen.title("county guessing game")
screen.setup(width=1000, height=1000)
image = "counties.gif"
screen.addshape(image)
turtle.shape(image)



screen.exitonclick()
#answer = screen.textinput(title="guess the county", prompt="what county am I in?")