import tkinter as tk

fenetre = tk.Tk()
fenetre.iconphoto(True, tk.PhotoImage(file='logo.png'))
fenetre.title('Backtest')


# tk.Label(fenetre, text='Hello World !').pack()
# tk.Button(fenetre, text='Button').pack()
# tk.Entry(fenetre).pack()
# tk.Checkbutton(fenetre, text='ligne').pack()

# value = tk.StringVar() 
# bouton1 = tk.Radiobutton(fenetre, text="Oui", variable=value, value=1)
# bouton2 = tk.Radiobutton(fenetre, text="Non", variable=value, value=2)
# bouton3 = tk.Radiobutton(fenetre, text="Peu être", variable=value, value=3)
# bouton1.pack()
# bouton2.pack()
# bouton3.pack()

# def action_1():
#     print('click')

# liste = tk.Listbox(fenetre)
# liste.insert(1, "1min")
# liste.insert(2, "5min")
# liste.insert(3, "30min")
# liste.insert(4, "1d")
# liste.insert(5, "1w")
# liste.pack()

# tk.Label(fenetre, text='choise timeframe').pack()
# tk.Button(fenetre, text='click', command=action_1).pack()



# fenetre.update_idletasks()

# print(fenetre.geometry())

# a = tk.Toplevel(fenetre, bg='red')
# b = tk.Toplevel(fenetre, bg='blue')
# fenetre.withdraw()



# tk.Canvas(fenetre, width=300, height=300, background='red').grid(row=0, column=0, padx=10, pady=10)
# tk.Canvas(fenetre, width=300, height=300, background='blue').grid(row=0, column=1, padx=10, pady=10)

# tk.Label(fenetre, text='test').grid(row=1, column=0)
# tk.Label(fenetre, text='test2').grid(row=1, column=1)

test = tk.IntVar(value=10)

def up():
    test.set(test.get() + 1)

def down():
    test.set(test.get() - 1)

tk.Button(fenetre, text='up', background='green', command=up, width=10).grid(row=0, column=0)
tk.Button(fenetre, text='down', background='red', command=down, width=10).grid(row=0, column=2)

tk.Label(fenetre, textvariable=test).grid(row=1,  column=0)
jsp = tk.StringVar(value='ecrire')
tk.Entry(fenetre, textvariable=jsp).grid(row=1,  column=1)
tk.Label(fenetre, textvariable=jsp).grid(row=1,  column=2)

fenetre.mainloop()