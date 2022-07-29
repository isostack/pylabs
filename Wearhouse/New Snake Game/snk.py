from turtle import Turtle
class Snake(Turtle):
    def __init__(self):
        self.box = []
        self.x_pos = [(0,0),(-20,0),(-40,0)]
        self.make()
        self.head = self.box[0]
    def make(self):
        for item in self.x_pos:
            self.add_item(item)
            
    def add_item(self , position):
        one = Turtle(shape = "square")
        one.shapesize(0.7 , 0.7)
        one.color("blue")
        one.penup()
        one.goto(position)
        self.box.append(one)

    def extend(self):
        self.add_item(self.box[-1].position())
        
    
    def move(self):
        for target in range(len(self.box) - 1, 0, -1):
            x_pos = self.box[target - 1].xcor()
            y_pos = self.box[target - 1].ycor()
            self.box[target].goto(x_pos, y_pos)
        self.head.fd(10)

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
            
            
        
        
    
