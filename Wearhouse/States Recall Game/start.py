import pandas
import turtle

wn = turtle.Screen()
wn.title("U.S States Game")
image = "blank_states_img.gif"
wn.addshape(image)
turtle.shape(image)
g_state = []

while len(g_state) < 50:
    data = pandas.read_csv("50_states.csv")
    answer_state = wn.textinput("Guess the state", "What is the capital of the state?").capitalize()
    if answer_state == "Exit":
        break
    elif data[data.state == answer_state].empty:
        pass 
    else :
        current_row = data[data.state == answer_state]
        g_state.append(answer_state)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(int(current_row.x) , int(current_row.y))
        tur.write(current_row.state.item())

def get_mouse_click(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click)
turtle.mainloop()