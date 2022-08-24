from tkinter import Label, IntVar, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import Tk
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint

class MyWindow:

    def __init__(self, win):
        pass


window = Tk()
mywin = MyWindow(window)
window.title('SOF Calculator')
window.geometry("600x600+10+10")
window.mainloop()
