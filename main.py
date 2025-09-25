import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get().strip()
    if task != "":
        list_box.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    try:
        selected_task_index = list_box.curselection()[0]
        list_box.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


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

list_box = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
list_box.pack(pady=10)

root.mainloop()
