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
        self.attacker_2_value_lbl = Label(self, text='Attacker #2:')
        self.attacker_1_value_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6'), width=5)
        self.attacker_2_value_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6'), width=5)
        
        self.defender_1_value_lbl = Label(self, text='Defender #1:')
        self.defender_2_value_lbl = Label(self, text='Defender #2:')
        self.defender_1_value_cbx = Combobox(self, values=('#', '0', '1', '2', '3', '4', '5', '6'), width=5)
        self.defender_2_value_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6'), width=5)
        
        self.attacker_1_pilot_skills_lbl = Label(self, text='Pilot skills:')
        self.attacker_2_pilot_skills_lbl = Label(self, text='Pilot skills:')
        self.attacker_1_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        self.attacker_2_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        
        self.defender_1_pilot_skills_lbl = Label(self, text='Pilot skills')
        self.defender_2_pilot_skills_lbl = Label(self, text='Pilot skills')
        self.defender_1_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        self.defender_2_pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        
        
        self.engagement_lbl = Label(self, text='Engagement:')
        self.engagement = IntVar()
        self.engagement.set(1)
        self.engagement_r1 = Radiobutton(self, text='1 vs 1', variable=self.engagement,
                                         value=1, command=partial(self.combat_active, self.engagement))
        self.engagement_r2 = Radiobutton(self, text='2 vs 1', variable=self.engagement,
                                         value=2, command=partial(self.combat_active, self.engagement))
        self.engagement_r3 = Radiobutton(self, text='1 vs 2', variable=self.engagement,
                                         value=3, command=partial(self.combat_active, self.engagement))

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
        
        self.attacker_2_d10_lbl = Label(self, text='dice d10:')

        self.attacker_2_drm_lbl = Label(self, text='DRMs:')

        self.attacker_2_result_lbl = Label(self, text='Result:')

        self.defender_2_d10_lbl = Label(self, text='dice d10:')

        self.defender_2_drm_lbl = Label(self, text='DRMs:')

        self.defender_2_result_lbl = Label(self, text='Result:')

        self.not_mutual_1_att = BooleanVar()
        self.not_mutual_1_att.set(False)
        self.not_mutual_chk_1_att = Checkbutton(self, text='defend only', variable=self.not_mutual_1_att)
        
        self.not_mutual_2_att = BooleanVar()
        self.not_mutual_2_att.set(False)
        self.not_mutual_chk_2_att = Checkbutton(self, text='defend only', variable=self.not_mutual_2_att)

        self.not_proper_1_att = BooleanVar()
        self.not_proper_1_att.set(False)
        self.not_proper_1_att_chk = Checkbutton(self, text='not NATO/US/JPN/PRC', variable=self.not_proper_1_att,
                                              state='disabled')
        
        self.not_proper_2_att = BooleanVar()
        self.not_proper_2_att.set(False)
        self.not_proper_2_att_chk = Checkbutton(self, text='not NATO/US/JPN/PRC', variable=self.not_proper_2_att,
                                              state='disabled')

        self.strike_1_att = BooleanVar()
        self.strike_1_att.set(False)
        self.strike_1_att_chk = Checkbutton(self, text='CS firing', variable=self.strike_1_att)
        
        self.strike_2_att = BooleanVar()
        self.strike_2_att.set(False)
        self.strike_2_att_chk = Checkbutton(self, text='CS firing', variable=self.strike_2_att)

        self.strike_1_def = BooleanVar()
        self.strike_1_def.set(False)
        self.strike_1_def_chk = Checkbutton(self, text='CS firing', variable=self.strike_1_def)

        self.not_proper_1_def = BooleanVar()
        self.not_proper_1_def.set(False)
        self.not_proper_1_def_chk = Checkbutton(self, text='not NATO/US/JPN/PRC',
                                              variable=self.not_proper_1_def, state='disabled')
        
        
        self.strike_2_def = BooleanVar()
        self.strike_2_def.set(False)
        self.strike_2_def_chk = Checkbutton(self, text='CS firing', variable=self.strike_2_def)

        self.not_proper_2_def = BooleanVar()
        self.not_proper_2_def.set(False)
        self.not_proper_2_def_chk = Checkbutton(self, text='not NATO/US/JPN/PRC',
                                              variable=self.not_proper_2_def, state='disabled')
        


        self.not_mutual_1_def = BooleanVar()
        self.not_mutual_1_def.set(False)
        self.not_mutual_chk_1_def = Checkbutton(self, text='defend only', variable=self.not_mutual_1_def)
        
        self.not_mutual_2_def = BooleanVar()
        self.not_mutual_2_def.set(False)
        self.not_mutual_chk_2_def = Checkbutton(self, text='defend only', variable=self.not_mutual_2_def)

        self.air_2_air_btn = Button(self, text='Calculate', command=self.calculate_a2a)
        
        self.clear_all_air_btn = Button(self, text='Clear all', command=self.clear_all_air)

        self.result_att_1_ent = Entry(self, width=7)
        self.d10_att_1_ent = Entry(self, width=7)
        self.DRM_att_1_ent = Entry(self, width=7)
        self.d10_def_1_ent = Entry(self, width=7)
        self.DRM_def_1_ent = Entry(self, width=7)
        self.result_def_1_ent = Entry(self, width=7)
        
        self.result_att_2_ent = Entry(self, width=7)
        self.d10_att_2_ent = Entry(self, width=7)
        self.DRM_att_2_ent = Entry(self, width=7)
        self.d10_def_2_ent = Entry(self, width=7)
        self.DRM_def_2_ent = Entry(self, width=7)
        self.result_def_2_ent = Entry(self, width=7)

        self.attacker_1_value_lbl.place(x=50, y=30)
        self.attacker_1_pilot_skills_lbl.place(x=50, y=60)
        
        self.attacker_2_value_lbl.place(x=50, y=150)
        self.attacker_2_pilot_skills_lbl.place(x=50, y=180)
        self.attacker_2_value_cbx.place(x=150, y=150)
        self.attacker_2_pilot_skills_cbx.place(x=150, y=180)
        self.strike_2_att_chk.place(x=50, y=210)
        self.not_proper_2_att_chk.place(x=50, y=240)
        
        self.defender_1_value_lbl.place(x=260, y=30)
        self.defender_1_pilot_skills_lbl.place(x=260, y=60)
        self.attacker_1_value_cbx.place(x=150, y=30)
        self.attacker_1_pilot_skills_cbx.place(x=150, y=60)
        
        self.defender_2_value_lbl.place(x=260, y=150)
        self.defender_2_pilot_skills_lbl.place(x=260, y=180)
        self.defender_2_value_cbx.place(x=360, y=150)
        self.defender_2_pilot_skills_cbx.place(x=360, y=180)
        self.strike_2_def_chk.place(x=260, y=210)
        self.not_proper_2_def_chk.place(x=260, y=240)
        self.not_mutual_chk_2_def.place(x=360, y=210)
        
        
        
        self.not_mutual_chk_1_att.place(x=150, y=90)
        self.not_mutual_chk_1_def.place(x=360, y=90)
        self.defender_1_value_cbx.place(x=360, y=30)
        self.defender_1_pilot_skills_cbx.place(x=360, y=60)
        self.strike_1_def_chk.place(x=260, y=90)
        self.not_proper_1_def_chk.place(x=260, y=120)
        self.distance_lbl.place(x=460, y=30)
        self.distance_r1.place(x=460, y=60)
        self.distance_r2.place(x=460, y=90)
        self.distance_r3.place(x=460, y=120)
        self.weather_lbl.place(x=460, y=150)
        self.weather_r1.place(x=460, y=180)
        self.weather_r2.place(x=460, y=210)
        self.weather_r3.place(x=460, y=240)
        self.engagement_lbl.place(x=460, y=270)
        self.engagement_r1.place(x=460, y=300)
        self.engagement_r2.place(x=460, y=330)
        self.engagement_r3.place(x=460, y=360)
        self.strike_1_att_chk.place(x=50, y=90)
        self.not_proper_1_att_chk.place(x=50, y=120)
        self.air_2_air_btn.place(x=50, y=270)
        self.clear_all_air_btn.place(x=120, y=270)
        self.d10_att_1_ent.place(x=150, y=330)
        self.DRM_att_1_ent.place(x=150, y=300)
        self.result_att_1_ent.place(x=150, y=360)
        self.d10_def_1_ent.place(x=360, y=330)
        self.DRM_def_1_ent.place(x=360, y=300)
        self.result_def_1_ent.place(x=360, y=360)
        self.not_mutual_chk_2_att.place(x=150, y=210)
        self.attacker_1_d10_lbl.place(x=50, y=330)
        self.attacker_1_drm_lbl.place(x=50, y=300)
        self.attacker_1_result_lbl.place(x=50, y=360)
        self.defender_1_d10_lbl.place(x=260, y=330)
        self.defender_1_drm_lbl.place(x=260, y=300)
        self.defender_1_result_lbl.place(x=260, y=360)
        
        self.attacker_2_drm_lbl.place(x=50, y=400)
        self.attacker_2_d10_lbl.place(x=50, y=430)
        self.attacker_2_result_lbl.place(x=50, y=460)
        
        self.defender_2_drm_lbl.place(x=260, y=400)
        self.defender_2_d10_lbl.place(x=260, y=430)
        self.defender_2_result_lbl.place(x=260, y=460)
        
        self.d10_att_2_ent.place(x=150, y=430)
        self.DRM_att_2_ent.place(x=150, y=400)
        self.result_att_2_ent.place(x=150, y=460)
        
        self.d10_def_2_ent.place(x=360, y=430)
        self.DRM_def_2_ent.place(x=360, y=400)
        self.result_def_2_ent.place(x=360, y=460)
        
        self.defender_2_value_cbx.config(state='disabled')
        self.defender_2_pilot_skills_cbx.config(state='disabled')
        self.strike_2_def_chk.config(state='disabled')
        self.not_proper_2_def_chk.config(state='disabled')
        self.not_mutual_chk_2_def.config(state='disabled')
        self.d10_def_2_ent.config(state='disabled')
        self.DRM_def_2_ent.config(state='disabled')
        self.result_def_2_ent.config(state='disabled')
        
        self.attacker_2_value_cbx.config(state='disabled')
        self.attacker_2_pilot_skills_cbx.config(state='disabled')
        self.strike_2_att_chk.config(state='disabled')
        self.not_proper_2_att_chk.config(state='disabled')
        self.not_mutual_chk_2_att.config(state='disabled')
        self.d10_att_2_ent.config(state='disabled')
        self.DRM_att_2_ent.config(state='disabled')
        self.result_att_2_ent.config(state='disabled')


    def skill_active(self, actual_distance):
        actual_distance = actual_distance.get()
        if actual_distance == 3:
            self.attacker_1_pilot_skills_cbx.config(state='normal')
            self.attacker_2_pilot_skills_cbx.config(state='normal')
            self.defender_1_pilot_skills_cbx.config(state='normal')
        else:
            self.attacker_1_pilot_skills_cbx.config(state='disabled')
            self.attacker_2_pilot_skills_cbx.config(state='disabled')
            self.defender_1_pilot_skills_cbx.config(state='disabled')
        if actual_distance == 2:
            self.not_proper_1_att_chk.config(state='normal')
            self.not_proper_2_att_chk.config(state='normal')
            self.not_proper_1_def_chk.config(state='normal')
        else:
            self.not_proper_1_att_chk.config(state='disabled')
            self.not_proper_2_att_chk.config(state='disabled')
            self.not_proper_1_def_chk.config(state='disabled')
            
    def combat_active(self, engagement):
        engagement = engagement.get()
        if engagement == 1:
            self.defender_2_value_cbx.config(state='disabled')
            self.defender_2_pilot_skills_cbx.config(state='disabled')
            self.strike_2_def_chk.config(state='disabled')
            self.not_proper_2_def_chk.config(state='disabled')
            self.not_mutual_chk_2_def.config(state='disabled')
            self.d10_def_2_ent.config(state='disabled')
            self.DRM_def_2_ent.config(state='disabled')
            self.result_def_2_ent.config(state='disabled')
            
            self.attacker_2_value_cbx.config(state='disabled')
            self.attacker_2_pilot_skills_cbx.config(state='disabled')
            self.strike_2_att_chk.config(state='disabled')
            self.not_proper_2_att_chk.config(state='disabled')
            self.not_mutual_chk_2_att.config(state='disabled')
            self.d10_att_2_ent.config(state='disabled')
            self.DRM_att_2_ent.config(state='disabled')
            self.result_att_2_ent.config(state='disabled')
            
        if engagement == 2:
            self.defender_2_value_cbx.config(state='disabled')
            self.defender_2_pilot_skills_cbx.config(state='disabled')
            self.strike_2_def_chk.config(state='disabled')
            self.not_proper_2_def_chk.config(state='disabled')
            self.not_mutual_chk_2_def.config(state='disabled')
            self.d10_def_2_ent.config(state='disabled')
            self.DRM_def_2_ent.config(state='disabled')
            self.result_def_2_ent.config(state='disabled')
            
            self.attacker_2_value_cbx.config(state='normal')
            self.attacker_2_pilot_skills_cbx.config(state='normal')
            self.strike_2_att_chk.config(state='normal')
            self.not_proper_2_att_chk.config(state='normal')
            self.not_mutual_chk_2_att.config(state='normal')
            self.d10_att_2_ent.config(state='normal')
            self.DRM_att_2_ent.config(state='normal')
            self.result_att_2_ent.config(state='normal')
            
        if engagement == 3:
            self.attacker_2_value_cbx.config(state='disabled')
            self.attacker_2_pilot_skills_cbx.config(state='disabled')
            self.strike_2_att_chk.config(state='disabled')
            self.not_proper_2_att_chk.config(state='disabled')
            self.not_mutual_chk_2_att.config(state='disabled')
            self.d10_att_2_ent.config(state='disabled')
            self.DRM_att_2_ent.config(state='disabled')
            self.result_att_2_ent.config(state='disabled')
            
            self.defender_2_value_cbx.config(state='normal')
            self.defender_2_pilot_skills_cbx.config(state='normal')
            self.strike_2_def_chk.config(state='normal')
            self.not_proper_2_def_chk.config(state='normal')
            self.not_mutual_chk_2_def.config(state='normal')
            self.d10_def_2_ent.config(state='normal')
            self.DRM_def_2_ent.config(state='normal')
            self.result_def_2_ent.config(state='normal')
            

    def calculate_a2a(self):

        self.d10_att_1_ent.delete(0, 'end')
        self.DRM_att_1_ent.delete(0, 'end')
        self.result_att_1_ent.delete(0, 'end')
        
        self.d10_def_1_ent.delete(0, 'end')
        self.DRM_def_1_ent.delete(0, 'end')
        self.result_def_1_ent.delete(0, 'end')
        
        self.d10_att_2_ent.delete(0, 'end')
        self.DRM_att_2_ent.delete(0, 'end')
        self.result_att_2_ent.delete(0, 'end')
        
        self.d10_def_2_ent.delete(0, 'end')
        self.DRM_def_2_ent.delete(0, 'end')
        self.result_def_2_ent.delete(0, 'end')
        

        if self.defender_1_value_cbx.get() == '#':
            target_att = 0
        else:
            target_att = int(self.defender_1_value_cbx.get())
            
        if not self.not_mutual_1_att.get():
            fire_1 = int(self.attacker_1_value_cbx.get())
            diff_att_1 = fire_1 - target_att
            if diff_att_1 > 4:
                diff_att_1 = 4
            if diff_att_1 < -4:
                diff_att_1 = -4
            column_att_1 = -diff_att_1 + 4
    
            d10_att_1 = randint(0, 9)
            DRM_att_1 = 0
            if self.actual_weather.get() == 3:
                DRM_att_1 += 3
            if self.strike_1_att.get():
                DRM_att_1 += 2
            if target_att == 0 and self.actual_distance.get() == 2:
                DRM_att_1 -= 1
            if self.not_proper_1_att.get() and self.actual_distance.get() == 2:
                DRM_att_1 += 1
            if self.actual_distance.get() == 3:
                skill_att_1 = int(self.attacker_1_pilot_skills_cbx.get())
                DRM_att_1 += skill_att_1
            if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
                DRM_att_1 += 1
    
            row_att_1 = d10_att_1 + DRM_att_1
            if row_att_1 > 10:
                row_att_1 = 10
            if row_att_1 < -2:
                row_att_1 = -2
            row_att_1 += 2
    
            if self.actual_distance.get() == 3:
                result_att_1 = AIR_COMBAT_RESULT_DOGFIGHT[column_att_1][row_att_1]
            else:
                result_att_1 = AIR_COMBAT_RESULT_LONG[column_att_1][row_att_1]
        else:
            d10_att_1 = '-'
            DRM_att_1 = '-'
            result_att_1 = '-'
            
        if not self.not_mutual_2_att.get() and self.engagement.get() == 2:
            
            fire_2 = int(self.attacker_2_value_cbx.get())
            diff_att_2 = fire_2 - target_att
            if diff_att_2 > 4:
                diff_att_2 = 4
            if diff_att_2 < -4:
                diff_att_2 = -4
            column_att_2 = -diff_att_2 + 4
            
            d10_att_2 = randint(0, 9)
            DRM_att_2 = 0
            if self.actual_weather.get() == 3:
                DRM_att_2 += 3
            if self.strike_2_att.get():
                DRM_att_2 += 2
            if target_att == 0 and self.actual_distance.get() == 2:
                DRM_att_2 -= 1
            if self.not_proper_1_att.get() and self.actual_distance.get() == 2:
                DRM_att_2 += 1
            if self.actual_distance.get() == 3:
                skill_att_2 = int(self.attacker_2_pilot_skills_cbx.get())
                DRM_att_2 += skill_att_2
            if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
                DRM_att_2 += 1
    
            row_att_2 = d10_att_2 + DRM_att_2
            if row_att_2 > 10:
                row_att_2 = 10
            if row_att_2 < -2:
                row_att_2 = -2
            row_att_1 += 2
    
            if self.actual_distance.get() == 3:
                result_att_2 = AIR_COMBAT_RESULT_DOGFIGHT[column_att_2][row_att_2]
            else:
                result_att_2 = AIR_COMBAT_RESULT_LONG[column_att_2][row_att_2]
        else:
            d10_att_2 = '-'
            DRM_att_2 = '-'
            result_att_2 = '-'
            
        vs_bomber = target_att == 0
        
        target_def = int(self.attacker_1_value_cbx.get())
        
        if not self.not_mutual_1_def.get() and not vs_bomber:
            
            fire_1 = int(self.defender_1_value_cbx.get())
            diff_def_1 = fire_1 - target_def

            if diff_def_1 > 4:
                diff_def_1 = 4
            if diff_def_1 < -4:
                diff_def_1 = -4
            column_def_1 = -diff_def_1 + 4

            d10_def_1 = randint(0, 9)
            DRM_def_1 = 0

            if self.actual_weather.get() == 3:
                DRM_def_1 += 3
            if self.strike_1_def.get():
                DRM_def_1 += 2
            if target_def == 0 and self.actual_distance.get() == 2:
                DRM_def_1 -= 1
            if self.not_proper_1_def.get() and self.actual_distance.get() == 2:
                DRM_def_1 += 1
            if self.actual_distance.get() == 3:
                skill_def_1 = int(self.defender_1_pilot_skills_cbx.get())
                DRM_def_1 += skill_def_1
            if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
                DRM_def_1 += 1

            row_def_1 = d10_def_1 + DRM_def_1
            if row_def_1 > 10:
                row_def_1 = 10
            if row_def_1 < -2:
                row_def_1 = -2
            row_def_1 += 2

            if self.actual_distance.get() == 3:
                result_def_1 = AIR_COMBAT_RESULT_DOGFIGHT[column_def_1][row_def_1]
            else:
                result_def_1 = AIR_COMBAT_RESULT_LONG[column_def_1][row_def_1]
        else:
            d10_def_1 = '-'
            DRM_def_1 = '-'
            result_def_1 = '-'
            
        if not self.not_mutual_2_def.get() and self.engagement.get() == 3:
            
            

            fire_2 = int(self.defender_2_value_cbx.get())
                
            diff_def_2 = fire_2 - target_def

            if diff_def_2 > 4:
                diff_def_2 = 4
            if diff_def_2 < -4:
                diff_def_2 = -4
            column_def_2 = -diff_def_2 + 4

            d10_def_2 = randint(0, 9)
            DRM_def_2 = 0

            if self.actual_weather.get() == 3:
                DRM_def_2 += 3
            if self.strike_1_def.get():
                DRM_def_2 += 2
            if target_def == 0 and self.actual_distance.get() == 2:
                DRM_def_2 -= 1
            if self.not_proper_2_def.get() and self.actual_distance.get() == 2:
                DRM_def_2 += 1
            if self.actual_distance.get() == 3:
                skill_def_2 = int(self.defender_2_pilot_skills_cbx.get())
                DRM_def_2 += skill_def_2
            if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
                DRM_def_2 += 1

            row_def_2 = d10_def_2 + DRM_def_2
            if row_def_2 > 10:
                row_def_2 = 10
            if row_def_2 < -2:
                row_def_2 = -2
            row_def_2 += 2

            if self.actual_distance.get() == 3:
                result_def_2 = AIR_COMBAT_RESULT_DOGFIGHT[column_def_2][row_def_2]
            else:
                result_def_2 = AIR_COMBAT_RESULT_LONG[column_def_2][row_def_2]
        else:
            d10_def_2 = '-'
            DRM_def_2 = '-'
            result_def_2 = '-'

        self.result_att_1_ent.insert(END, result_att_1)
        self.DRM_att_1_ent.insert(END, str(DRM_att_1))
        self.d10_att_1_ent.insert(END, str(d10_att_1))
        
        self.result_att_2_ent.insert(END, result_att_2)
        self.DRM_att_2_ent.insert(END, str(DRM_att_2))
        self.d10_att_2_ent.insert(END, str(d10_att_2))
        
        self.d10_def_1_ent.insert(END, str(d10_def_1))
        self.DRM_def_1_ent.insert(END, str(DRM_def_1))
        self.result_def_1_ent.insert(END, str(result_def_1))
        
        self.d10_def_2_ent.insert(END, str(d10_def_2))
        self.DRM_def_2_ent.insert(END, str(DRM_def_2))
        self.result_def_2_ent.insert(END, str(result_def_2))
        
    def clear_all_air(self):
        
        self.d10_att_2_ent.config(state='normal')
        self.DRM_att_2_ent.config(state='normal')
        self.result_att_2_ent.config(state='normal')
        
        self.d10_def_2_ent.config(state='normal')
        self.DRM_def_2_ent.config(state='normal')
        self.result_def_2_ent.config(state='normal')

        self.not_proper_1_att.set(False)
        self.strike_1_att.set(False)
        self.not_proper_1_att.set(False)
        self.strike_1_att.set(False)
        self.not_mutual_1_att.set(False)
        self.attacker_1_value_cbx.set('')
        self.attacker_1_pilot_skills_cbx.set('')
        
        self.not_proper_2_att.set(False)
        self.strike_2_att.set(False)
        self.not_proper_2_att.set(False)
        self.strike_2_att.set(False)
        self.not_mutual_2_att.set(False)
        self.attacker_2_value_cbx.set('')
        self.attacker_2_pilot_skills_cbx.set('')


        self.not_proper_1_def.set(False)
        self.strike_1_def.set(False)
        self.not_proper_1_def.set(False)
        self.strike_1_def.set(False)
        self.not_mutual_1_def.set(False)
        self.defender_1_value_cbx.set('')
        self.defender_1_pilot_skills_cbx.set('')


        self.not_proper_2_def.set(False)
        self.strike_2_def.set(False)
        self.not_proper_2_def.set(False)
        self.strike_2_def.set(False)
        self.not_mutual_2_def.set(False)
        self.defender_2_value_cbx.set('')
        self.defender_2_pilot_skills_cbx.set('')
        
        self.d10_att_1_ent.delete(0, 'end')
        self.DRM_att_1_ent.delete(0, 'end')
        self.result_att_1_ent.delete(0, 'end')
        
        self.d10_def_1_ent.delete(0, 'end')
        self.DRM_def_1_ent.delete(0, 'end')
        self.result_def_1_ent.delete(0, 'end')
        
        self.d10_att_2_ent.delete(0, 'end')
        self.DRM_att_2_ent.delete(0, 'end')
        self.result_att_2_ent.delete(0, 'end')
        
        self.d10_def_2_ent.delete(0, 'end')
        self.DRM_def_2_ent.delete(0, 'end')
        self.result_def_2_ent.delete(0, 'end')

