from tkinter import Label, IntVar, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import Tk
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint
# from functools import partial


class StrikeTable:

    def __init__(self, win):

        self.attacker_type_lbl = Label(win, text='Attacker type:')
        attacker_types = ('Air Strike', 'Sup_HQ', 'US_HQ', 'other_HQ', 'Artillery',
                          'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel')
        self.attacker_type_cbx = Combobox(win, values=attacker_types, width=10)
        self.attacker_type_cbx.set('Air Strike')

        self.air_strike_value_lbl = Label(win, text='Air Strike Value:')
        self.air_strike_value_cbx = Combobox(win, values=('1', '2', '3', '4', '5', '6'), width=5)
        self.air_strike_value_cbx.set('1')
        self.target_type_lbl = Label(win, text='Target type:')

        target_types = ('Marsh/Flat', 'Rough/Rough Woods/Flat Woods', 'Highland/Highland Woods', 'Mountain',
                        'Urban', 'Air Defense Track', 'Hardened Target')
        self.target_type_cbx = Combobox(win, values=target_types, width=30)
        self.target_type_cbx.set('Marsh/Flat')

        self.target_over_stacked = BooleanVar()
        self.target_over_stacked.set(False)
        self.target_over_stacked_chk = Checkbutton(win, text='Target hex overstacked',
                                                   variable=self.target_over_stacked)
        self.high_mountain = BooleanVar()
        self.high_mountain.set(False)
        self.high_mountain_chk = Checkbutton(win, text='Target in high mountain', variable=self.high_mountain)

        self.russian_rocket = BooleanVar()
        self.russian_rocket.set(False)
        self.russian_rocket_chk = Checkbutton(win, text='Russian rocket artillery', variable=self.russian_rocket)

        self.ah_1_ww = BooleanVar()
        self.ah_1_ww.set(False)
        self.ah_1_chk = Checkbutton(win, text='AH-1Z Wild Weasel strike', variable=self.ah_1_ww)

        self.non_us_cruise = BooleanVar()
        self.non_us_cruise.set(False)
        self.non_us_cruise_chk = Checkbutton(win, text='non-US cruise strike', variable=self.non_us_cruise)

        self.hq_reduced = BooleanVar()
        self.hq_reduced.set(False)
        self.hq_reduced_chk = Checkbutton(win, text='HQ reduced strength', variable=self.hq_reduced)

        self.unit_city_fort_jungle = BooleanVar()
        self.unit_city_fort_jungle.set(False)
        self.unit_city_fort_jungle_chk = Checkbutton(win, text='Unit in city/fort/jungle',
                                                     variable=self.unit_city_fort_jungle)
        self.bridge_or_beachhead = BooleanVar()
        self.bridge_or_beachhead.set(False)
        self.bridge_or_beachhead_chk = Checkbutton(win, text='vs bridge or beachhead',
                                                   variable=self.bridge_or_beachhead)

        self.interceptor_vs_unit = BooleanVar()
        self.interceptor_vs_unit.set(False)
        self.interceptor_vs_unit_chk = Checkbutton(win, text='unit attacked by interceptor',
                                                   variable=self.interceptor_vs_unit)
        self.theater_busting = BooleanVar()
        self.theater_busting.set(False)
        self.theater_busting_chk = Checkbutton(win, text='theater weapon busting', variable=self.theater_busting)

        self.vs_enemy_aaa = BooleanVar()
        self.vs_enemy_aaa.set(False)
        self.vs_enemy_aaa_chk = Checkbutton(win, text='vs enemy AAA', variable=self.vs_enemy_aaa)

        self.stand_off_vs_leg = BooleanVar()
        self.stand_off_vs_leg.set(False)
        self.stand_off_vs_leg_chk = Checkbutton(win, text='stand off vs leg unit', variable=self.stand_off_vs_leg)

        self.targeted_value_cbx = Combobox(win, values=('0', '-1', '-2'), width=5)
        self.targeted_value_cbx.set('0')

        self.pilot_skills_lbl = Label(win, text='Pilot skills:')
        self.pilot_skills_cbx = Combobox(win, values=('-2', '-1', '0', '1', '2'), width=5)
        self.pilot_skills_cbx.set('0')

        self.aa_result_lbl = Label(win, text='AA result:')
        self.aa_result_cbx = Combobox(win, values=('0', '1', '2', '3', '4'), width=5)
        self.aa_result_cbx.set('0')

        self.actual_weather = IntVar()
        self.actual_weather.set(1)
        self.clear_weather_rb = Radiobutton(win, text="Clear", variable=self.actual_weather, value=1)
        self.overcast_weather_rb = Radiobutton(win, text="Overcast", variable=self.actual_weather, value=2)
        self.storm_weather_rb = Radiobutton(win, text="Storm", variable=self.actual_weather, value=3)

        self.strike_btn = Button(win, text='Strike!', command=self.calculate_strike)

        self.strike_d10_lbl = Label(win, text='d10:')
        self.strike_d10_ent = Entry(width=10)

        self.strike_drm_lbl = Label(win, text='Strike DRM:')
        self.strike_drm_ent = Entry(width=10)

        self.strike_result_lbl = Label(win, text='Strike Result:')
        self.strike_result_ent = Entry(width=10)

        self.hardened = BooleanVar()
        self.hardened.set(False)
        self.hardened_chk = Checkbutton(win, text='Hardened Target', variable=self.hardened)

        self.nuclear = BooleanVar()
        self.nuclear.set(False)
        self.nuclear_chk = Checkbutton(win, text='Destroyed by Nuclear', variable=self.nuclear)

        self.site_type_cbx = Combobox(win, values=('Airfield', 'Airbase', 'Helos'), width=8)
        self.site_type_cbx.set('Airfield')

        self.destroy_type_cbx = Combobox(win, values=('Strike 1', 'Strike 2', 'X'), width=8)
        self.destroy_type_cbx.set('Strike 1')

        self.damage_btn = Button(win, text='Damage', command=self.calculate_damage)

        self.collateral_damage_ent = Entry(width=12)
        self.d10_coll_ent = Entry(width=10)

        self.attacker_type_lbl.place(x=50, y=40)
        self.attacker_type_cbx.place(x=150, y=40)
        self.air_strike_value_lbl.place(x=250, y=40)
        self.air_strike_value_cbx.place(x=350, y=40)
        self.target_type_lbl.place(x=50, y=80)
        self.target_type_cbx.place(x=150, y=80)

        self.target_over_stacked_chk.place(x=50, y=120)
        self.high_mountain_chk.place(x=50, y=160)
        self.ah_1_chk.place(x=50, y=200)
        self.non_us_cruise_chk.place(x=50, y=240)
        self.hq_reduced_chk.place(x=50, y=280)
        self.unit_city_fort_jungle_chk.place(x=50, y=320)
        self.bridge_or_beachhead_chk.place(x=50, y=360)
        self.vs_enemy_aaa_chk.place(x=50, y=400)
        self.stand_off_vs_leg_chk.place(x=50, y=440)

        self.clear_weather_rb.place(x=250, y=120)
        self.overcast_weather_rb.place(x=250, y=160)
        self.storm_weather_rb.place(x=250, y=200)

        self.strike_btn.place(x=250, y=240)
        self.strike_d10_ent.place(x=350, y=280)
        self.strike_d10_lbl.place(x=250, y=280)
        self.strike_drm_ent.place(x=350, y=320)
        self.strike_drm_lbl.place(x=250, y=320)
        self.strike_result_ent.place(x=350, y=360)
        self.strike_result_lbl.place(x=250, y=360)

        self.aa_result_lbl.place(x=350, y=120)
        self.aa_result_cbx.place(x=450, y=120)
        self.pilot_skills_lbl.place(x=350, y=160)
        self.pilot_skills_cbx.place(x=450, y=160)

        self.damage_btn.place(x=250, y=400)
        self.site_type_cbx.place(x=350, y=400)
        self.destroy_type_cbx.place(x=350, y=440)
        self.hardened_chk.place(x=350, y=480)
        self.nuclear_chk.place(x=350, y=520)
        self.d10_coll_ent.place(x=250, y=440)
        self.collateral_damage_ent.place(x=250, y=480)

    def calculate_strike(self):

        self.strike_result_ent.delete(0, 'end')
        self.strike_d10_ent.delete(0, 'end')
        self.strike_drm_ent.delete(0, 'end')

        air_strike_target_1 = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 0,
                               'Rough/Rough Woods/Flat Woods': 1, 'Marsh/Flat': 2, 'Hardened Target': 9,
                               'Air Defense Track': 9}
        air_strike_target_2 = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1,
                               'Rough/Rough Woods/Flat Woods': 2, 'Marsh/Flat': 3,
                               'Hardened Target': 0, 'Air Defense Track': 0}
        air_strike_target_3 = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2,
                               'Rough/Rough Woods/Flat Woods': 3, 'Marsh/Flat': 4, 'Hardened Target': 1,
                               'Air Defense Track': 1}
        air_strike_target_4 = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3,
                               'Rough/Rough Woods/Flat Woods': 4, 'Marsh/Flat': 5, 'Hardened Target': 2,
                               'Air Defense Track': 2}
        air_strike_target_5 = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 4,
                               'Rough/Rough Woods/Flat Woods': 5, 'Marsh/Flat': 6, 'Hardened Target': 3,
                               'Air Defense Track': 3}
        air_strike_target_6 = {'Urban': 5, 'Mountain': 5, 'Highland/Highland Woods': 5,
                               'Rough/Rough Woods/Flat Woods': 6, 'Marsh/Flat': 6, 'Hardened Target': 4,
                               'Air Defense Track': 3}
        sup_hq_target = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                         'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
        us_hq_target = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                        'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
        other_hq_target = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                           'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
        artillery_target = {'Urban': 1, 'Mountain': 1, 'Highland/Highland Woods': 2, 'Rough/Rough Woods/Flat Woods': 3,
                            'Marsh/Flat': 4, 'Hardened Target': 9, 'Air Defense Track': 9}
        helo_2_target = {'Urban': 2, 'Mountain': 2, 'Highland/Highland Woods': 3, 'Rough/Rough Woods/Flat Woods': 4,
                         'Marsh/Flat': 5, 'Hardened Target': 9, 'Air Defense Track': 9}
        helo_1_target = {'Urban': 0, 'Mountain': 0, 'Highland/Highland Woods': 1, 'Rough/Rough Woods/Flat Woods': 2,
                         'Marsh/Flat': 3, 'Hardened Target': 9, 'Air Defense Track': 9}
        scud_target = {'Urban': 3, 'Mountain': 3, 'Highland/Highland Woods': 7, 'Rough/Rough Woods/Flat Woods': 7,
                       'Marsh/Flat': 7, 'Hardened Target': 2, 'Air Defense Track': 9}
        cruise_target = {'Urban': 4, 'Mountain': 4, 'Highland/Highland Woods': 8, 'Rough/Rough Woods/Flat Woods': 8,
                         'Marsh/Flat': 8, 'Hardened Target': 3, 'Air Defense Track': 2}
        wild_weasel_target = {'Urban': 9, 'Mountain': 9, 'Highland/Highland Woods': 9,
                              'Rough/Rough Woods/Flat Woods': 9, 'Marsh/Flat': 9, 'Hardened Target': 9,
                              'Air Defense Track': 4}
        strike_table_no_air = {'Sup_HQ': sup_hq_target, 'US_HQ': us_hq_target,
                               'other_HQ': other_hq_target, 'Artillery': artillery_target, 'Helo 1': helo_1_target,
                               'Helo 2': helo_2_target, 'SCUD': scud_target, 'Cruise': cruise_target,
                               'Wild Weasel': wild_weasel_target}
        strike_table_air_only = {'1': air_strike_target_1, '2': air_strike_target_2, '3': air_strike_target_3,
                                 '4': air_strike_target_4, '5': air_strike_target_5, '6': air_strike_target_6}

        if self.attacker_type_cbx.get() != 'Air Strike':
            target = strike_table_no_air[self.attacker_type_cbx.get()]
            column = target[self.target_type_cbx.get()]
        else:
            target = strike_table_air_only[self.air_strike_value_cbx.get()]
            column = target[self.target_type_cbx.get()]

        d10_strike = randint(0, 9)
        drm_strike = 0
        if self.target_over_stacked.get():
            drm_strike -= 2
        if self.high_mountain.get():
            drm_strike -= 2
        if self.russian_rocket.get():
            drm_strike -= 1
        if self.ah_1_ww.get():
            drm_strike += 1
        if self.non_us_cruise.get():
            drm_strike += 1
        if self.hq_reduced.get():
            drm_strike += 1
        if self.unit_city_fort_jungle.get():
            drm_strike += 1
        if self.bridge_or_beachhead.get():
            drm_strike += 2
        if self.interceptor_vs_unit.get():
            drm_strike += 2
        if self.theater_busting.get():
            drm_strike += 2
        if self.vs_enemy_aaa.get():
            drm_strike += 3
        if self.stand_off_vs_leg.get():
            drm_strike += 3
        drm_strike += int(self.aa_result_cbx.get())
        drm_strike += int(self.pilot_skills_cbx.get())
        if self.actual_weather == 3:
            drm_strike += 3
        air_attacker = ['Air Strike', 'Helo 1', 'Helo 2', 'SCUD', 'Cruise', 'Wild Weasel']
        if self.actual_weather == 2 and self.attacker_type_cbx.get() in air_attacker:
            drm_strike += 2
        row = d10_strike + drm_strike
        if row < -2:
            row = -2
        if row > 7:
            row = 7

        advanced_strike_table = [['Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', '-', '-', '-', '-', '-', '-'],
                                 ['Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                                  '-', '-', '-', '-'],
                                 ['Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                                  '-', '-', '-'],
                                 ['Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                                  'Strike 1', '-', '-'],
                                 ['X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', 'Strike 1',
                                  'Strike 1', '-'],
                                 ['X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1',
                                  'Strike 1', '-'],
                                 ['X', 'X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-'],
                                 ['X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-', '-'],
                                 ['X', 'X', 'X', 'X', 'Strike 2', 'Strike 2', 'Strike 1', 'Strike 1', 'Strike 1', '-'],
                                 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

        advanced_strike_table_vs_aa = [['-1', '-1', '-1', '-1', '-', '-', '-', '-', '-', '-'],
                                       ['-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-', '-'],
                                       ['-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
                                       ['-2', '-2', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-'],
                                       ['-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-1', '-'],
                                       ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-1', '-'],
                                       ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                                       ['-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-', '-'],
                                       ['-3', '-3', '-3', '-3', '-2', '-2', '-1', '-1', '-1', '-'],
                                       ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

        if self.target_type_cbx.get() != 'Air Defense Track':
            result = advanced_strike_table[column][row]
        else:
            result = advanced_strike_table_vs_aa[column][row]

        self.strike_result_ent.insert(END, result)
        self.strike_d10_ent.insert(END, str(d10_strike))
        self.strike_drm_ent.insert(END, str(drm_strike))

    def calculate_damage(self):

        self.collateral_damage_ent.delete(0, 'end')
        self.d10_coll_ent.delete(0, 'end')

        side_type_to_column = {'Airfield': [0, 1, 2], 'Airbase': [3, 4, 5], 'Helos': [6, 7, 8]}
        destroy_to_column = {'Strike 1': 0, 'Strike 2': 1, 'X': 2}
        side = side_type_to_column[self.site_type_cbx.get()]
        destroy = destroy_to_column[self.destroy_type_cbx.get()]
        column = side[destroy]

        d10_coll = randint(0, 9)
        drm_coll = 0

        if self.hardened.get():
            drm_coll += 1
        if self.nuclear.get():
            drm_coll -= 2

        row = drm_coll + d10_coll
        if row < 0:
            row = 0
        if row > 7:
            row = 7

        collateral_damage_table = [['Air', 'AmPt', '-', '-', '-', '-', '-', '-'],
                                   ['Air*', 'Air', 'AmPt', '-', '-', '-', '-', '-'],
                                   ['Air*', 'Air*', 'Air', 'AmPt', '-', '-', '-', '-'],
                                   ['Air AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-', '-'],
                                   ['Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', '-', '-', '-'],
                                   ['Air* Air AmPt', 'Air* Air AmPt', 'Air* AmPt', 'Air AmPt', 'Air', 'Air', 'Air',
                                    '-'],
                                   ['Step', 'Step', '-', '-', '-', '-', '-', '-'],
                                   ['Elim', 'Step', 'Step', '-', '-', '-', '-', '-'],
                                   ['Elim', 'Elim', 'Step', 'Step', '-', '-', '-', '-']]

        result = collateral_damage_table[column][row]
        self.d10_coll_ent.insert(END, str(d10_coll))
        self.collateral_damage_ent.insert(END, result)


window = Tk()
mywin = StrikeTable(window)
window.title('Advanced Air Warfare Calculator')
window.geometry("600x600+10+10")
window.mainloop()
