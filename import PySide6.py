import tkinter as tk
from tkinter import ttk
import mplfinance as mpf
import pandas as pd

# Fonction pour créer le graphique de chandelier japonais
def create_candlestick_chart():
    data = {
        'date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
        'open': [100, 105, 110, 108, 112],
        'high': [105, 112, 115, 112, 116],
        'low': [95, 100, 105, 103, 105],
        'close': [102, 110, 108, 110, 114],
    }

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    mpf.plot(df, type='candle', style='yahoo', title='Graphique de Chandelier Japonais')

# Création de la fenêtre principale Tkinter
root = tk.Tk()
root.title("Graphique de Chandelier Japonais avec Tkinter et mplfinance")

# Création d'un cadre à l'intérieur de la fenêtre
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Bouton pour générer le graphique de chandelier japonais
generate_button = ttk.Button(frame, text="Générer Chandelier Japonais", command=create_candlestick_chart)
generate_button.pack()

# Lancement de la boucle principale Tkinter
root.mainloop()