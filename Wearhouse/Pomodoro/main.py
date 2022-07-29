from pathlib import WindowsPath
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
protocol = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(protocol)
    title.config(text="Pomodoro App" , fg = "Green")
    canvas.itemconfig(timer_text, text = "00:00")
    end_elem.config(text = "Click to start a session")
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mechanism():
    global reps
    reps += 1

    if reps % 8 == 0:
        title.config(text ="Long Break", fg = RED)
        countdown_mechanism(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title.config(text ="Short Break"  , fg = PINK)
        countdown_mechanism(SHORT_BREAK_MIN * 60)
    else:
        title.config(text ="Work Time", fg = GREEN)
        countdown_mechanism(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def countdown_mechanism(count):
    global protocol
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 9:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text , text = f"{min}:{sec}")

    if count > 0:  
        protocol = window.after(1000, countdown_mechanism, count - 1)
    else:
        timer_mechanism()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        end_elem.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- # 
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100 , bg=YELLOW)
#Title
title = Label(window, text="Pomodoro App", font=("Courier", 40), fg="green", bg=YELLOW)
title.grid(row=0, column=1)
#Canvas
canvas = Canvas(window, width=200, height=224, highlightthickness=0 , bg=YELLOW)
appimg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=appimg)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35 , "bold"), fill="white")
canvas.grid(row=1, column=1)
#Other Elements
btn_one = Button(window, text="Start", font=(FONT_NAME), fg="green", bg=YELLOW , highlightthickness=0, command=timer_mechanism)
btn_one.grid(row=2, column=0)
btn_two = Button(window, text="Reset", font=(FONT_NAME), fg="green", bg=YELLOW, highlightthickness=0, command = reset_timer)
btn_two.grid(row=2, column=2)
end_elem = Label(window, font=(FONT_NAME, 20), fg="Green", bg=YELLOW)
end_elem.grid(row=3, column=1)

window.mainloop()