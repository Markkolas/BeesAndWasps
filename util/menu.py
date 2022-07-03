from tkinter import *
from tkinter import ttk

class game:

    def __init__(self, root):
        root.title("Bees & Wasps")

        #Main game turtle holder
        graphics_holder = Canvas(root, background="black")
        graphics_holder.grid(column=0, row=0, sticky=(N, W, E, S))

        #Aux info turtle holder
        #TODO

        #Info place
        info_frame = ttk.Frame(root, borderwidth=2, relief="solid")
        info_frame.grid(column=0, row=1)

        info_label = ttk.Label(info_frame, text="Sample text", width=50)
        info_label.grid(column=0, row=0)

        #Button place
        button_frame = ttk.Frame(root, borderwidth=2, relief="solid")
        button_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        info_label1 = ttk.Label(button_frame, text="Sample text", anchor=CENTER)
        info_label1.grid(column=0, row=0)

        #Grid config
        root.columnconfigure(0, minsize=600)
        root.rowconfigure(0, minsize=600)
        root.columnconfigure(1, minsize=100)
        root.rowconfigure(1, minsize=100)

        print(root.grid_slaves())

root = Tk()
game(root)
root.mainloop
