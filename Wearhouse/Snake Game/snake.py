from turtle import Turtle 

class Snake:
    def __init__(self):
        self.box = []
        self.x_position = [(0,0), (-20,0), (-40,0)]
        self.make()
        self.head = self.box[0]   

    def make(self):
        for item in self.x_position:
            one = Turtle(shape="square")
            one.color("green")
            one.penup()
            one.goto(item)
            self.box.append(one)
    def move(self):
        for target in range(len(self.box) - 1, 0, -1):
            x_pos = self.box[target - 1].xcor()
            y_pos = self.box[target - 1].ycor()
            self.box[target].goto(x_pos, y_pos)
        self.head.fd(20)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for item in self.box:
            item.goto(1000,1000)
        #self.head.goto(0,0)
        self.box = []
        self.make()
        self.head = self.box[0]
        