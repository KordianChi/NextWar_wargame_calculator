from tkinter import Label, BooleanVar, IntVar, Toplevel, Radiobutton
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from random import randint
from hex_map import HexMap

class Supply(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Supply')
        self.geometry("300x250+10+10")

        self.em_supply_btn = Button(self, text='Emergency', command=self.emergency_supply)
        self.em_supply_lbl = Label(self, text='Result:')
        self.em_supply_ent = Entry(self, width=7)

        self.unit = BooleanVar()
        self.unit.set(True)

        self.hq_r = Radiobutton(self, text='HQ', variable=self.unit, value=False)
        self.ground_unit_r = Radiobutton(self, text='Unit', variable=self.unit, value=True)
        
        self.supply_source_hex_lbl = Label(self, text='Source hex:')
        self.supply_source_hex_ent = Entry(self, width=7)
        
        self.supply_target_hex_lbl = Label(self, text='Target hex:')
        self.supply_target_hex_ent = Entry(self, width=7)
        
        
        self.source_mp = IntVar()
        self.source_mp.set(6)

        self.source_mp_r1 = Radiobutton(self, text='Urban', variable=self.source_mp,
                                        value=6)
        
        self.source_mp_r2 = Radiobutton(self, text='Depot', variable=self.source_mp,
                                        value=8)
        
        self.source_mp_r3 = Radiobutton(self, text='MSU/HQ', variable=self.source_mp,
                                        value=4)
        
        self.supply_btn = Button(self, text='Supply', command=self.check_supply)
        self.supply_ent = Entry(self, width=7)
        
        self.source_mp_r1.place(x=180, y=20)
        self.source_mp_r2.place(x=180, y=60)
        self.source_mp_r3.place(x=180, y=100)
        
        self.supply_btn.place(x=30, y=100)
        self.supply_ent.place(x=110, y=100)


        self.supply_target_hex_lbl.place(x=30, y=20)
        self.supply_target_hex_ent.place(x=110, y=20)
        
        self.supply_source_hex_lbl.place(x=30, y=60)
        self.supply_source_hex_ent.place(x=110, y=60)

        self.em_supply_btn.place(x=30, y=140)
        self.hq_r.place(x=110, y=140)
        self.ground_unit_r.place(x=160, y=140)
        self.em_supply_lbl.place(x=30, y=180)
        self.em_supply_ent.place(x=80, y=180)
        
    hex_map = HexMap()
        
    def setup_hex_map(self):
        pass
        
    def check_supply(self):
        pass

    def emergency_supply(self):

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