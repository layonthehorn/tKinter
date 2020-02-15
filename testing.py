import tkinter as tk
import glob
import os
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

        # to load window image
        img = tk.PhotoImage(file="icon.gif")
        self.tk.call('wm', 'iconphoto', self._w, img)
        # set title of window
        tk.Tk.wm_title(self, "Vern's Adventure")
        # container that we populate with things
        container = tk.Frame(self)
        # packed to top, filled fill the space allocated by pack, expand fill all white space
        container.pack(side="top", fill="both", expand=True)
        # something
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # dictionary of frames that we can switch between
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            # starting page
            frame = F(container, self)

            self.frames[F] = frame

            # assigning row and column of grid.
            # sticky to each side equally. stretches
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='start page')
        label.pack(pady=10, padx=10)

        # makes a button that does something
        button_one = ttk.Button(self, text="go page one",
                               command=lambda: controller.show_frame(PageOne))
        button_one.pack()

        # makes a button that does something
        button_two = ttk.Button(self, text="go page two",
                               command=lambda: controller.show_frame(PageTwo))
        button_two.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='page one')
        label.pack(pady=10, padx=10)

        # makes a button that does something
        button_one = ttk.Button(self, text="go start page",
                               command=lambda: controller.show_frame(StartPage))
        button_one.pack()

        # makes a button that does something
        button_two = ttk.Button(self, text="go page two",
                               command=lambda: controller.show_frame(PageTwo))
        button_two.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='page two')
        label.pack(pady=10, padx=10)

        # makes a button that does something
        button_one = ttk.Button(self, text="go start page",
                               command=lambda: controller.show_frame(StartPage))
        button_one.pack()

        # makes a button that does something
        button_two = ttk.Button(self, text="go page one",
                               command=lambda: controller.show_frame(PageOne))
        button_two.pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()
