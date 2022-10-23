from tkinter import *

root = Tk()
root.title ("Dan Joshua M. Tagaan - BSIT-1R12")
root.geometry('400x180')

insrt = Entry(root)
insrt.grid(row=0,column=0)

in_bal = Label(root)
dep_lbl = Label(root)
withd_lbl = Label(root)
rem_lbl = Label(root)

def init_balance():
    global Balance 
    Balance = 0
    Balance = int(insrt.get())
    in_bal.config(text="Balance: " + str(Balance))
    in_bal.grid(row=3, column=5)
    btn_init.config(state=DISABLED)
    insrt.delete(0, END)


def depo():
    global Balance
    Balance = Balance
    depos = 0
    depos = int(insrt.get())
    new = Balance + depos
    Balance = new
    dep_lbl.config(text="Deposited amount: " + str(depos))
    dep_lbl.grid(row=4, column=5)
    insrt.delete(0, END)


def witdrw():
    global Balance
    Balance = Balance
    withdraw = 0
    withdraw = int(insrt.get())
    new = Balance - withdraw
    Balance = new
    withd_lbl.config(text="Withdrawn amount: " + str(withdraw))
    withd_lbl.grid(row=4, column=5)
    insrt.delete(0, END)


def rem_bal():
    rem_lbl.config(text="Remaining balance: " + str(Balance))
    rem_lbl.grid(row=3,column=5)
    insrt.delete(0, END)


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