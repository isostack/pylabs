from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    import random
    # Generate a random password
    pass_inpt.delete(0,END)
    password = ''.join([chr(random.randint(48,126)) for _ in range(0,8)])
    pass_inpt.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    # Get data
    item_name = wnt_inpt.get()
    item_mail = mail_inpt.get()
    item_pass = pass_inpt.get()
    json_data = {
        item_name :{
          "email": item_mail,
          "password":item_pass
        }
    }
    try:
        # Check for empty entry
        if len(item_pass) == 0 or len(item_name) == 0 or len(item_mail) == 0:
            raise ValueError('Empty entry')
    except ValueError:
        # Display error message
        messagebox.showinfo('Error','You have unfilled fields in the form!')
    else:
        with open('password.json', 'w') as json_file:
            json.dump(json_data , json_file , indent=4)
        # Clear the password
            pyperclip.copy(item_pass)
            pass_inpt.delete(0,END)
            wnt_inpt.delete(0,END)

    
    # item_name = wnt_inpt.get()
    # item_mail = mail_inpt.get()
    # item_pass = pass_inpt.get()
    # # Check if the password is empty
    # if len(item_pass) == 0 or len(item_name) == 0 or len(item_mail) == 0:
    #     messagebox.showinfo('Error','You have unfilled fields in the form!')
    # else:    
    #     state = messagebox.askokcancel(title = item_name , message=f"Website: {item_name}'s \nPassword: {item_pass} \nEmail: {item_mail} \n\nIs this correct?")
    #     # Save the password
        
    #     if state:
    #         with open('passwords.txt', 'a') as file:
    #             item = item_name + ' | ' + item_mail + ' | ' + item_pass + '\n'
    #             file.write(item)
    #     # Clear the password
    #         pyperclip.copy(item_pass)
    #         pass_inpt.delete(0,END)
    #         wnt_inpt.delete(0,END)
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