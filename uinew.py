THEME_COLOR = "#375362"

from tkinter import  *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.configure(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.score_label = Label(self.window, text="Score : 0", background=THEME_COLOR , fg="white")
        self.score_label.grid(row=0, column=1)
        

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_txt = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some text", 
            fill=THEME_COLOR, 
            font=("Ariel", 20))
        self.canvas.grid(row=1, column=0, columnspan=2 , pady=30)

        check_img = PhotoImage(file="images/true.png")
        self.check = Button(image=check_img)
        self.check.grid(row=2, column=0)

        times_img = PhotoImage(file="images/false.png")
        self.times = Button(image=times_img)
        self.times.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


