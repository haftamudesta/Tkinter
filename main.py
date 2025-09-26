import tkinter as tk
from tkinter import ttk, messagebox

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 87.1,
    "GBP": 0.78,
    "GPY": 146.55,
}


def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_combo.get()
        to_currency = to_combo.get()
        if from_currency and to_currency:
            usd_amount = amount/exchange_rates[from_currency]
            converted = usd_amount*exchange_rates[to_currency]
            result_label.config(
                text=f"{amount} {from_currency}={converted:.2f} {to_currency}")
        else:
            messagebox.showerror("Error,Please select currency")
    except ValueError:
        messagebox.showerror("Error,Enter a valid Amount.")


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

tk.Button(window, text="Convert", font=(
    "Arial", 12), bg="lightblue", command=convert_currency).pack(pady=10)

result_label = tk.Label(window, text="", font=(
    "Arial", 12))
result_label.pack()
window.mainloop()
