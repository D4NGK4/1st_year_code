from tkinter import *

root = Tk()
root.geometry('800x800')

var1 = StringVar()
var2 = StringVar()

lbl = Label(root)

Label(root, text="Enter First Number").place(x=0, y=200)
dta1 = Entry(root, textvariable=var1).place(x=150, y=200)
Label(root, text="Enter Second Number").place(x=0, y=400)
dta2 = Entry(root, textvariable=var2).place(x=150, y=400)


def add():
    sum = int(var1.get()) + int(var2.get())
    lbl.config(text="Result: " + str(sum))
    lbl.place(x=400, y=300)


bttn = Button(root, text="Calculate Sum", command=add).place(x=195, y=300)
root.mainloop()