from tkinter import Tk
from tkinter.ttk import Button
from clearing_operation import ClearingOperation
from air_2_air_combat_table import AirToAirCombatTable
from air_defense_table import  AirCombatTable
from cyber_warfare_table import CyberWarfareTable
from ground_combat_table import CombatResultTable
from sof_table import SofTable
from strike_table import StrikeTable
from naval_warfare import NavalWarfare

class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        clearing_ops_btn = Button(self, text='Clearing', command=self.clearing_ops, width=15)
        clearing_ops_btn.place(x=50, y=50)
        air_2_air_btn = Button(self, text='Air To Air', command=self.air_2_air_combat, width=15)
        air_2_air_btn.place(x=50, y=80)
        air_defense_btn = Button(self, text='Air Defense', command=self.air_defense, width=15)
        air_defense_btn.place(x=50, y=110)
        cyber_warfare_btn = Button(self, text='Cyber Warfare', command=self.cyber_warfare, width=15)
        cyber_warfare_btn.place(x=50, y=140)
        ground_combat_btn = Button(self, text='Ground Combat', command=self.ground_combat, width=15)
        ground_combat_btn.place(x=150, y=110)
        special_ops_btn = Button(self, text='Special Ops', command=self.special_ops, width=15)
        special_ops_btn.place(x=150, y=50)
        strike_btn = Button(self, text='Strike', command=self.strike, width=15)
        strike_btn.place(x=150, y=80)
        naval_btn = Button(self, text='Naval', command=self.naval, width=15)
        naval_btn.place(x=150, y=140)

    def clearing_ops(self):
        window = ClearingOperation(self)
        window.grab_set()

    def air_2_air_combat(self):
        window = AirToAirCombatTable(self)
        window.grab_set()

    def air_defense(self):
        window = AirCombatTable(self)
        window.grab_set()

    def cyber_warfare(self):
        window = CyberWarfareTable(self)
        window.grab_set()

    def ground_combat(self):
        window = CombatResultTable(self)
        window.grab_set()

    def special_ops(self):
        window = SofTable(self)
        window.grab_set()

    def strike(self):
        window = StrikeTable(self)
        window.grab_set()

    def naval(self):
        window = NavalWarfare(self)
        window.grab_set()