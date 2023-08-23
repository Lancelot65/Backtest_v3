from tkinter import Tk, Label, Listbox#, Button

color = 'lavender'

fenetre = Tk()
fenetre.configure(bg=color)
fenetre.title('backtest')

Label(fenetre, text='paramètre graphique', bg=color).grid(row=0, column=1, columnspan=2)

Label(fenetre, text='echelle', bg=color).grid(row=1, column=0)
timelist = Listbox(fenetre, width=10, height=5, selectbackground='grey', bg=color)
timelist.insert(1, "1min")
timelist.insert(2, "5min")
timelist.insert(3, "30min")
timelist.insert(4, "1d")
timelist.insert(5, "1w")
timelist.select_set(0)
timelist.grid(row=2, column=0)

Label(fenetre, text='exchange', bg=color).grid(row=1, column=1)
exchangelist = Listbox(fenetre, width=10, height=5, selectbackground='grey', bg=color, relief='solid')
exchangelist.insert(1, 'BTC/USDT')
exchangelist.insert(2, "EUR/USDT")
exchangelist.insert(3, "...")
exchangelist.insert(4, "...")
exchangelist.insert(5, "...")
exchangelist.select_set(0)
exchangelist.grid(row=2, column=3)

Label(fenetre, text='type shema', bg=color).grid(row=1, column=3)
exchangelist = Listbox(fenetre, width=10, height=5, selectbackground='grey', bg=color, relief='solid')
exchangelist.insert(1, 'ligne')
exchangelist.insert(2, "bougie")
exchangelist.select_set(0)
exchangelist.grid(row=2, column=1)

#Button(fenetre, text='valider la selection')
fenetre.mainloop()