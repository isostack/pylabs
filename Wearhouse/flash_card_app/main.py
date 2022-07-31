BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_word = None

#***************************** GREEN CARDS     *******************************#
def flip_card():
    global current_word
    app_canv.itemconfig(bg_photo , image=card_back)
    current_word = random.choice(to_learn)
    app_canv.itemconfig(card_title , text = "English")
    app_canv.itemconfig(card_word , text = current_word["English"])


#***************************** WHITE CARDS     *******************************#
def next_card():
    global current_word , func_timer
    window.after_cancel(func_timer)
    app_canv.itemconfig(bg_photo , image=card_front)
    current_word = random.choice(to_learn)
    app_canv.itemconfig(card_title , text = "French")
    app_canv.itemconfig(card_word , text = current_word["French"])
    func_timer = window.after(3000 , flip_card)
#***************************** SAVE CARDS     *******************************#
def is_known():
    to_learn.remove(current_word)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv' , index=False)
    next_card()

window = Tk()
window.title("Flash App")
window.config(padx=50,pady=20 ,bg=BACKGROUND_COLOR)

func_timer = window.after(3000 , flip_card)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
green_btn = PhotoImage(file='images/right.png')
red_btn = PhotoImage(file='images/wrong.png')

app_canv = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
bg_photo = app_canv.create_image(400,263 , image = card_front)
app_canv.grid(row=0,column=0 , columnspan=2)
card_title = app_canv.create_text(400,150 , font=("Ariel" , 30,"italic"))
card_word = app_canv.create_text(400,263 , font=("Ariel" , 60,"italic"))
known_btn = Button(image = green_btn,highlightthickness=0 , command = is_known)
unknown_btn = Button(image=red_btn,highlightthickness=0 , command= next_card)
known_btn.grid(row=1,column =0)
unknown_btn.grid(row=1,column =1)

next_card()


window.mainloop()