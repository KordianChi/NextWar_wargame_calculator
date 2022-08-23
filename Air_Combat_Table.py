from tkinter import Label, IntVar, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import Tk
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint
from functools import partial


class MyWindow:
    def __init__(self, win):
        self.lbl0 = Label(win, text='Attacker:')
        self.cb0 = Combobox(win, values=('1', '2', '3', '4', '5', '6'), width=5)
        self.cb0.set('1')
        self.lbl2 = Label(win, text='Defender:')
        self.cb2 = Combobox(win, values=('#', '0', '1', '2', '3', '4', '5', '6'), width=5)
        self.cb2.set('1')
        self.lbl3 = Label(win, text='Distance:')
        self.lbl4 = Label(win, text='Weather:')
        self.lbl5 = Label(win, text='DRMs:')
        self.lbl6 = Label(win, text='dice d10:')
        self.lbl7 = Label(win, text='DRMs:')
        self.lbl8 = Label(win, text='Att - Def:')
        self.lbl9 = Label(win, text='Result:')
        self.lbl27 = Label(win, text='dice d10:')
        self.lbl28 = Label(win, text='DRMs:')
        self.lbl29 = Label(win, text='Result:')
        self.lbl10 = Label(win, text='Detection:')
        self.cb3 = Combobox(win, values=('Local', '0-1', '2-3', '4', '5', '6', '7', '8', '9', '10'), width=5)
        self.cb3.set('Local')
        self.lbl11 = Label(win, text='AWACS adv:')
        self.cb4 = Combobox(win, values=('0-1', '2', '3', '4'), width=5)
        self.cb4.set('0-1')
        self.lbl12 = Label(win, text='Wild Weasel:')
        self.cb5 = Combobox(win, values=('0', '1', '2'), width=5)
        self.cb5.set('0')
        self.lbl13 = Label(win, text='DRMs:')
        self.lbl14 = Label(win, text='dice d10:')
        self.lbl15 = Label(win, text='Result:')
        self.lbl16 = Label(win, text='SAM value:')
        self.cb6 = Combobox(win, values=('Local', '0-1', '2', '3-4', '5-6', '7', '8', '9', '10'), width=5)
        self.cb6.set('Local')
        self.lbl18 = Label(win, text='DRMs:')
        self.lbl19 = Label(win, text='dice d10:')
        self.lbl20 = Label(win, text='Result:')
        self.lbl21 = Label(win, text='AAA value:')
        self.cb8 = Combobox(win, values=('Local', '0-1', '2', '3'), width=5)
        self.cb8.set('Local')
        self.lbl22 = Label(win, text='DRMs:')
        self.lbl23 = Label(win, text='dice d10:')
        self.lbl24 = Label(win, text='Result:')

        self.btn1 = Button(win, text='Calculate', command=self.calculate_a2a)
        self.btn2 = Button(win, text='Calculate', command=self.calculate_detection)
        self.btn3 = Button(win, text='Calculate', command=self.sam_defence)
        self.btn4 = Button(win, text='Calculate', command=self.aaa_defence)

        self.t1 = Entry(width=10)
        self.t2 = Entry(width=10)
        self.t3 = Entry(width=10)
        self.t4 = Entry(width=10)
        self.t6 = Entry(width=10)
        self.t7 = Entry(width=10)
        self.t8 = Entry(width=10)
        self.t9 = Entry(width=10)
        self.t10 = Entry(width=10)
        self.t11 = Entry(width=10)
        self.t12 = Entry(width=10)
        self.t13 = Entry(width=10)
        self.t14 = Entry(width=10)
        self.t15 = Entry(width=10)
        self.t16 = Entry(width=10)
        self.t17 = Entry(width=10)

        self.strike = IntVar()
        self.strike.set(0)
        self.not_proper = IntVar()
        self.not_proper.set(0)
        self.vs_bomber = IntVar()
        self.vs_bomber.set(0)

        self.strike_def = IntVar()
        self.strike.set(0)
        self.not_proper_def = IntVar()
        self.not_proper_def.set(0)

        self.actual_weather = IntVar()
        self.actual_weather.set(1)
        self.actual_distance = IntVar()
        self.actual_distance.set(1)

        self.not_mutual = BooleanVar()
        self.not_mutual.set(False)
        self.c25 = Checkbutton(win, text='not mutual firing', variable=self.not_mutual)

        self.cb1 = Combobox(win, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        self.cb1.set('0')
        self.cb9 = Combobox(win, values=('-2', '-1', '0', '1', '2'), width=5, state='disabled')
        self.cb9.set('0')
        self.lbl25 = Label(win, text='Pilot skills')

        self.r1 = Radiobutton(win, text="Long Range", variable=self.actual_distance,
                              value=1, command=partial(self.skill_active, self.actual_distance))
        self.r2 = Radiobutton(win, text="Stand-off", variable=self.actual_distance,
                              value=2, command=partial(self.skill_active, self.actual_distance))
        self.r3 = Radiobutton(win, text="Dogfight", variable=self.actual_distance,
                              value=3, command=partial(self.skill_active, self.actual_distance))

        self.r4 = Radiobutton(win, text="Clear", variable=self.actual_weather, value=1)
        self.r5 = Radiobutton(win, text="Overcast", variable=self.actual_weather, value=2)
        self.r6 = Radiobutton(win, text="Storm", variable=self.actual_weather, value=3)
        self.c2 = Checkbutton(win, text='CS firing', variable=self.strike)
        self.c3 = Checkbutton(win, text='not NATO/US/JPN/PRC', variable=self.not_proper, state='disabled')
        self.c5 = Checkbutton(win, text='vs Bomber', variable=self.vs_bomber, state='disabled')
        self.c23 = Checkbutton(win, text='CS firing', variable=self.strike_def)
        self.c24 = Checkbutton(win, text='not NATO/US/JPN/PRC', variable=self.not_proper_def, state='disabled')

        self.near_HQ = BooleanVar()
        self.near_HQ.set(False)
        self.c6 = Checkbutton(win, text='Target near HQ', variable=self.near_HQ)

        self.passed_occ = BooleanVar()
        self.passed_occ.set(False)
        self.c7 = Checkbutton(win, text='Passed through occupied hex', variable=self.passed_occ)

        self.vs_helos = BooleanVar()
        self.vs_helos.set(False)
        self.c8 = Checkbutton(win, text='vs Attack Helos', variable=self.vs_helos)

        self.EZOC_landing = BooleanVar()
        self.EZOC_landing.set(False)
        self.c9 = Checkbutton(win, text='Landing in EZOC', variable=self.EZOC_landing)

        self.vs_para = BooleanVar()
        self.vs_para.set(False)
        self.c10 = Checkbutton(win, text='vs Transport/Paradrop/CAS', variable=self.vs_para)

        self.mountain = BooleanVar()
        self.mountain.set(False)
        self.c11 = Checkbutton(win, text='Mission in mountain', variable=self.mountain)

        self.cruise = BooleanVar()
        self.cruise.set(False)
        self.c12 = Checkbutton(win, text='vs Cruise Missle', variable=self.cruise)

        self.stealth = BooleanVar()
        self.stealth.set(False)
        self.c13 = Checkbutton(win, text='solely Stealth mission', variable=self.stealth)

        self.SAM_HQ = BooleanVar()
        self.SAM_HQ.set(False)
        self.c14 = Checkbutton(win, text='Target near HQ', variable=self.SAM_HQ)

        self.helo_over_enemy = BooleanVar()
        self.helo_over_enemy.set(False)
        self.c15 = Checkbutton(win, text='Helo flew over enemy', variable=self.helo_over_enemy)

        self.sam_vs_cruise = BooleanVar()
        self.sam_vs_cruise.set(False)
        self.c16 = Checkbutton(win, text='SAM vs Cruise Missile', variable=self.sam_vs_cruise)

        self.sam_vs_stealth = BooleanVar()
        self.sam_vs_stealth.set(False)
        self.c17 = Checkbutton(win, text='SAM vs Stealth', variable=self.sam_vs_stealth)

        self.lbl17 = Label(win, text='Wild Weasel')
        self.cb7 = Combobox(win, values=('0', '1', '2'), width=5)
        self.cb7.set('0')

        self.aaa_vs_helos = BooleanVar()
        self.aaa_vs_helos.set(False)
        self.c18 = Checkbutton(win, text='AAA vs Helos', variable=self.aaa_vs_helos)

        self.ciws = BooleanVar()
        self.ciws.set(False)
        self.c19 = Checkbutton(win, text='CIWS', variable=self.ciws)

        self.usn_ciws = BooleanVar()
        self.usn_ciws.set(False)
        self.c20 = Checkbutton(win, text='USN CIWS', variable=self.usn_ciws)

        self.aaa_vs_transport = BooleanVar()
        self.aaa_vs_transport.set(False)
        self.c21 = Checkbutton(win, text='AAA vs Transport', variable=self.aaa_vs_transport)

        self.aaa_vs_stealth = BooleanVar()
        self.aaa_vs_stealth.set(False)
        self.c22 = Checkbutton(win, text='AAA vs Stealth', variable=self.aaa_vs_stealth)

        self.lbl1 = Label(win, text='Pilot skills:')

        self.lbl0.place(x=50, y=40)
        self.lbl1.place(x=50, y=80)
        self.lbl2.place(x=250, y=40)
        self.cb0.place(x=150, y=40)
        self.cb1.place(x=150, y=80)
        self.cb2.place(x=350, y=40)
        self.lbl25.place(x=250, y=80)
        self.c23.place(x=250, y=120)
        self.c24.place(x=250, y=160)
        self.cb9.place(x=350, y=80)
        self.lbl3.place(x=450, y=40)
        self.r1.place(x=450, y=80)
        self.r2.place(x=450, y=120)
        self.r3.place(x=450, y=160)
        self.lbl4.place(x=450, y=200)
        self.r4.place(x=450, y=240)
        self.r5.place(x=450, y=280)
        self.r6.place(x=450, y=320)
        self.c2.place(x=50, y=120)
        self.c3.place(x=50, y=160)
        self.lbl6.place(x=50, y=280)
        self.lbl7.place(x=50, y=240)
        self.lbl9.place(x=50, y=320)
        self.t1.place(x=150, y=280)
        self.t2.place(x=150, y=240)
        self.t4.place(x=150, y=320)
        self.lbl27.place(x=250, y=280)
        self.lbl28.place(x=250, y=240)
        self.lbl29.place(x=250, y=320)
        self.t15.place(x=350, y=280)
        self.t16.place(x=350, y=240)
        self.t17.place(x=350, y=320)
        self.c25.place(x=150, y=200)
        self.btn1.place(x=50, y=200)
        self.lbl10.place(x=600, y=40)
        self.cb3.place(x=700, y=40)
        self.lbl11.place(x=600, y=80)
        self.cb4.place(x=700, y=80)
        self.c6.place(x=600, y=120)
        self.c7.place(x=600, y=160)
        self.c8.place(x=600, y=200)
        self.c9.place(x=600, y=240)
        self.c10.place(x=600, y=280)
        self.c11.place(x=600, y=320)
        self.c12.place(x=600, y=360)
        self.c13.place(x=600, y=400)
        self.lbl12.place(x=600, y=440)
        self.cb5.place(x=700, y=440)
        self.btn2.place(x=600, y=480)
        self.lbl13.place(x=600, y=520)
        self.lbl14.place(x=600, y=560)
        self.lbl15.place(x=600, y=600)
        self.t6.place(x=700, y=520)
        self.t7.place(x=700, y=560)
        self.t8.place(x=700, y=600)
        self.lbl16.place(x=800, y=40)
        self.cb6.place(x=900, y=40)
        self.c14.place(x=800, y=80)
        self.c15.place(x=800, y=120)
        self.c16.place(x=800, y=160)
        self.c17.place(x=800, y=200)
        self.lbl17.place(x=800, y=240)
        self.cb7.place(x=900, y=240)
        self.btn3.place(x=800, y=280)
        self.lbl18.place(x=800, y=320)
        self.t9.place(x=900, y=320)
        self.lbl19.place(x=800, y=360)
        self.t10.place(x=900, y=360)
        self.lbl20.place(x=800, y=400)
        self.t11.place(x=900, y=400)
        self.lbl21.place(x=1000, y=40)
        self.cb8.place(x=1100, y=40)
        self.c18.place(x=1000, y=80)
        self.c19.place(x=1000, y=120)
        self.c20.place(x=1000, y=160)
        self.c21.place(x=1000, y=200)
        self.c22.place(x=1000, y=240)
        self.btn4.place(x=1000, y=280)
        self.lbl22.place(x=1000, y=320)
        self.lbl23.place(x=1000, y=360)
        self.lbl24.place(x=1000, y=400)
        self.t12.place(x=1100, y=320)
        self.t13.place(x=1100, y=360)
        self.t14.place(x=1100, y=400)

    def skill_active(self, actual_distance):
        actual_distance = actual_distance.get()
        if actual_distance == 3:
            self.cb1.config(state='normal')
            self.cb9.config(state='normal')
        else:
            self.cb1.config(state='disabled')
            self.cb9.config(state='disabled')
        if actual_distance == 2:
            self.c3.config(state='normal')
            self.c24.config(state='normal')
        else:
            self.c3.config(state='disabled')
            self.c24.config(state='disabled')

    def calculate_a2a(self):

        Air_Combat_Result_dogfight = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-'],
                                      ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-'],
                                      ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-'],
                                      ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-'],
                                      ['X', 'X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-'],
                                      ['X', 'DA', 'DA', 'A', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                                      ['DA', 'DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-'],
                                      ['DA', 'A', 'D', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                      ['A', 'D', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

        Air_Combat_Result_long = [['X', 'X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-'],
                                  ['X', 'X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-'],
                                  ['X', 'X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-'],
                                  ['X', 'X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-'],
                                  ['X', 'X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-'],
                                  ['X', 'DA', 'DA', 'A', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-'],
                                  ['DA', 'DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-'],
                                  ['DA', 'A', 'Ad', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                  ['A', 'Ad', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t15.delete(0, 'end')
        self.t16.delete(0, 'end')
        self.t17.delete(0, 'end')

        if self.cb2.get() == '#':
            target = 0
        else:
            target = int(self.cb2.get())
        fire = int(self.cb0.get())
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
        if self.strike.get() == 1:
            DRM_att += 2
        if target == 0 and self.actual_distance.get() == 2:
            DRM_att -= 1
        if self.not_proper.get() == 1 and self.actual_distance.get() == 2:
            DRM_att += 1
        if self.actual_distance.get() == 3:
            skill_att = int(self.cb1.get())
            DRM_att += skill_att
        if self.vs_bomber.get() == 1 and self.actual_distance.get() == 3:
            DRM_att -= 1
        if self.actual_weather.get() == 2 and self.actual_distance.get() == 3:
            DRM_att += 1

        row_att = d10_att + DRM_att
        if row_att > 10:
            row_att = 10
        if row_att < -2:
            row_att = -2
        row_att += 2

        if self.actual_distance.get() == 3:
            result_att = Air_Combat_Result_dogfight[column_att][row_att]
        else:
            result_att = Air_Combat_Result_long[column_att][row_att]

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
            if self.strike_def.get() == 1:
                DRM_def += 2
            if target == 0 and self.actual_distance.get() == 2:
                DRM_def -= 1
            if self.not_proper_def.get() == 1 and self.actual_distance.get() == 2:
                DRM_def += 1
            if self.actual_distance.get() == 3:
                skill_def = int(self.cb9.get())
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
                result_def = Air_Combat_Result_dogfight[column_def][row_def]
            else:
                result_def = Air_Combat_Result_long[column_def][row_def]
        else:
            d10_def = '-'
            DRM_def = '-'
            result_def = '-'

        self.t4.insert(END, result_att)
        self.t2.insert(END, str(DRM_att))
        self.t1.insert(END, str(d10_att))
        self.t15.insert(END, str(d10_def))
        self.t16.insert(END, str(DRM_def))
        self.t17.insert(END, str(result_def))

        self.not_proper.set(0)
        self.strike.set(0)
        self.not_proper_def.set(0)
        self.strike_def.set(0)
        self.vs_bomber.set(0)
        self.not_mutual.set(False)

    def calculate_detection(self):

        self.t6.delete(0, 'end')
        self.t7.delete(0, 'end')
        self.t8.delete(0, 'end')
        detection_to_column = {'Local': 0, '0-1': 1, '2-3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
        advanced_detection_table = [['D', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                                    ['ED', 'D', 'D', '-', '-', '-', '-', '-', '-', '-'],
                                    ['ED', 'D', 'D', 'D', '-', '-', '-', '-', '-', '-'],
                                    ['ED', 'ED', 'D', 'D', 'D', '-', '-', '-', '-', '-'],
                                    ['ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-', '-'],
                                    ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-', '-'],
                                    ['ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-', '-'],
                                    ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-', '-'],
                                    ['ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', 'D', '-'],
                                    ['ED', 'ED', 'ED', 'ED', 'ED', 'D', 'D', 'D', 'D', '-']]

        detection_value = self.cb3.get()
        column = detection_to_column[detection_value]

        d10 = randint(0, 9)
        awacs_to_num = {'0-1': 0, '2': -1, '3': -2, '4': -3}
        DRM = 0
        if self.near_HQ.get():
            DRM -= 1
        if self.passed_occ.get():
            DRM -= 1
        if self.vs_helos.get():
            DRM -= 1
        if self.EZOC_landing.get():
            DRM -= 1
        if self.vs_para.get():
            DRM += 1
        if self.mountain.get():
            DRM += 1
        if self.cruise.get():
            DRM += 1
        if self.stealth.get():
            DRM += 5
        if self.actual_weather.get() == 2:
            DRM += 1
        if self.actual_weather.get() == 3:
            DRM += 3
        if detection_value != 'Local':
            awacs = awacs_to_num[self.cb4.get()]
            DRM += awacs
        weasel = int(self.cb5.get())
        DRM += weasel
        row = d10 + DRM
        if row < 0:
            row = 0
        if row > 9:
            row = 9
        result = advanced_detection_table[column][row]
        self.t6.insert(END, str(DRM))
        self.t7.insert(END, str(d10))
        self.t8.insert(END, result)

    def sam_defence(self):

        self.t9.delete(0, 'end')
        self.t10.delete(0, 'end')
        self.t11.delete(0, 'end')

        sam_value_to_column = {'Local': 2, '0-1': 0, '2': 1, '3-4': 2, '5-6': 3, '7': 4, '8': 5, '9': 6, '10': 7}
        advanced_sam_table = [['A', '+1', '+1', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                              ['X', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-', '-'],
                              ['X', 'A', 'A', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                              ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-', '-'],
                              ['X', 'X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-'],
                              ['X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-'],
                              ['X', 'X', 'X', 'A', 'A', 'A', '+2', '+2', '+1', '+1', '-']]

        column = sam_value_to_column[self.cb6.get()]

        d10 = randint(0, 9)
        DRM = 0
        if self.SAM_HQ.get():
            DRM -= 1
        if self.helo_over_enemy.get():
            DRM -= 1
        if self.sam_vs_cruise.get():
            DRM += 1
        if self.sam_vs_stealth.get():
            DRM += 3
        if self.actual_weather.get() == 2:
            DRM += 1
        if self.actual_weather.get() == 3:
            DRM += 3
        weasel = int(self.cb7.get())
        DRM += 2 * weasel
        row = d10 + DRM
        if row < 0:
            row = 0
        if row > 10:
            row = 10
        result = advanced_sam_table[column][row]
        self.t9.insert(END, str(DRM))
        self.t10.insert(END, str(d10))
        self.t11.insert(END, result)

    def aaa_defence(self):

        self.t12.delete(0, 'end')
        self.t13.delete(0, 'end')
        self.t14.delete(0, 'end')

        aaa_value_to_column = {'Local': 0, '0-1': 0, '2': 1, '3': 2}
        advanced_aaa_table = [['+2', '+1', '+1', '-', '-', '-', '-', '-', '-', '-'],
                              ['A', '+2', '+2', '+1', '+1', '-', '-', '-', '-', '-'],
                              ['X', 'A', 'A', '+2', '+2', '+1', '+1', '-', '-', '-']]
        column = aaa_value_to_column[self.cb8.get()]

        d10 = randint(0, 9)
        DRM = 0
        if self.aaa_vs_helos.get():
            DRM -= 1
        if self.ciws.get():
            DRM -= 1
        if self.usn_ciws.get():
            DRM -= 2
        if self.aaa_vs_transport.get():
            DRM -= 1
        if self.aaa_vs_stealth.get():
            DRM += 3
        if self.actual_weather.get() == 2:
            DRM += 2
        if self.actual_weather.get() == 3:
            DRM += 4
        row = d10 + DRM
        if row < 0:
            row = 0
        if row > 9:
            row = 9

        result = advanced_aaa_table[column][row]

        self.t12.insert(END, str(DRM))
        self.t13.insert(END, str(d10))
        self.t14.insert(END, result)


window = Tk()
mywin = MyWindow(window)
window.title('Advanced Air Warfare Calculator')
window.geometry("1300x800+10+10")
window.mainloop()
