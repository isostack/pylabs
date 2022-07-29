#import statements
from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Score

#screen object
wn = Screen() 
wn.setup(width = 600, height = 600)
wn.title("Snake Game")
wn.tracer(0)
wn.bgcolor("black")
wn.listen()

#object instances
snake = Snake()
food = Food()
scores = Score()
state = True

#screen listening
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")

#mail loop
while state:
    wn.update()
    time.sleep(0.2) 
    snake.move()

    # Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        scores.counter()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scores.reset()
        snake.reset()
       
    # Detect collision with snake
    for item in snake.box:
        if item == snake.head:
            pass
        elif snake.head.distance(item) < 10:
            scores.reset()
            snake.reset()
           

wn.exitonclick()







