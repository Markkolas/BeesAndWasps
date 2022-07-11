#All are from and "is" part of me
from tkinter import *
from tkinter import ttk
import util.user_interface as u
import bees.queen as qb
import turtle

"""
Let me explain. I want the UI to be FULLY INDEPENDENT.
So, I want the UI buttons to generate events that will be processed here,
where the tkinter mainloop is called.

Can be of use in the future:
https://stackoverflow.com/questions/31798723/tkinter-generate-and-invoke-virtual-event-between-different-widgets
"""

def gen_worker():
    interface.winfo("Generate worker bee")

def gen_drone():
    interface.winfo("Generate drone bee")

callbacks = {
    "Worker" : gen_worker,
    "Drone" : gen_drone,
}

root = Tk()
interface = u.UI(root, callbacks)

player = qb.Queen((0, 0))

print(player.get_position())

root.mainloop()
