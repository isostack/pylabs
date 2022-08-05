THEME_COLOR = "#375362"

from tkinter import  *
from quiz_brain import QuizBrain
import time 

class QuizInterface:
    def __init__(self , quiz : QuizBrain):
        self.quiz = quiz
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
            text=self.quiz.score, 
            fill=THEME_COLOR, 
            font=("Ariel", 20))
        self.canvas.grid(row=1, column=0, columnspan=2 , pady=30)

        check_img = PhotoImage(file="images/true.png")
        self.check = Button(image=check_img , command=self.true_func)
        self.check.grid(row=2, column=0)

        times_img = PhotoImage(file="images/false.png")
        self.times = Button(image=times_img , command =self.false_func)
        self.times.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_txt, text=self.quiz.next_question())
        else:
            end = f"You've completed the quiz , Your final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_txt, text=end)

    
    def true_func(self):
        if 'True' == self.quiz.bring_answer():
            self.quiz.score += 1
            self.score_label.config(text=f"Score :: {self.quiz.score}")
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(400 , self.get_next_question)   
        
    def false_func(self):
        if 'False' == self.quiz.bring_answer():
            self.quiz.score += 1
            self.score_label.config(text=f"Score :: {self.quiz.score}")
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(400 , self.get_next_question)
    

