import tkinter as Tk

root = Tk.Tk()

root.title("ZooAdmin")
root.state('zoomed')
root.configure(background='grey')

#CONNECTING DATABASE
connect = Tk.Label(root, text='Connect Your SQL Database')
connect.place(x=80, y=110)
connect.configure(fg='black')
connect.configure(font=("Helvetica", 18))
connect.configure(background='grey')
connectinput = Tk.Entry(root, width=55)
connectinput.insert(0, "name of database")
connectinput.place(x=80, y=140)
connectbt = Tk.Button(root, text="Connect")
connectbt.place(x=185,y = 175)

#GENERATING REPORT
report = Tk.Label(root, text='Generate the Report')
report.place(x=100, y=210)
report.configure(fg='black')
report.configure(font=("Helvetica", 18))
report.configure(background='grey')
menu= Tk.StringVar()
menu.set("Select Any Table")
reportselect= Tk.OptionMenu(root, menu, "Workers", "Animals", "Vehicles")
reportselect.place(x=145, y=265)
reportbt = Tk.Button(root, text="Generate")
reportbt.place(x=180, y=300)

#REGISTER NEW OPTION
reg = Tk.Label
reg = Tk.Label(root, text='Register New Item')
reg.place(x=100, y=300)
reg.configure(fg='black')
reg.configure(font=("Helvetica", 18))
reg.configure(background='grey')

menu= Tk.StringVar()
menu.set("Select Any Option")
regselect1= Tk.OptionMenu(root, menu, "Workers", "Animals", "Vehicles")
regselect1.place(x=145, y=345)


regselect = Tk.Label
regselect = Tk.Label(root, text='Enter Information')
regselect.place(x=100, y=385)
regselect.configure(fg='black')
regselect.configure(font=("Helvetica", 18))
regselect.configure(background='grey')
regenter = Tk.Entry(root, width=45)
regenter.place(x=80, y=425)

















root.mainloop()