import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

#instances
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
game_is_on = True

while game_is_on:
    screen.update() #only show screen after the 2 paddles have been made and moved to the edge
    time.sleep(ball.move_speed)# control the speed of the game to show ball movement
    ball.move()
    
    #detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    #detect if ball missed r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #detect if ball missed l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()