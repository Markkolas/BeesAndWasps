from tkinter import *
from tkinter import ttk
import turtle

class game:

    def __init__(self, root):
        root.title("Bees & Wasps")

        #Main game turtle holder
        self._init_graphics(root)

        #Aux info turtle holder
        #TODO

        #Info place
        self._init_text(root)
        #Button place
        self._init_buttons(root)

        #Grid config
        root.columnconfigure(0, minsize=600)
        root.rowconfigure(0, minsize=600)
        root.columnconfigure(1, minsize=100)
        root.rowconfigure(1, minsize=100)

    def _init_graphics(self, root):
        graphics_holder = Canvas(root, background="black")
        graphics_holder.grid(column=0, row=0, sticky=(N, W, E, S))

        screen = turtle.TurtleScreen(graphics_holder)
        screen.bgcolor("black")

        t = turtle.RawTurtle(screen, shape="turtle")
        t.color("white")

        self.s = screen
        self.t = t

    def _init_text(self, root):
        self.info_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=5)
        self.info_frame.grid(column=0, row=1, sticky=(N, W, S, E))

        self.info_text = Text(self.info_frame, height=5)
        self.info_text.grid(column=0, row=0)
        self.info_text.configure(state="disable")


        self.scroll = Scrollbar(self.info_frame, orient=VERTICAL, command=self.info_text.yview)
        self.scroll.grid(column=1, row=0, sticky=(N,S))

    def _init_buttons(self, root):
        self.button_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=5)
        self.button_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.button1 = ttk.Button(self.button_frame, text="Test one", command=(lambda: self.winfo("Hello")))
        self.button1.grid(row=0, column=0)

        self.button2 = ttk.Button(self.button_frame, text="Test two", command=(lambda: self.winfo("Hi")))
        self.button2.grid(row=0, column=1)

    def _init_aux():
        pass

    def winfo(self, msg):
        #See: https://tkdocs.com/tutorial/text.html
        self.info_text.configure(state="normal")
        if int(self.info_text.index("end - 1 line").split('.')[0]) > 10: #Check number of lines written
            self.info_text.delete("end - 1 line", "end")
        self.info_text.insert(1.0, msg.replace("\n","")+"\n")
        self.info_text.configure(state="disable")

root = Tk()
game(root)
root.mainloop
