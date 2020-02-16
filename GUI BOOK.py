from tkinter import *
import sys


class Window:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Print Message", command=self.print_message)
        self.entry_one = Entry(master)
        self.entry_one.bind("<Return>", self.print_message)
        self.entry_one.pack()
        self.print_button.pack(side="left")

        self.quit_button = Button(frame, text="Quit.", command=frame.quit)
        self.quit_button.pack(side="left")

    def print_message(self, *args):
        print("Testing.")


root = Tk()
main = Window(root)
root.mainloop()