#All are from and "is" part of me
from tkinter import *
import time
import turtle

class UI:

    test_time = 0
    def __init__(self, root):
        root.title("Bees & Wasps")

        #Main game turtle holder
        self._init_graphics(root)

        #Aux info turtle holder
        self._init_info_graphs(root)

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
        graphics_holder = Canvas(root, background="black", width=800, height=600)
        graphics_holder.grid(column=0, row=0)
        #It actually creates a 802x602 canvas

        screen = turtle.TurtleScreen(graphics_holder)
        screen.bgcolor("black")

        t = turtle.RawTurtle(screen, shape="square")
        t.color("white")
        t.penup()
        t.speed(0)

        screen.listen()
        screen.onkeypress(self.goup, "w")
        screen.onkeypress(self.godown, "s")
        screen.onkeypress(self.goleft, "a")
        screen.onkeypress(self.goright, "d")

        self.s = screen
        self.t = t

    def _init_info_graphs(self, root):
        graphics_holder = Canvas(root, background="black", width=80, height=80)
        graphics_holder.grid(column=1, row=1)

        screen = turtle.TurtleScreen(graphics_holder)
        screen.bgcolor("black")

        t = turtle.RawTurtle(screen, shape="square")
        t.color("white")

        self.si = screen
        self.ti = t

    def _init_text(self, root):
        self.info_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=5)
        self.info_frame.grid(column=0, row=1, sticky=(N, W, S, E))

        self.info_text = Text(self.info_frame, height=5, width=100, background="black", foreground="white")
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

    def winfo(self, msg):
        #See: https://tkdocs.com/tutorial/text.html
        self.info_text.configure(state="normal")
        if int(self.info_text.index("end - 1 line").split('.')[0]) > 10: #Check number of lines written
            self.info_text.delete("end - 1 line", "end")
        self.info_text.insert(1.0, msg.replace("\n","")+"\n")
        self.info_text.configure(state="disable")

    def cal_test_time(self):
        ntime=time.time()
        print(ntime-self.test_time)
        self.test_time = ntime

    def goup(self):
        self.cal_test_time()
        self.t.seth(90)
        self.t.forward(1)

    def godown(self):
        self.cal_test_time()
        self.t.seth(270)
        self.t.forward(1)

    def goright(self):
        self.cal_test_time()
        self.t.seth(0)
        self.t.forward(1)

    def goleft(self):
        self.cal_test_time()
        self.t.seth(180)
        self.t.forward(1)


root = Tk()
interface = UI(root)
root.mainloop()
