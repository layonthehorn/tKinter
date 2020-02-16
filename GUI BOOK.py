import tkinter as tk
import sys

# for nicer buttons
from tkinter import ttk


# inheriting from tk.TK
class Window(tk.Tk):

    # arguments and keyword arguments
    # args is variables usually
    # kwargs are dictionaries usually
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.print_button = tk.Button(self, text="Print Message", command=self.print_message)
        self.entry_one = tk.Entry(self)
        self.entry_one.bind("<Return>", self.print_message)
        self.entry_one.pack()
        self.print_button.pack(side="left")

        self.quit_button = tk.Button(self, text="Quit.", command=sys.exit)
        self.quit_button.pack(side="left")

    def print_message(self, *args):
        print("Testing.")


app = Window()
app.mainloop()
