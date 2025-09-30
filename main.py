import tkinter as tk


class MyApp(tk.Frame):
    def __init__(self, window):
        self.current_page_index = 0
        self.pages = [self.page1, self.page2, self.page3, self.page4]
        self.color1 = "#222448"
        self.color2 = "#54527E"
        self.color3 = "WHITE"
        super().__init__(
            window,
            bg=self.color1
        )
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_page_container()
        self.create_pager()
        self.pages[self.current_page_index]()

    def create_page_container(self):
        self.page_container = tk.Frame(
            self.main_frame,
            background=self.color1
        )
        self.page_container.columnconfigure(0, weight=1)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=1)
        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)

    def create_pager(self):
        self.pager = tk.Frame(
            self.main_frame,
            background=self.color1,
            height=125,
            width=400,
        )
        self.pager.columnconfigure(0, weight=1)
        self.pager.columnconfigure(1, weight=1)
        self.pager.rowconfigure(0, weight=1)
        self.pager.grid(column=0, row=1, sticky=tk.NSEW)
        self.pager.grid_propagate(0)

        prev_button = tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            disabledforeground="#3B3A56",
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=("Arial", 18),
            cursor="hand1",
            text="Previous",
            state=tk.DISABLED
        )
        prev_button.grid(column=0, row=0)

        self.page_number = tk.Label(
            self.pager,
            background=self.color1,
            foreground=self.color3,
            font=("Arial", 18)
        )
        self.page_number.grid(column=1, row=0)

        next_button = tk.Button(
            self.pager,
            background=self.color2,
            foreground=self.color3,
            activebackground=self.color2,
            disabledforeground="#3B3A56",
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=("Arial", 18),
            cursor="hand1",
            text="Next"
        )
        next_button.grid(column=2, row=0)

    def page1(self):
        title = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color2,
            height=2,
            font=("Arial", 26, "bold"),
            text="Page 1"
        )
        title.grid(column=0, row=0)
        text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'''
        content = tk.Label(
            self.page_container,
            background=self.color2,
            foreground=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)

    def page2(self):
        title = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color2,
            height=2,
            font=("Arial", 26, "bold"),
            text="Page 2"
        )
        title.grid(column=0, row=0)
        text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.'''
        content = tk.Label(
            self.main_frame,
            background=self.color2,
            foreground=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)

    def page3(self):
        title = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color2,
            height=2,
            font=("Arial", 26, "bold"),
            text="Page 3"
        )
        title.grid(column=0, row=0)
        text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.'''
        content = tk.Label(
            self.main_frame,
            background=self.color2,
            foreground=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)

    def page4(self):
        title = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color2,
            height=2,
            font=("Arial", 26, "bold"),
            text="Page 3"
        )
        title.grid(column=0, row=0)
        text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
        content = tk.Label(
            self.main_frame,
            background=self.color2,
            foreground=self.color3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)


window = tk.Tk()
window.title("Multipage App")
window.geometry("700x500")
window.resizable(width=False, height=False)
multi_page = MyApp(window)
window.mainloop()
