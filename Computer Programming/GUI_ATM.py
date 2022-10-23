from tkinter import *
from turtle import width

from click import command

root = Tk()
root.title ("Dan Joshua M. Tagaan - BSIT-1R12")
root.geometry('500x400')

var = StringVar()

dta1 = Entry(root, textvariable= var)
dta1.grid(row=0, column=0)

lbl  = Label(root)



def init_balance():
    global Balance
    Balance = 0
    set_int = int(dta1.get())
    lbl.config(text="" + str(set_int))
    lbl.grid(row=3, column=5)
    Balance = int(set_int) + int(Balance)
    btn_init.config(state=DISABLED)
    dta1.delete(0, END)
    
def rem_bal():
    lbl.config(text="" + str(Balance))
    lbl.grid(row=3, column=5)
    dta1.delete(0, END)

def depo():
    global Balance
    Depos = int(dta1.get())
    Depos = Balance + Depos
    dta1.delete(0, END)
    lbl.config(text="" + str(Balance))
    lbl.grid(row=3, column=5)
    

def witdrw():
    witd = int(dta1.get())
    witd = Balance - witd
    dta1.delete(0, END)
    lbl.config(text="" + str(Balance))
    lbl.grid(row=3, column=5)

def ext():
    quit()

btn_init = Button(root, text="(1)Set initial balance", command=init_balance)
btn_rmbl = Button(root, text="(2)Remaining balance", command=rem_bal)
btn_dep = Button(root, text="(3)Deposit", command=depo)
btn_wthdr = Button(root, text="(4)Withdraw", command=witdrw)
btn_ext = Button(root, text="(5)Exit", command=ext)

btn_init.grid(row=1,column=0, sticky= "ew")
btn_rmbl.grid(row=2,column=0, sticky= "ew")
btn_dep.grid(row=3,column=0, sticky= "ew")
btn_wthdr.grid(row=4,column=0, sticky= "ew")
btn_ext.grid(row=5,column=0, sticky= "ew")



root.mainloop()