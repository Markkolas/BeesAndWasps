from tkinter import *
from tkinter import ttk

game_window = Tk()
game_window.title("Bees&Wasps")
game_window.geometry("800x800")

mainframe = ttk.Frame(game_window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
game_window.columnconfigure(0, weight=1)
game_window.rowconfigure(0, weight=1)

message = StringVar()

ttk.Button(mainframe, text="Play", command=(lambda: message.set("PLAY :D")))\
    .grid(column=0, row=0, sticky=(N, S, E, W))
ttk.Button(mainframe, text="Quit", command=(lambda: message.set(":(")))\
    .grid(column=0, row=1, sticky=(N, S, E, W))

ttk.Label(mainframe, textvariable=message, font=("Arial", 100))\
    .grid(column=0, row=2, sticky=(N, S, E, W))

game_window.mainloop()
