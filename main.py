import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "task.json"


def load_task():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                tasks = json.load(f)
                for task in tasks:
                    list_box.insert(tk.END, task)
            except json.JSONDecodeError:
                pass


def save_task():
    tasks = list_box.get(0, tk.END)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    task = entry.get().strip()
    if task != "":
        list_box.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_task()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    try:
        selected_task_index = list_box.curselection()[0]
        list_box.delete(selected_task_index)
        save_task()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


def clear_all_tasks():
    if list_box.size() > 0:
        response = messagebox.askyesno(
            "Confirm", "Are you sure you want to delete all tasks?")
        if response:
            list_box.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "No tasks to clear!")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task",
                          width=15, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear all Tasks",
                         width=15, command=clear_all_tasks)
clear_button.pack(pady=5)

list_box = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
list_box.pack(pady=10)

load_task()

root.mainloop()
