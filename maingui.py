import tkinter as Tk

root = Tk.Tk()

root.title("ZooAdmin")
root.state('zoomed')
root.configure(background='grey')

#CONNECTING DATABASE
connect = Tk.Label(root, text='Connect Your SQL Database')
connect.place(relx=0.4, rely=0.1, relwidth=0.2)
connect.configure(fg='black')
connect.configure(font=("Helvetica", 18))
connect.configure(background='grey')
connectinput = Tk.Entry(root, width=55)
connectinput.insert(0, "name of database")
connectinput.place(relx=0.4, rely=0.15, relwidth=0.2)
connectbt = Tk.Button(root, text="Connect")
connectbt.place(relx=0.4, rely=0.2, relwidth=0.2)

#GENERATING REPORT
report = Tk.Label(root, text='Generate the Report')
report.place(relx=0.4, rely=0.25, relwidth=0.2)
report.configure(fg='black')
report.configure(font=("Helvetica", 18))
report.configure(background='grey')
menu= Tk.StringVar()
menu.set("Select Any Table")
reportselect= Tk.OptionMenu(root, menu, "Workers", "Animals", "Vehicles")
reportselect.place(relx=0.4, rely=0.3, relwidth=0.2)
reportbt = Tk.Button(root, text="Generate")
reportbt.place(relx=0.4, rely=0.35, relwidth=0.2)

#REGISTER NEW OPTION
reg = Tk.Label
reg = Tk.Label(root, text='Register New Item')
reg.place(relx=0.4, rely=0.4, relwidth=0.2)
reg.configure(fg='black')
reg.configure(font=("Helvetica", 18))
reg.configure(background='grey')

menu= Tk.StringVar()
menu.set("Select Any Option")
regselect1= Tk.OptionMenu(root, menu, "Workers", "Animals", "Vehicles")
regselect1.place(relx=0.4, rely=0.45, relwidth=0.2)


regselect = Tk.Label
regselect = Tk.Label(root, text='Enter Information')
regselect.place(relx=0.4, rely=0.5, relwidth=0.2)
regselect.configure(fg='black')
regselect.configure(font=("Helvetica", 18))
regselect.configure(background='grey')
regenter = Tk.Entry(root, width=45)
regenter.place(relx=0.4, rely=0.55, relwidth=0.2)
regenterbt = Tk.Button(root, width = 45, text = "Submit Info")

regenterbt.place(relx=0.4, rely=0.6, relwidth =0.2)

















root.mainloop()