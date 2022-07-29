from turtle import Turtle
import random

from scoreb import TEXT_DATA, FONT_DATA

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5 , 0.5)
        self.color("blue")
        self.speed("fastest")
        #self.hideturtle()
        self.refresh()
    def refresh(self):
        self.clear()
        self.goto(random.randint(-320,320) , random.randint(-320,320))
        self.write("h", align= TEXT_DATA, font = FONT_DATA)
    
class Mera:
    def __init__(self , arr):
        self.bank = ["m","e","r","a"]
        self.box = []
        self.main_data = list(arr)
        self.data = [*self.main_data ,*self.bank]
        self.make()

    def make(self):
        for item in self.data:
            one = Turtle()
            one.penup()
            one.shapesize(0.8 , 0.8)
            one.color("blue")
            one.letter = item
            one.speed("fastest")
            one.goto(random.randint(-300,300) , random.randint(-300,300))
            one.write(f"{item}", align= TEXT_DATA, font = FONT_DATA)
            #one.hideturtle()          
            self.box.append(one)
            
    def refresh(self):
        for item in self.box:
            item.goto(random.randint(-320,320) , random.randint(-320,320))
            item.write(f"{item}", align= TEXT_DATA, font = FONT_DATA)
        
            
            
            
