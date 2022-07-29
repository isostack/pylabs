from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.goto(0,0)
        self.speed("fastest")
        self.dx = 10
        self.dy = 10 
    
    def  move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
    
    def reset(self):
        self.goto(0,0)
        self.dx *= -1