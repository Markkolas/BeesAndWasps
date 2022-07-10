#All are from and "is" part of me
from tkinter import *
from tkinter import ttk
import user_interface as u
import turtle

root = Tk()
interface = u.UI(root)

root.bind("<<B1>>", lambda e: interface.winfo("Hello"))
root.bind("<<B2>>", lambda e: interface.winfo("Hi"))

print(root.event_info("<<B1>>"))

root.mainloop()
