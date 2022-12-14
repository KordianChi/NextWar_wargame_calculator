from tkinter import Label, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from random import randint
from constants import MISSION_TO_NUMBER, CYBER_WARFARE_TABLE


class CyberWarfareTable(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title('Cyber Warfare Table')
        self.geometry("300x270+10+10")

        self.cwc_mission_lbl = Label(self, text='Mission:')
        self.cwc_mission_cbx = Combobox(self, values=('UN Resolution', 'Electronic Detection', 'Air Superiority',
                                                      'Strike Phase', 'Ground Combat'), width=18)
        self.cwc_mission_cbx.set('Ground Combat')
        self.cwc_attack_lbl = Label(self, text='CW Attacker:')
        self.cwc_attack_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6', '7'), width=4)
        self.cwc_attack_cbx.set('0')
        self.cwc_attack_surv_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6', '7'), width=4)
        self.cwc_attack_surv_cbx.set('0')

        self.cwc_defend_lbl = Label(self, text='CW Defender:')
        self.cwc_defend_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6', '7'), width=4)
        self.cwc_defend_cbx.set('0')
        self.cwc_defend_surv_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6', '7'), width=4)
        self.cwc_defend_surv_cbx.set('0')

        self.cwc_first_turn_attack = BooleanVar()
        self.cwc_first_turn_attack.set(False)
        self.cwc_first_turn_attack_chk = Checkbutton(self, text='First Turn Attack DRM',
                                                     variable=self.cwc_first_turn_attack)
        self.calculate_cyber_btn = Button(self, text='Result', command=self.calculate_cyber)
        self.result_lbl = Label(self, text='Result:')
        self.result_ent = Entry(self, width=7)
        self.attack_survive_lbl = Label(self, text='Attacker survive:')
        self.attack_survive_ent = Entry(self, width=7)
        self.defender_survive_lbl = Label(self, text='Defender survive:')
        self.defender_survive_ent = Entry(self, width=7)

        self.cwc_mission_lbl.place(x=20, y=10)
        self.cwc_mission_cbx.place(x=120, y=10)
        self.cwc_attack_lbl.place(x=20, y=40)
        self.cwc_attack_cbx.place(x=120, y=40)
        self.cwc_attack_surv_cbx.place(x=180, y=40)
        self.cwc_defend_lbl.place(x=20, y=70)
        self.cwc_defend_cbx.place(x=120, y=70)
        self.cwc_defend_surv_cbx.place(x=180, y=70)
        self.cwc_first_turn_attack_chk.place(x=20, y=100)
        self.calculate_cyber_btn.place(x=20, y=130)
        self.result_lbl.place(x=20, y=160)
        self.result_ent.place(x=120, y=160)
        self.attack_survive_lbl.place(x=20, y=190)
        self.attack_survive_ent.place(x=120, y=190)
        self.defender_survive_lbl.place(x=20, y=220)
        self.defender_survive_ent.place(x=120, y=220)

    def calculate_cyber(self):
        self.attack_survive_ent.delete(0, 'end')
        self.defender_survive_ent.delete(0, 'end')
        self.result_ent.delete(0, 'end')

        mission_number = MISSION_TO_NUMBER[self.cwc_mission_cbx.get()]
        row = CYBER_WARFARE_TABLE[mission_number]
        attack_value = int(self.cwc_attack_cbx.get()) - int(self.cwc_defend_cbx.get())
        if attack_value < 0:
            attack_value = 0
        value = row[attack_value]
        d10 = randint(0, 9)
        if d10 < value:
            result = 'Success'
        else:
            result = 'Fail'

        d10_att_suv = randint(0, 9)
        if d10_att_suv < int(self.cwc_attack_surv_cbx.get()):
            att_survive = 'Yes'
        else:
            if d10_att_suv > int(self.cwc_attack_surv_cbx.get()):
                att_survive = 'No'
            else:
                att_survive = 'Reset'

        if int(self.cwc_defend_cbx.get()) == 0:
            def_survive = '-'
        else:
            d10_def_suv = randint(0, 9)
            if d10_def_suv < int(self.cwc_defend_surv_cbx.get()):
                def_survive = 'Yes'
            else:
                if d10_def_suv > int(self.cwc_defend_surv_cbx.get()):
                    def_survive = 'No'
                else:
                    def_survive = 'Reset'
        self.attack_survive_ent.insert(END, att_survive)
        self.defender_survive_ent.insert(END, def_survive)
        self.result_ent.insert(END, result)
