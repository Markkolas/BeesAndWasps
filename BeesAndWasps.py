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

def cal_test_time(self):
        ntime=time.time()
        print(ntime-self.test_time)
        self.test_time = ntime
"""

def gen_worker():
    interface.winfo("Generate worker bee")

def gen_drone():
    interface.winfo("Generate drone bee")

def player_up():
    print(player.y)
    player.y = player.y + player.speed
    interface.draw_player(player.x, player.y)

def player_down():
    player.y -= player.speed
    interface.draw_player(player.x, player.y)

def player_right():
    player.x += player.speed
    interface.draw_player(player.x, player.y)

def player_left():
    player.x -= player.speed
    interface.draw_player(player.x, player.y)

callbacks = {
    "Worker" : gen_worker,
    "Drone" : gen_drone,
    "PUp" : player_up,
    "PDown" : player_down,
    "PRight" : player_right,
    "PLeft" : player_left
}

root = Tk()
interface = u.UI(root, callbacks)

player = qb.Queen(0, 0)

root.mainloop()
