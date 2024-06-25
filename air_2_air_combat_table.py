from tkinter import Label, IntVar, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint
from functools import partial
from constants import AIR_COMBAT_RESULT_DOGFIGHT, AIR_COMBAT_RESULT_LONG


class AirToAirCombatTable(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Advanced Air Warfare Calculator')
        self.geometry("600x600+10+10")

        self.attacker_1_value_lbl = Label(self, text='Attacker #1:')
        self.attacker_1_value_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6'), width=5)
        self.defender_1_value_lbl = Label(self, text='Defender #1:')
        self.defender_1_value_cbx = Combobox(self, values=('#', '0', '1', '2', '3', '4', '5', '6'), width=5)
        self.attacker_1_pilot_skills_lbl = Label(self, text='Pilot skills:')
        self.attacker_1_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        self.defender_1_pilot_skills_lbl = Label(self, text='Pilot skills')
        self.defender_1_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        
        
        self.engagement_lbl = Label(self, text='Engagement:')
        self.engagement = IntVar()
        self.engagement.set(1)
        self.engagement_r1 = Radiobutton(self, text='1 vs 1', variable=self.engagement,
                                         value=1)
        self.engagement_r2 = Radiobutton(self, text='2 vs 1', variable=self.engagement,
                                         value=2)
        self.engagement_r3 = Radiobutton(self, text='1 vs 2', variable=self.engagement,
                                         value=3)

        self.distance_lbl = Label(self, text='Distance:')
        self.actual_distance = IntVar()
        self.actual_distance.set(1)
        self.distance_r1 = Radiobutton(self, text="Long Range", variable=self.actual_distance,
                                       value=1, command=partial(self.skill_active, self.actual_distance))
        self.distance_r2 = Radiobutton(self, text="Stand-off", variable=self.actual_distance,
                                       value=2, command=partial(self.skill_active, self.actual_distance))
        self.distance_r3 = Radiobutton(self, text="Dogfight", variable=self.actual_distance,
                                       value=3, command=partial(self.skill_active, self.actual_distance))

        self.weather_lbl = Label(self, text='Weather:')
        self.actual_weather = IntVar()
        self.actual_weather.set(1)
        self.weather_r1 = Radiobutton(self, text="Clear", variable=self.actual_weather, value=1)
        self.weather_r2 = Radiobutton(self, text="Overcast", variable=self.actual_weather, value=2)
        self.weather_r3 = Radiobutton(self, text="Storm", variable=self.actual_weather, value=3)

        self.attacker_1_d10_lbl = Label(self, text='dice d10:')

        self.attacker_1_drm_lbl = Label(self, text='DRMs:')

        self.attacker_1_result_lbl = Label(self, text='Result:')

        self.defender_1_d10_lbl = Label(self, text='dice d10:')

        self.defender_1_drm_lbl = Label(self, text='DRMs:')

        self.defender_1_result_lbl = Label(self, text='Result:')

        self.not_mutual = BooleanVar()
        self.not_mutual.set(False)
        self.not_mutual_chk = Checkbutton(self, text='defend only', variable=self.not_mutual)

        self.not_proper_1_att = BooleanVar()
        self.not_proper_1_att.set(False)
        self.not_proper_1_att_chk = Checkbutton(self, text='not NATO/US/JPN/PRC', variable=self.not_proper_1_att,
                                              state='disabled')

        self.strike_1_att = BooleanVar()
        self.strike_1_att.set(False)
        self.strike_1_att_chk = Checkbutton(self, text='CS firing', variable=self.strike_1_att)

        self.strike_1_def = BooleanVar()
        self.strike_1_def.set(False)
        self.strike_1_def_chk = Checkbutton(self, text='CS firing', variable=self.strike_1_def)

        self.not_proper_1_def = BooleanVar()
        self.not_proper_1_def.set(False)
        self.not_proper_1_def_chk = Checkbutton(self, text='not NATO/US/JPN/PRC',
                                              variable=self.not_proper_1_def, state='disabled')

        self.air_2_air_btn = Button(self, text='Calculate', command=self.calculate_a2a)

        self.result_att_1_ent = Entry(self, width=7)
        self.d10_att_1_ent = Entry(self, width=7)
        self.DRM_att_1_ent = Entry(self, width=7)
        self.d10_def_1_ent = Entry(self, width=7)
        self.DRM_def_1_ent = Entry(self, width=7)
        self.result_def_1_ent = Entry(self, width=7)

        self.attacker_1_value_lbl.place(x=50, y=30)
        self.attacker_1_pilot_skills_lbl.place(x=50, y=60)
        self.defender_1_value_lbl.place(x=250, y=30)
        self.defender_1_pilot_skills_lbl.place(x=250, y=60)
        self.attacker_1_value_cbx.place(x=150, y=30)
        self.attacker_1_pilot_skills_cbx.place(x=150, y=60)
        self.defender_1_value_cbx.place(x=350, y=30)
        self.defender_1_pilot_skills_cbx.place(x=350, y=60)
        self.strike_1_def_chk.place(x=250, y=90)
        self.not_proper_1_def_chk.place(x=250, y=120)
        self.distance_lbl.place(x=450, y=30)
        self.distance_r1.place(x=450, y=60)
        self.distance_r2.place(x=450, y=90)
        self.distance_r3.place(x=450, y=120)
        self.weather_lbl.place(x=450, y=150)
        self.weather_r1.place(x=450, y=180)
        self.weather_r2.place(x=450, y=210)
        self.weather_r3.place(x=450, y=240)
        self.engagement_lbl.place(x=450, y=270)
        self.engagement_r1.place(x=450, y=300)
        self.engagement_r2.place(x=450, y=330)
        self.engagement_r3.place(x=450, y=360)
        self.strike_1_att_chk.place(x=50, y=90)
        self.not_proper_1_att_chk.place(x=50, y=120)
        self.air_2_air_btn.place(x=50, y=270)
        self.d10_att_1_ent.place(x=150, y=330)
        self.DRM_att_1_ent.place(x=150, y=300)
        self.result_att_1_ent.place(x=150, y=360)
        self.d10_def_1_ent.place(x=350, y=330)
        self.DRM_def_1_ent.place(x=350, y=300)
        self.result_def_1_ent.place(x=350, y=360)
        self.not_mutual_chk.place(x=350, y=90)
        self.attacker_1_d10_lbl.place(x=50, y=330)
        self.attacker_1_drm_lbl.place(x=50, y=300)
        self.attacker_1_result_lbl.place(x=50, y=360)
        self.defender_1_d10_lbl.place(x=250, y=330)
        self.defender_1_drm_lbl.place(x=250, y=300)
        self.defender_1_result_lbl.place(x=250, y=360)

    def skill_active(self, actual_distance):
        actual_distance = actual_distance.get()
        if actual_distance == 3:
            self.attacker_1_pilot_skills_cbx.config(state='normal')
            self.defender_1_pilot_skills_cbx.config(state='normal')
        else:
            self.attacker_1_pilot_skills_cbx.config(state='disabled')
            self.defender_1_pilot_skills_cbx.config(state='disabled')
        if actual_distance == 2:
            self.not_proper_1_att_chk.config(state='normal')
            self.not_proper_1_def_chk.config(state='normal')
        else:
            self.not_proper_1_att_chk.config(state='disabled')
            self.not_proper_1_def_chk.config(state='disabled')

    def calculate_a2a(self):

        self.d10_att_1_ent.delete(0, 'end')
        self.DRM_att_1_ent.delete(0, 'end')
        self.result_att_1_ent.delete(0, 'end')
        self.d10_def_1_ent.delete(0, 'end')
        self.DRM_def_1_ent.delete(0, 'end')
        self.result_def_1_ent.delete(0, 'end')

        if self.defender_value_cbx.get() == '#':
            target = 0
        else:
            target = int(self.defender_1_value_cbx.get())
        fire = int(self.attacker_1_value_cbx.get())
        diff_att = fire - target
        if diff_att > 4:
            diff_att = 4
        if diff_att < -4:
            diff_att = -4
        column_att = -diff_att + 4

        d10_att = randint(0, 9)
        DRM_att = 0
        if self.actual_weather.get() == 3:
            DRM_att += 3
        if self.strike_1_att.get():
            DRM_att += 2
        if target == 0 and self.actual_distance.get() == 2:
            DRM_att -= 1
        if self.not_proper_1_att.get() and self.actual_distance.get() == 2:
            DRM_att += 1
        if self.actual_distance.get() == 3:
            skill_att = int(self.attacker_1_pilot_skills_cbx.get())
            DRM_att += skill_att
        if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
            DRM_att += 1

        row_att = d10_att + DRM_att
        if row_att > 10:
            row_att = 10
        if row_att < -2:
            row_att = -2
        row_att += 2

        if self.actual_distance.get() == 3:
            result_att = AIR_COMBAT_RESULT_DOGFIGHT[column_att][row_att]
        else:
            result_att = AIR_COMBAT_RESULT_LONG[column_att][row_att]

        vs_bomber = target == 0

        if not self.not_mutual.get() and not vs_bomber:

            diff_def = target - fire

            if diff_def > 4:
                diff_def = 4
            if diff_def < -4:
                diff_def = -4
            column_def = -diff_def + 4

            d10_def = randint(0, 9)
            DRM_def = 0

            if self.actual_weather.get() == 3:
                DRM_def += 3
            if self.strike_def.get():
                DRM_def += 2
            if target == 0 and self.actual_distance.get() == 2:
                DRM_def -= 1
            if self.not_proper_1_def.get() and self.actual_distance.get() == 2:
                DRM_def += 1
            if self.actual_distance.get() == 3:
                skill_def = int(self.defender_1_pilot_skills_cbx.get())
                DRM_def += skill_def
            if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
                DRM_def += 1

            row_def = d10_def + DRM_def
            if row_def > 10:
                row_def = 10
            if row_def < -2:
                row_def = -2
            row_def += 2

            if self.actual_distance.get() == 3:
                result_def = AIR_COMBAT_RESULT_DOGFIGHT[column_def][row_def]
            else:
                result_def = AIR_COMBAT_RESULT_LONG[column_def][row_def]
        else:
            d10_def = '-'
            DRM_def = '-'
            result_def = '-'

        self.result_att_1_ent.insert(END, result_att)
        self.DRM_att_1_ent.insert(END, str(DRM_att))
        self.d10_att_1_ent.insert(END, str(d10_att))
        self.d10_def_1_ent.insert(END, str(d10_def))
        self.DRM_def_1_ent.insert(END, str(DRM_def))
        self.result_def_1_ent.insert(END, str(result_def))

        self.not_proper_1_att.set(False)
        self.strike_1_att.set(False)
        self.not_proper_1_def.set(False)
        self.strike_1_def.set(False)
        self.not_mutual.set(False)
