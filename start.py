from tkinter import *
#**************************** UI ***********************************#

#**************************** File Caller ***********************************#

   

#**************************** UI ***********************************#
def call_img():
    main_win = Tk()
    main_win.config(padx=20 , pady=20)
    main_win.title("Quote Program")
    # text = Label(main_win , text = "This is a private program")
    # text.pack()

    # end_btn = Button(main_win , text="End")
    # end_btn.pack()
    win_canv = Canvas(width=720 , height=1440,highlightthickness=0)
    
    main_win.mainloop()

call_img()