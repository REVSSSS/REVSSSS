from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Your account was hacked").grid(column=0, row=0)

ttk.Button(frm, text="Continue", command=root.destroy).grid(column=2, row=0)

root.mainloop()
