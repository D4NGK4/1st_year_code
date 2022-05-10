from tkinter import *

root = Tk()
root.geometry('300x300')

var1 = StringVar()
var2 = StringVar()

lbl = Label(root)

Label(root, text="Enter First Number").grid(row=0, column=0)
dta1 = Entry(root, textvariable=var1).grid(row=0, column=1)
Label(root, text="Enter Second Number").grid(row=1, column=0)
dta2 = Entry(root, textvariable=var2).grid(row=1, column=1)


def add():
    sum = int(var1.get()) + int(var2.get())
    lbl.config(text="Result: " + str(sum))
    lbl.grid(row=3, column=1)


bttn = Button(root, text="Compute Sum", command=add).grid(row=2, column=1)
root.mainloop()