from tkinter import Tk, ttk, Label, Button, PhotoImage, Entry, StringVar, Frame, Toplevel
import sys
from ccxt import binance
sys.path.append('../trad/Ohlcvplus')
from ohlcv import OhlcvPlus
from mplfinance.original_flavor import candlestick_ohlcgit
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_tableau():
    date_debut = annee.get() + '-' + mois.get() + '-' + jour.get() + ' 00:00:00'
    date_fin = annee_f.get() + '-' + mois_f.get() + '-' + jour_f.get() + ' 00:00:00'

 
    ohlcvp = OhlcvPlus(binance())
    data = ohlcvp.load(market=exchange.get(), timeframe=timelist.get(), since=date_debut, limit=date_fin, update=True, verbose=True, workers=100)
    df = data[['timestamp', 'open', 'high', 'low', 'close']]

    graphique = Toplevel(fenetre)

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    candlestick_ohlc(ax, df.values, colorup='g', colordown='r', width=0.0000002, alpha=0.9)

    # Intégrer le graphique Matplotlib dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=graphique)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    

color = 'lavender'

fenetre = Tk()
fenetre.option_add("*Font", "Times 10")

fenetre.resizable(False, False)

fenetre.configure(bg=color)
fenetre.title('backtest')
fenetre.iconphoto(True, PhotoImage(file='logo.png'))

Label(fenetre, text='Paramètre graphique', bg=color, font=("Times 15")).grid(row=0, column=1)

style = ttk.Combobox(fenetre, values=["ligne", "bougie"], state="readonly")
style.current(0)
Label(fenetre, text='type shema', bg=color).grid(row=1, column=3)
style.grid(row=2, column=1)


exchange = ttk.Combobox(fenetre, values=["BTC/USDT", "EUR/USDT"], state="readonly")
exchange.current(0)
exchange.grid(row=2, column=3)
Label(fenetre, text='exchange', bg=color).grid(row=1, column=1)

timelist = ttk.Combobox(fenetre, values=["1m", "5m","30m","1h", "1w"], state="readonly")
timelist.current(0)
Label(fenetre, text='timeframe', bg=color).grid(row=1, column=0)
timelist.grid(row=2, column=0)

Label(fenetre, text='debut', bg=color).grid(row=3, column=0)
Label(fenetre, text='Fin', bg=color).grid(row=3, column=3)
Button(fenetre, text='afficher', command=plot_tableau).grid(row=3, column=1, rowspan=2)

frame1 = Frame()
frame1.grid(row=4, column=0)

annee = StringVar(value='2023')
Entry(frame1, textvariable=annee, width=4).grid(row=0, column=0)
Label(frame1, text='/', bg=color, width=1).grid(row=0, column=2)

mois = StringVar(value='01')
Entry(frame1, textvariable=mois, width=2).grid(row=0, column=3)
Label(frame1, text='/', bg=color, width=1).grid(row=0, column=4)

jour = StringVar(value='01')
Entry(frame1, textvariable=jour, width=2).grid(row=0, column=5)
Label(frame1, text=' ', bg=color, width=1).grid(row=0, column=6)




frame2 = Frame()
frame2.grid(row=4, column=3)

annee_f = StringVar(value='2023')
Entry(frame2, textvariable=annee_f, width=4).grid(row=0, column=0)
Label(frame2, text='/', bg=color, width=1).grid(row=0, column=2)

mois_f = StringVar(value='01')
Entry(frame2, textvariable=mois_f, width=2).grid(row=0, column=3)
Label(frame2, text='/', bg=color, width=1).grid(row=0, column=4)

jour_f = StringVar(value='01')
Entry(frame2, textvariable=jour_f, width=2).grid(row=0, column=5)
Label(frame2, text=' ', bg=color, width=1).grid(row=0, column=6)



Label(fenetre, text='Paramètre supplémentaire', bg=color, font=("Times 15")).grid(row=5, column=1, pady=10)


fenetre.mainloop()