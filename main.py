import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

exchange_rates = {"USD": 1.0}


def fetch_exchange_rates():
    try:
        response = requests.get(
            "https://api.exchangerate-api.com/v4/latest/USD", timeout=10)

        if response.status_code == 200:
            data = response.json()
            rates = data.get('rates', {})
            if rates:
                exchange_rates.update(rates)
                exchange_rates["USD"] = 1.0
                sorted_currencies = sorted(exchange_rates.keys())
                exchange_rates.update(sorted_currencies)

            last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True, "Rates updated successfully!"
        else:
            return False, "Failed to fetch rates. Using cached rates."
    except requests.exceptions.RequestException as e:
        return False, f"Network error: {str(e)}. Using cached rates."
    except Exception as e:
        return False, f"Error: {str(e)}. Using cached rates."


fetch_exchange_rates()


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
window.title("Currency Converter with Real-Time Rates")
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
