import tkinter as tk
from tkinter import ttk, messagebox

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 87.1,
    "GBP": 0.78,
    "GPY": 146.55,
}

window = tk.Tk()

window.title("Currency Convertor")
window.geometry("400x250")

tk.Label(window, text="Amount", font=("Arial", 12)).pack()
amount_entry = tk.Entry(window, font=("Arial", 12))
amount_entry.pack()

tk.Label(window, text="From Currency", font=("Arial", 12)).pack()
from_combo = ttk.Combobox(window, values=list(
    exchange_rates.keys()), font=("Arial", 12))
from_combo.pack()

tk.Label(window, text="To Currency", font=("Arial", 12)).pack()
to_combo = ttk.Combobox(window, values=list(
    exchange_rates.keys()), font=("Arial", 12))
to_combo.pack()


window.mainloop()
