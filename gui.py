import tkinter as Tk
import db_backend as db

def displayLoginWindow(conn):
    root = Tk.Tk()
    
    root.title("Login Form")
    root.geometry("650x345")
    root.configure(background='grey')
    
    welcome_text = Tk.Label(root, text="Welcome to ZooAdmin!")
    welcome_text.place(x=80, y=90)
    welcome_text.configure(fg='black')
    welcome_text.configure(font=("Courier", 32))
    welcome_text.configure(background='grey')
    
    user_name = Tk.Label(root, text="Username")
    user_name.place(x=190, y=165)
    user_name.configure(background='grey')
    user_name.configure(fg='black')
    user_name_var = Tk.StringVar(root, value='')
    user_name_input_area = Tk.Entry(root, width=30)
    user_name_input_area.place(x=250, y=165)
    
    user_password = Tk.Label(root, text="Password")
    user_password.place(x=190, y=185)
    user_password.configure(background='grey')
    user_password.configure(fg='black')
    user_password_var = Tk.StringVar(root, value='')
    user_password_input_area = Tk.Entry(root, show="*", textvariable=user_password_var, width=30)
    user_password_input_area.place(x=250, y=185)
    
    submit_button = Tk.Button(root,
                              text="Submit Information",
                              command=lambda:db.createLoginTest(conn,
                                                      user_name_input_area.get(),
                                                      user_password_input_area.get()))
    submit_button.place(x=250, y=245)
    
    
    
    root.mainloop()

