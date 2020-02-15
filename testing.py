import tkinter as tk


# inheriting from tk.TK
class Window(tk.Tk):
    # arguments and keyword arguments
    # args is variables usually
    # kwargs are dictionaries usually
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # container that we populate with things
        container = tk.Frame(self)
        # packed to top, filled fill the space allocated by pack, expand fill all white space
        container.pack(side="top", fill="both", expand=True)
        # something
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # dictionary of frames that we can switch between
        self.frames = {}

        # starting page
        frame = StartPage(container, self)

        self.frames[StartPage] = frame

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
        label = tk.Label(self, text='Start Page')
        label.pack(pady=10, padx=10)


app = Window()
app.mainloop()
