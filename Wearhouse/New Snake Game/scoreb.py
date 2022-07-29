from turtle import Turtle

TEXT_DATA = "center"
FONT_DATA = ("Courier" , 20, "normal")

class Score(Turtle):
    def __init__(self , name):
        super().__init__()
        self.username = name
        self.scored = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.inject()

    def inject(self):
        self.write(f"Name:{self.username} Found: {self.scored}", align= TEXT_DATA, font = FONT_DATA)

    def game_lost(self):
        self.goto(0,0)
        self.write(f"GAME OVER You lost!", align= TEXT_DATA, font = FONT_DATA)
    def game_win(self):
        self.goto(0,0)
        self.write(f"Congratulations!", align= TEXT_DATA, font = FONT_DATA)

    def update(self):
        self.scored += 1
        self.clear()
        self.inject()
    
        
