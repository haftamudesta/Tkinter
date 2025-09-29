import tkinter as tk


class MyApp(tk.Frame):
    def __init__(self, root):
        self.color1 = "#222448"
        self.color2 = "54527E"
        self.color3 = "WHITE"
        super().__init__(
            root,
            bg=self.color1
        )
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.coluumnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)


window = tk.Tk()
window.title("Multipage App")
window.geometry("700x500")
window.resizable(width=False, height=False)
window.mainloop()
