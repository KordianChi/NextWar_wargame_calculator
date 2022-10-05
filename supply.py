from tkinter import Label, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from random import randint

class Supply(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Supply')
        self.geometry("300x270+10+10")