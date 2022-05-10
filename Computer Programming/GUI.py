from tkinter import *

root = Tk()
root.geometry('300x300')

var1 = StringVar()
var2 = StringVar()

lbl = Label(root)

Label(root, text="Enter First Number").pack()
dta1 = Entry(root, textvariable=var1).pack()
Label(root, text="Enter Second Number").pack()
dta2 = Entry(root, textvariable=var2).pack()


def add():
    sum = int(var1.get()) + int(var2.get())
    lbl.config(text="Result: " + str(sum))
    lbl.pack()


bttn = Button(root, text="Calculate Sum", command=add).pack()
root.mainloop()