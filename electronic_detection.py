from tkinter import Label, Toplevel, Radiobutton, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from random import randint

class ElectronicDetection(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Electronic Detection')
        self.geometry("280x140+10+10")

        self.side = BooleanVar()
        self.side.set(True)

        self.non_allied_r = Radiobutton(self, text='Non-allied', variable=self.side, value=False)
        self.allied_r = Radiobutton(self, text='Allied', variable=self.side, value=True)

        self.non_allied_cyber = BooleanVar()
        self.non_allied_cyber.set(False)
        self.non_allied_cyber_chk = Checkbutton(self, text='Non-allied cyberattack', variable=self.non_allied_cyber)

        self.allied_cyber = BooleanVar()
        self.allied_cyber.set(False)
        self.allied_cyber_chk = Checkbutton(self, text='Allied cyberattack', variable=self.allied_cyber)

        self.result_btn = Button(self, text='Detection', command=self.detection_result)
        self.result_lbl = Label(self, text='Det:')
        self.result_ent = Entry(self, width=5)

        self.result_btn.place(x=20, y=70)
        self.result_ent.place(x=60, y=100)
        self.result_lbl.place(x=20, y=100)
        self.non_allied_r.place(x=20, y=20)
        self.allied_r.place(x=20, y=40)
        self.allied_cyber_chk.place(x=110, y=20)
        self.non_allied_cyber_chk.place(x=110, y=40)

    def detection_result(self):
        self.result_ent.delete(0, 'end')

        d10 = randint(0, 9)

        result = '-'

        if self.side.get():
            if self.allied_cyber.get():
                d10 -= 2
            if self.non_allied_cyber.get():
                d10 += 2
            if d10 < 5:
                result = 'D'
        else:
            if self.allied_cyber.get():
                d10 += 2
            if self.non_allied_cyber.get():
                d10 -= 2
            if d10 < 3:
                result = 'D'

        self.result_ent.insert(END, result)