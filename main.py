import tkinter as tk
from tkinter import ttk, messagebox

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 87.1,
    "GBP": 0.78,
    "JPY": 146.55,
    "CAD": 1.35,
    "AUD": 1.52,
    "CHF": 0.88,
    "CNY": 7.18,
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
window.resizable(False, False)

tk.Label(window, text="Amount", font=("Arial", 12)).pack()
amount_entry = tk.Entry(window, font=("Arial", 12))
amount_entry.pack()
amount_entry.focus()

tk.Label(window, text="From Currency", font=("Arial", 12)).pack()
from_combo = ttk.Combobox(window, values=list(
    exchange_rates.keys()), font=("Arial", 12), state="readonly")
from_combo.pack()
from_combo.set("USD")  # Set default value

tk.Label(window, text="To Currency", font=("Arial", 12)).pack()
to_combo = ttk.Combobox(window, values=list(
    exchange_rates.keys()), font=("Arial", 12), state="readonly")
to_combo.pack()
to_combo.set("EUR")  # Set default value

tk.Button(window, text="Convert", font=(
    "Arial", 12), bg="lightblue", command=convert_currency).pack(pady=10)
# Bind Enter key to convert function
window.bind('<Return>', lambda event: convert_currency())

result_label = tk.Label(window, text="", font=(
    "Arial", 12))
result_label.pack()
window.mainloop()
