from tkinter import Tk, Button, Label, Checkbutton, IntVar, ttk, Entry ,StringVar
import pandas as pd

root = Tk()

operation = StringVar()
liste = []

df = pd.DataFrame({
    'close' : [1, 2, 3, 4, 5],
    'open' : [5, 4, 3, 2, 1]
})

def validate():
    global operation
    liste.append(operation.get())
    operation.set('')

def fin():
    global liste, df
    close = df.close
    open = df.open
    for calcul in liste:
        print(eval(calcul))

def reinitialiser():
    global liste
    liste = []

Entry(root, textvariable=operation).grid(row=0, column=0, columnspan=2 ,ipadx=5, ipady=5)
Button(root, command=validate).grid(row=0 ,column=2 ,ipadx=5, ipady=5)
Button(root, text='fin', command=fin).grid(row=1, column=1)
Button(root, text='reinitialiser', command=reinitialiser).grid(row=2, column=1)

root.mainloop()