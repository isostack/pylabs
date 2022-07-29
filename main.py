from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    import random
    # Generate a random password
    pass_inpt.delete(0,END)
    password = ''
    for i in range(0,8):
        password += chr(random.randint(33,126))
    pass_inpt.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    # Get the password
    item_name = wnt_inpt.get()
    item_mail = mail_inpt.get()
    item_pass = pass_inpt.get()
    # Save the password
    with open('passwords.txt', 'a') as file:
        item = item_name + ' | ' + item_mail + ' | ' + item_pass + '\n'
        file.write(item)
    # Clear the password
    pass_inpt.delete(0,END)
    wnt_inpt.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
app_image = PhotoImage(file = 'logo.png')
app_canv = Canvas(width=200 , height=200)
app_canv.create_image(100,100 , image=app_image)
app_canv.grid(row=0,column=1)

webname_txt = Label(window,text="Website Name:")
webname_txt.grid(row=1,column=0)
mail_txt = Label(window,text="Email:")
mail_txt.grid(row=2,column=0)
pass_txt = Label(window,text="Password:")
pass_txt.grid(row=3,column=0)

wnt_inpt = Entry(window,width=55)
wnt_inpt.grid(row=1,column=1,columnspan=2)
wnt_inpt.focus()
mail_inpt = Entry(window,width=55)
mail_inpt.grid(row=2,column=1,columnspan=2)
mail_inpt.insert(END,"gamma@gmail.com")
pass_inpt = Entry(window,width=36)
pass_inpt.grid(row=3,column=1)

gen_btn = Button(window,text="Generate Password",command=gen_pass)
gen_btn.grid(row=3,column=2)

save_btn = Button(window,width=46, text="Add Item", command=add_data)
save_btn.grid(row=4,column=1 , columnspan=2)
window.mainloop()