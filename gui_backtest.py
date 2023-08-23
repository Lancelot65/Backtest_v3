from tkinter import Tk, PhotoImage, Frame, Label, Button, ttk, StringVar, Toplevel, Spinbox, Checkbutton, IntVar
import sys
from ccxt import binance
sys.path.append('../trad/Ohlcvplus')
from ohlcv import OhlcvPlus
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class gui(Tk):
    def __init__(self):
        super().__init__()

        self.color = StringVar(value='lavender')

        self.option_add('*Font', 'Times 10')
        #self.configure(bg=self.color.get())
        self.resizable(False, False)
        self.title('backtest')
        self.iconphoto(True, PhotoImage(file='logo.png'))

        self.frame_reglage = Frame(self)
        self.frame_reglage.grid(row=0, column=0)
        self.reglage_simple(self.frame_reglage)
                

        self.mainloop()
    
    def reglage_simple(self, frame):
        Label(frame, text='Paramètre graphique', font=("Times 15")).grid(row=0, column=1, ipady=10)
        Label(frame, text='exchange').grid(row=1, column=0)
        Label(frame, text='type de shéma').grid(row=1, column=1)
        Label(frame, text='timeframe').grid(row=1, column=2)

        self.exchange = ttk.Combobox(frame, values=["BTC/USDT", "EUR/USDT"], state="readonly")
        self.exchange.current(0)
        self.exchange.grid(row=2, column=0, padx=5)

        self.type_graphique = ttk.Combobox(frame, values=["ligne", "bougie"], state="readonly")
        self.type_graphique.current(1)
        self.type_graphique.grid(row=2, column=1, padx=5)

        self.timeframe = ttk.Combobox(frame, values=["1m", "5m","30m","1h", "1w"], state="readonly")
        self.timeframe.current(2)
        self.timeframe.grid(row=2, column=2, padx=5)

        Label(frame, text='debut').grid(row=3, column=0)
        Label(frame, text='Fin').grid(row=3, column=2)

        frame1 = Frame(frame)
        frame1.grid(row=4, column=0)

        self.annee_debut = StringVar(value='2023')
        Spinbox(frame1, textvariable=self.annee_debut, from_=2015, to=datetime.now().year, width=4).grid(row=0, column=0)
        Label(frame1, text='/', width=1).grid(row=0, column=2)

        self.mois_debut = StringVar(value='01')
        Spinbox(frame1, textvariable=self.mois_debut, from_=1, to=12, width=2).grid(row=0, column=3)
        Label(frame1, text='/',  width=1).grid(row=0, column=4)

        self.jour_debut = StringVar(value='01')
        Spinbox(frame1, textvariable=self.jour_debut, from_=1, to=31, width=2).grid(row=0, column=5)
        Label(frame1, text=' ',  width=1).grid(row=0, column=6)




        frame2 = Frame(frame)
        frame2.grid(row=4, column=2)

        self.annee_fin = StringVar(value=datetime.now().year)
        Spinbox(frame2, textvariable=self.annee_fin, from_=2015, to=datetime.now().year, width=4).grid(row=0, column=0)
        Label(frame2, text='/', width=1).grid(row=0, column=2)

        self.mois_fin = StringVar(value=datetime.now().month)
        Spinbox(frame2, textvariable=self.mois_fin, from_=1, to=12, width=2).grid(row=0, column=3)
        Label(frame2, text='/',  width=1).grid(row=0, column=4)

        self.jour_fin = StringVar(value=datetime.now().day)
        Spinbox(frame2, textvariable=self.jour_fin, from_=1, to=31, width=2).grid(row=0, column=5)
        Label(frame2, text=' ',  width=1).grid(row=0, column=6)

        Button(frame, text='charger\ntableau', command=self.boutton_charger_press).grid(row=4, column=1)
    
    def charger_graphique(self):
        self.graphique = Toplevel(self)

        fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = fig.add_subplot(111)
        if self.type_graphique.get() == 'bougie':
            candlestick_ohlc(self.ax, self.data.values, colorup='g', colordown='r', width=0.0000002, alpha=0.9)
        else:
            self.ax.plot(self.data.timestamp, self.data.close)

        canvas = FigureCanvasTkAgg(fig, master=self.graphique)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    def charger_data(self):
        date_debut = self.annee_debut.get() + '-' + self.mois_debut.get() + '-' + self.jour_debut.get() + ' 00:00:00'
        date_fin = self.annee_fin.get() + '-' + self.mois_fin.get() + '-' + self.jour_fin.get() + ' 00:00:00'


        ohlcvp = OhlcvPlus(binance())
        self.data = ohlcvp.load(market=self.exchange.get(), timeframe=self.timeframe.get(), since=date_debut, limit=date_fin, update=True, verbose=True, workers=100)

    def boutton_charger_press(self):
        self.charger_data()
        self.charger_graphique()
    
gui()