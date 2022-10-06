from tkinter import Label, BooleanVar, Toplevel, Radiobutton
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from random import randint

class Supply(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Supply')
        self.geometry("200x100+10+10")

        self.supply_btn = Button(self, text='Supply', command=self.supply_result)
        self.supply_lbl = Label(self, text='Result:')
        self.supply_ent = Entry(self, width=7)

        self.unit = BooleanVar()
        self.unit.set(True)

        self.hq_r = Radiobutton(self, text='HQ', variable=self.unit, value=False)
        self.ground_unit_r = Radiobutton(self, text='Unit', variable=self.unit, value=True)

        self.supply_btn.place(x=20, y=20)
        self.hq_r.place(x=70, y=20)
        self.ground_unit_r.place(x=120, y=20)
        self.supply_lbl.place(x=20, y=50)
        self.supply_ent.place(x=70, y=50)

    def supply_result(self):

        self.supply_ent.delete(0, 'end')

        result = '-'
        d10 = randint(0, 9)

        if self.unit:
            if d10 < 6:
                result = 'Supply'
        else:
            if d10 < 3:
                result = 'Supply'

        self.supply_ent.insert(END, result)