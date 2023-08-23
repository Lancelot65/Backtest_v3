import tkinter as tk
from tkinter import ttk
from datetime import datetime

def on_datetime_selected():
    selected_datetime = f"{year_var.get()}-{month_var.get()}-{day_var.get()} {hour_var.get()}:{minute_var.get()}"
    datetime_label.config(text=f"Selected Date and Time: {selected_datetime}")

root = tk.Tk()
root.title("Calendrier avec Heure")

date_frame = ttk.Frame(root)
year_var = tk.StringVar(value=str(datetime.now().year))
year_entry = ttk.Combobox(date_frame, textvariable=year_var, values=[])
year_entry.grid(row=0, column=0, padx=5)

month_var = tk.StringVar(value=str(datetime.now().month).zfill(2))
month_entry = ttk.Combobox(date_frame, textvariable=month_var, values=[str(i).zfill(2) for i in range(1, 13)])
month_entry.grid(row=0, column=1, padx=5)

day_var = tk.StringVar(value=str(datetime.now().day).zfill(2))
day_entry = ttk.Combobox(date_frame, textvariable=day_var, values=[str(i).zfill(2) for i in range(1, 32)])
day_entry.grid(row=0, column=2, padx=5)

date_frame.pack()

time_frame = ttk.Frame(root)
hour_var = tk.StringVar(value="00")
hour_entry = ttk.Combobox(time_frame, textvariable=hour_var, values=[str(i).zfill(2) for i in range(24)])
hour_entry.grid(row=0, column=0, padx=5)

minute_var = tk.StringVar(value="00")
minute_entry = ttk.Combobox(time_frame, textvariable=minute_var, values=[str(i).zfill(2) for i in range(60)])
minute_entry.grid(row=0, column=1, padx=5)

time_frame.pack()

time_button = ttk.Button(root, text="Select Date and Time", command=on_datetime_selected)
time_button.pack(pady=(10, 0))

datetime_label = tk.Label(root, text="Selected Date and Time: ")
datetime_label.pack(padx=10, pady=(0, 10))

root.mainloop()
