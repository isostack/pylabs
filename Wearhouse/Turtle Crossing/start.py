#module imports
from turtle import Turtle , Screen
from player import Player
from object_manager import CarMng
from scoreboard import Scoreboard
import time
import random

#screen setup
wn = Screen()
wn.setup(width=800 , height=600)
wn.title("Turtle Crossing")
wn.bgcolor("black")
wn.tracer(0)
wn.listen()

#variable calls
g_state = True
g_player = Player()
car_mng = CarMng()
scores = Scoreboard()

wn.onkey(g_player.move, "Up")

#while loops
while g_state:
    wn.update()
    time.sleep(0.1)

    car_mng.create_cars()
    car_mng.move()

    for car in car_mng.all_cars:
        if car.distance(g_player) < 20:
            scores.game_over()
            g_state = False

    if g_player.finished():
        scores.counter()
        g_player.goto_start()
        

wn.exitonclick()













