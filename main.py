from tkinter import Tk
from tkinter.ttk import Button
from clearing_operation import ClearingOperation
from air_2_air_combat_table import AirToAirCombatTable
from air_defense_table import  AirCombatTable
from cyber_warfare_table import CyberWarfareTable
from ground_combat_table import CombatResultTable
from sof_table import SofTable
from strike_table import StrikeTable

class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        clearing_ops_btn = Button(self, text='Clearing', command=self.clearing_ops)
        clearing_ops_btn.place(x=50, y=50)
        air_2_air_btn = Button(self, text='Air To Air', command=self.air_2_air_combat)
        air_2_air_btn.place(x=50, y=80)
        air_defense_btn = Button(self, text='Air Defense', command=self.air_defense)
        air_defense_btn.place(x=50, y=110)
        cyber_warfare_btn = Button(self, text='Cyber Warfare', command=self.cyber_warfare)
        cyber_warfare_btn.place(x=50, y=140)
        ground_combat_btn = Button(self, text='Ground Combat', command=self.ground_combat)
        ground_combat_btn.place(x=50, y=170)
        special_ops_btn = Button(self, text='Special Ops', command=self.special_ops)
        special_ops_btn.place(x=150, y=50)
        strike_btn = Button(self, text='Strike', command=self.strike)
        strike_btn.place(x=150, y=80)

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


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()