import tkinter as tk

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
        # self.geometry("400x400")
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


# starting page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # changeable text message in label
        self.message = tk.StringVar()
        self.message.set("")

        # getting label message
        self.label = tk.Label(self, text="")
        self.label.grid(row=0, column=2)

        # a place to enter text
        label_one = tk.Label(self, text="What should I do?")
        label_one.grid(row=0, sticky="e")

        # place to take in data
        self.entry_one = tk.Entry(self)
        # allows pressing the enter key to get data
        self.entry_one.bind("<Return>", self.get_text)
        # places the entry location
        self.entry_one.grid(row=0, column=1)

        # makes a button that does something
        button_one = ttk.Button(self, text="go page one",
                                command=lambda: controller.show_frame(PageOne))
        button_one.grid(row=3, column=0)

        # makes a button that does something
        button_two = ttk.Button(self, text="go page two",
                                command=lambda: controller.show_frame(PageTwo))
        button_two.grid(row=3, column=2)

        button_two = ttk.Button(self, text="Enter Command",
                                command=lambda: self.get_text())
        button_two.grid(row=3, column=1)

    # needs one parameter or will not work.
    def get_text(self, event=0):
        # gets info from box
        self.message.set(self.entry_one.get())
        # sets label to entry data
        self.label.config(text=self.message.get())
        # clears entry after data is taken in
        self.entry_one.delete(0, 'end')


# page one
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # making a canvas for the image
        self.canvas = tk.Canvas(self, bg="black", height=894, width=894)
        # must keep image around with self.
        self.bg_picture = tk.PhotoImage(file="background.gif")

        # making a label to hold image
        bg_label = tk.Label(self, image=self.bg_picture)
        # placing the label
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # packing the canvas
        self.canvas.pack()

        label = tk.Label(self, text='page one')
        label.pack(pady=10, padx=10)

        # makes a button that does something
        button_one = ttk.Button(self, text="go start page",
                                command=lambda: controller.show_frame(StartPage))
        button_one.pack(side="left")

        # makes a button that does something
        button_two = ttk.Button(self, text="go page two",
                                command=lambda: controller.show_frame(PageTwo))
        button_two.pack(side="right")


# second page
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='page two')
        label.pack(pady=10, padx=10)

        # makes a button that does something
        button_one = ttk.Button(self, text="go start page",
                                command=lambda: controller.show_frame(StartPage))
        button_one.pack(side="left")

        # makes a button that does something
        button_two = ttk.Button(self, text="go page one",
                                command=lambda: controller.show_frame(PageOne))
        button_two.pack(side="right")


if __name__ == "__main__":
    app = Window()
    app.mainloop()
