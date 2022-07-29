#project imports
from turtle import Turtle , Screen
from snk import Snake
from metadata import Food , Mera
from scoreb import Score
import time

#window setup
wn = Screen()
wn.setup(650 , 650)
wn.title("Snake Game")
wn.bgcolor("black")
wn.tracer(0)

p_n = wn.textinput(title = "Player Name" , prompt="Type in your name")

wn.listen()

#class instances
snake = Snake()
food = Mera(p_n)
scores = Score(p_n)
g_state = True

#key listening
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")

#main loop
while g_state:
    wn.update()
    time.sleep(0.2) 
    snake.move()
    
    #detect collision
            
    for item in food.box:  
        if snake.head.distance(item) < 15 and snake.head.xcor() <= item.xcor() + 15 and snake.head.ycor() <= item.ycor() + 15:
            print(snake.head.xcor())
            print(item.xcor())
            snake.head.fd(20)
            if item.letter in food.main_data:
                pink = food.box[food.box.index(item)]
                pink.clear()
                food.main_data.remove(pink.letter)
                print(food.main_data)
                scores.update()
                snake.extend()
            else:
                g_state = False
                scores.game_lost()
                
        elif len(food.main_data) == 0:
                g_state = False
                scores.game_win()
                
    #detect collision with wall
    if snake.head.xcor() < -330 or snake.head.xcor() > 330 or snake.head.ycor() < -330 or snake.head.ycor() > 330:
        g_state = False
        scores.game_over()
    for item in snake.box[1:]:
        if snake.head.distance(item) < 1:
            g_state = False
            scores.game_over()
    
wn.exitonclick()





























