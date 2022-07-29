FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        
    def update(self):
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font= FONT)
    
    def counter(self):
        self.score += 1
        self.update()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)