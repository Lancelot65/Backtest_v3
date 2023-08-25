from tkinter import Tk, PhotoImage, Frame, Label, Button, ttk, StringVar, Toplevel, Spinbox, Checkbutton, IntVar, Entry, messagebox, BooleanVar
import sys
from ccxt import binance
sys.path.append('../trad/Ohlcvplus')
from ohlcv import OhlcvPlus
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.dates import date2num, DateFormatter
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

class gui(Tk):
    def __init__(self):
        super().__init__()

        self.color = StringVar(value='lavender')
        self.data = None

        self.indicateur = {}

        self.option_add('*Font', 'Times 10')
        #self.configure(bg=self.color.get())
        self.resizable(False, False)
        self.title('backtest')
        self.iconphoto(True, PhotoImage(file='logo.png'))

        self.frame_reglage = Frame(self)
        self.frame_reglage.grid(row=0, column=0)
        self.reglage_simple(self.frame_reglage)

        self.frame_ind = Frame(self)
        self.frame_ind.grid(row=1, column=0)
        self.plus_option(self.frame_ind)

        self.mainloop()
    
    def reglage_simple(self, frame):
        Label(frame, text='Paramètre graphique', font=("Times 15")).grid(row=0, column=1, ipady=10)
        Label(frame, text='exchange').grid(row=1, column=0)
        Label(frame, text='timeframe').grid(row=1, column=2)
        Button(frame, text='load data', command=lambda: self.charger_data(True)).grid(row=2, column=1, rowspan=2, ipady=10)
        

        self.exchange = ttk.Combobox(frame, values=["BTC/USDT", "EUR/USDT"], state="readonly")
        self.exchange.current(0)
        self.exchange.grid(row=2, column=0, padx=5)

        self.timeframe = ttk.Combobox(frame, values=["1m", "5m","30m","1h", "1d", "1w"], state="readonly")
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
    
    def charger_graphique(self):

        close = self.data.close
        open = self.data.open
        high = self.data.high
        low = self.data.low

        fig, ax = plt.subplots()
        self.data.timestamp = pd.to_datetime(self.data.timestamp, unit='ms').apply(date2num)
                   
        candlestick_ohlc(ax, self.data.values, colorup='g', colordown='r', width=0.0000002, alpha=0.9)
        ax.xaxis.set_major_formatter(DateFormatter('%d-%m-%Y'))
        fig.autofmt_xdate()
        fig.tight_layout()

        for ind in self.indicateur:
            if self.indicateur[ind][1].get() == True:
                ax.plot(self.data.timestamp, eval(self.indicateur[ind][0]), label=ind)
        

        self.protocol("WM_DELETE_WINDOW", self.fermer_fenetre)

        ax.legend()
        plt.show()

    def charger_data(self, forcer=False):
        if self.data is None or forcer == True:
            date_debut = self.annee_debut.get() + '-' + self.mois_debut.get() + '-' + self.jour_debut.get() + ' 00:00:00'
            date_fin = self.annee_fin.get() + '-' + self.mois_fin.get() + '-' + self.jour_fin.get() + ' 00:00:00'


            ohlcvp = OhlcvPlus(binance())
            self.data = ohlcvp.load(market=self.exchange.get(), timeframe=self.timeframe.get(), since=date_debut, limit=date_fin)

    def boutton_charger_press(self):
        self.charger_data()
        self.charger_graphique()
    
    def plus_option(self, frame):
        Label(frame, text='Reglage indicateurs', font=("Times 15")).grid(row=0, column=0, columnspan=2, ipady=10, sticky='e')
        Label(frame, text='rentrer vos formules', font=("Times 10")).grid(row=1, column=0, columnspan=2, ipady=10, sticky='e')

        self.operation = StringVar()
        Entry(frame, textvariable=self.operation).grid(row=2, column=0, sticky='w')

        self.name = StringVar()
        Entry(frame, textvariable=self.name).grid(row=3, column=0, sticky='w')

        Button(frame, text='check', command=self.validate).grid(row=2, column=1, sticky='w', padx=5)
        Button(frame, text='reinitialiser', command=self.reinitialiser).grid(row=3, column=1, sticky='w', padx=5) 

        Button(frame, text='charger\ntableau', command=self.boutton_charger_press).grid(row=4, column=0, pady=5)

        self.frame_ind = Frame(frame)
        self.frame_ind.grid(row=2, column=2)
    
    def validate(self):

        df = pd.DataFrame({'close' : [], 'open' : [], 'low' : [], 'high' : [], 'volume' : []})
        close = df.close
        open = df.open
        high = df.high
        low = df.low

        
        try:
            eval(self.operation.get())
            
            if self.name.get() in self.indicateur and messagebox.askquestion('nom existant', 'Etes vous sur de modifier le calcul associe a ce nom?'):
                self.indicateur[self.name.get()][2].destroy()

                checklist_var = BooleanVar(value=True)
                checklist = Checkbutton(self.frame_ind, text=self.name.get(), variable=checklist_var)
                checklist.grid(row=len(self.indicateur) + 1, column=3)

                
                self.indicateur[self.name.get()] = [self.operation.get(), checklist_var, checklist]
                
                self.operation.set('')
                self.name.set('')
                print(self.indicateur)
            else:
                checklist_var = BooleanVar(value=True)
                checklist = Checkbutton(self.frame_ind, text=self.name.get(), variable=checklist_var)
                checklist.grid(row=len(self.indicateur), column=3)

                
                self.indicateur[self.name.get()] = [self.operation.get(), checklist_var, checklist]
                
                self.operation.set('')
                self.name.set('')
                print(self.indicateur)
        except:
             messagebox.showerror(title='error', message='error')

    def reinitialiser(self):
        self.indicateur = {}
        for button in self.indicateur:
            button[2].destroy()
    
    def fermer_fenetre(self):
        plt.close()
        self.destroy()

        
gui()