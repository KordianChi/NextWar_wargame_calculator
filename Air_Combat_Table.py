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

        self.lbl4 = Label(win, text='Weather:')
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

        self.btn2 = Button(win, text='Calculate', command=self.calculate_detection)
        self.btn3 = Button(win, text='Calculate', command=self.sam_defence)
        self.btn4 = Button(win, text='Calculate', command=self.aaa_defence)


        self.t6 = Entry(width=7)
        self.t7 = Entry(width=7)
        self.t8 = Entry(width=7)
        self.t9 = Entry(width=7)
        self.t10 = Entry(width=7)
        self.t11 = Entry(width=7)
        self.t12 = Entry(width=7)
        self.t13 = Entry(width=7)
        self.t14 = Entry(width=7)



        self.actual_weather = IntVar()
        self.actual_weather.set(1)

        self.r4 = Radiobutton(win, text="Clear", variable=self.actual_weather, value=1)
        self.r5 = Radiobutton(win, text="Overcast", variable=self.actual_weather, value=2)
        self.r6 = Radiobutton(win, text="Storm", variable=self.actual_weather, value=3)


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


        self.lbl10.place(x=50, y=40)
        self.lbl11.place(x=50, y=80)
        self.c6.place(x=50, y=120)
        self.c7.place(x=50, y=160)
        self.c8.place(x=50, y=200)
        self.c9.place(x=50, y=240)
        self.c10.place(x=50, y=280)
        self.c11.place(x=50, y=320)
        self.c12.place(x=50, y=360)
        self.c13.place(x=50, y=400)
        self.lbl12.place(x=50, y=440)
        self.btn2.place(x=50, y=480)
        self.lbl13.place(x=50, y=520)
        self.lbl14.place(x=50, y=560)
        self.lbl15.place(x=50, y=600)
        self.cb3.place(x=150, y=40)
        self.cb4.place(x=150, y=80)
        self.cb5.place(x=150, y=440)
        self.t6.place(x=150, y=520)
        self.t7.place(x=150, y=560)
        self.t8.place(x=150, y=600)
        self.lbl4.place(x=250, y=440)
        self.r4.place(x=250, y=480)
        self.r5.place(x=250, y=520)
        self.r6.place(x=250, y=560)
        self.lbl16.place(x=250, y=40)
        self.c14.place(x=250, y=80)
        self.c15.place(x=250, y=120)
        self.c16.place(x=250, y=160)
        self.c17.place(x=250, y=200)
        self.lbl17.place(x=250, y=240)
        self.btn3.place(x=250, y=280)
        self.lbl19.place(x=250, y=360)
        self.lbl18.place(x=250, y=320)
        self.lbl20.place(x=250, y=400)
        self.cb6.place(x=350, y=40)
        self.cb7.place(x=350, y=240)
        self.t9.place(x=350, y=320)
        self.t10.place(x=350, y=360)
        self.t11.place(x=350, y=400)
        self.lbl21.place(x=450, y=40)
        self.c18.place(x=450, y=80)
        self.c19.place(x=450, y=120)
        self.c20.place(x=450, y=160)
        self.c21.place(x=450, y=200)
        self.c22.place(x=450, y=240)
        self.btn4.place(x=450, y=280)
        self.lbl22.place(x=450, y=320)
        self.lbl23.place(x=450, y=360)
        self.lbl24.place(x=450, y=400)
        self.cb8.place(x=550, y=40)
        self.t12.place(x=550, y=320)
        self.t13.place(x=550, y=360)
        self.t14.place(x=550, y=400)


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
window.geometry("650x650+10+10")
window.mainloop()
