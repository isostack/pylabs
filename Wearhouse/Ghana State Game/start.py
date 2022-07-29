import turtle
import pandas

wn = turtle.Screen()
wn.title("Ghana States Game")
image = "ghana.gif"
wn.addshape(image)
wn.setup(width=800, height=600)
turtle.shape(image)
green = pandas.read_csv("data.csv")
brown = green.state.to_list()
score = 0
guessed_states = []
while score < 16:
    answer = wn.textinput(title = f"{score} regions correct", prompt="Type in a region").title()

    if answer == "End":
        missing_states = [state for state in brown if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    elif answer in brown:
        score += 1
        guessed_states.append(answer)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(int(green[green.state == answer].x) , int(green[green.state == answer].y))
        tur.write(green[green.state == answer].state.item())

end_tur = turtle.Turtle()
end_tur.shape("arrow")
end_tur.penup()
end_tur.shapesize(0.5,0.5)
end_tur.speed("slow")
x = -380 
y =  250
for item in brown:
    end_tur.goto(x , y)
    end_tur.write(item , font=("Arial", 10, "normal"))
    y -= 20
    
end_tur.goto(x , y - 20)
    
end_tur.write("THESE REGIONS OF GHANA." , font=("Arial", 15, "normal"))

wn.mainloop()
