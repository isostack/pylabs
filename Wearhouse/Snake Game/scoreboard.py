from  turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        with open("../../Desktop/data.txt") as data:
            self.high_score = int(data.read())
        
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=("Courier", 24, "normal"))
    
    def counter(self):
        self.score += 1
        self.update()
 
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt" , mode="w") as old_data:
                old_data.write(str(self.score))
        self.score = 0
        self.update()

    
            
    