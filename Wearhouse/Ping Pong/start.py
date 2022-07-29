from turtle import Turtle, Screen
from pads import Pad
from ball import Ball
from scoreboard import ScoreBoard
import time

#screen setup
wn = Screen()
wn.setup(width = 800, height = 600)
wn.title("Ping Pong")
wn.listen() 
wn.bgcolor("black")
wn.tracer(0)

#variables
r_pad = Pad(380)
l_pad = Pad(-380)
ball = Ball()
scores = ScoreBoard()

#screen listening
wn.onkey(r_pad.pad_up, "Up")
wn.onkey(r_pad.pad_down, "Down")
wn.onkey(l_pad.pad_up, "Left")
wn.onkey(l_pad.pad_down, "Right")

g_state = True 

while g_state: 
    time.sleep(0.1)
    wn.update()
    ball.move()
    # Detect collision with the wall and pad
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.dy *= -1
    elif ball.distance(r_pad) < 50 and ball.xcor() > 350:
        ball.dx *= -1 
    elif ball.distance(l_pad) < 50 and ball.xcor() < -350:
        ball.dx *= -1 
    # Detect if ball misses
    elif ball.xcor() > 390:
        print("Left player wins!")
        ball.reset()
        scores.l_point()
        
    elif ball.xcor() < -390:
        print("Right player wins!")
        ball.reset()
        scores.r_point()

wn.exitonclick()