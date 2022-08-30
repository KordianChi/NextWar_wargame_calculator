# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 11:03:36 2022
"""
import math
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import Tk
from tkinter.ttk import Combobox
from random import randint


class MyWindow:
    def __init__(self, win):
        self.lbl0 = Label(win, text='Terrain Type')
        self.lbl1 = Label(win, text='Attacker:')
        self.lbl2 = Label(win, text='Defender:')
        self.lbl3 = Label(win, text='Shift left:')
        self.lbl4 = Label(win, text='Shift right:')
        self.lbl5 = Label(win, text='DRM plus:')
        self.lbl6 = Label(win, text='DRM minus:')
        self.lbl7 = Label(win, text='D10:')
        self.lbl8 = Label(win, text='Attack : Defence')
        self.lbl9 = Label(win, text='Dice + DRM:')
        self.lbl10 = Label(win, text='Combat result:')
        self.lbl11 = Label(win, text='Reduce attacker loss:')
        self.cb = Combobox(win, values=("Flat or Flat Woods", "Rough, Rough Woods, Marsh or Paddy",
                                           "Highlands, any Jungle, Highland Woods", "Mountain", "Urban"), width=35)

        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.t6 = Entry()
        self.t7 = Entry()
        self.t8 = Entry()
        self.t9 = Entry()
        self.t10 = Entry()
        self.t11 = Entry()

        self.cb.place(x=200, y=50)
        self.lbl0.place(x=100, y=50)
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=200, y=100)
        self.lbl2.place(x=100, y=150)
        self.t2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)
        self.lbl5.place(x=100, y=300)
        self.t5.place(x=200, y=300)
        self.lbl6.place(x=100, y=350)
        self.t6.place(x=200, y=350)
        self.b1 = Button(win, text='Calculate', command=self.calculate)
        self.b1.place(x=250, y=400)
        self.lbl7.place(x=100, y=450)
        self.t7.place(x=250, y=450)
        self.lbl8.place(x=100, y=500)
        self.t8.place(x=250, y=500)
        self.lbl9.place(x=100, y=550)
        self.t9.place(x=250, y=550)
        self.lbl10.place(x=100, y=600)
        self.t10.place(x=250, y=600)
        self.lbl11.place(x=100, y=650)
        self.t11.place(x=250, y=650)

    def calculate(self):
        combat_result_table = [['1/1R', '1/1', '1/1', '1/1', '1/-', '2/1', '2/1', '2/-',
                                '1/1', '2/-', '3/1', '3/-', '2/1', '4/-', '4/-', '4/-'],
                               ['1/1R', '1/1R', '1/1', '1/1', '1/1', '1/-', '2/1', '2/1',
                                '2/-', '2/-', '2/1', '3/1', '3/-', '3/-', '2/1', '4/-'],
                               ['-/1R', '1/1R', '1/1R', '1/1', '1/2', '1/1', '1/-', '2/1',
                                '2/1', '2/-', '2/-', '2/-', '3/1', '2/1', '3/-', '4/-'],
                               ['-/1R', '-/1R', '1/1R', '1/1R', '1/1', '1/-', '1/1', '1/-',
                                '2/1', '2/1', '1/1', '2/-', '2/-', '3/1', '2/1', '2/-'],
                               ['-/2R', '-/1R', '-/1R', '1/1R', '1/1R', '1/1', '1/1', '1/1',
                                '1/-', '2/1', '2/1', '2/-', '2/-', '2/-', '3/1', '3/-'],
                               ['/-2R', '1/2R', '-/1', '-/1R', '1/2', '1/1R', '1/1', '1/1',
                                '2/1', '1/-', '2/1', '2/1', '2/-', '1/1', '2/-', '3/1'],
                               ['-/2R', '-/2R', '1/2R', '-/1R', '-/1R', '1/1R', '1/2', '1/1',
                                '1/1', '1/-', '1/-', '2/1', '1/1', '2/-', '2/1', '2/-'],
                               ['-/3R', '-/2R', '-/2R', '1/2R', '-/1', '-/1R', '1/1R', '1/1R',
                                '1/2', '1/1', '1/1', '1/-', '2/1', '1/1', '2/-', '2/1'],
                               ['-/3R', '1/3R', '-/2R', '-/1R', '1/2R', '-/1R', '-/2', '1/1R',
                                '1/1R', '1/1', '1/2', '1/1', '1/-', '1/1', '2/1', '3/1'],
                               ['-/3R', '-/3R', '1/3R', '-/2R', '-/1R', '1/2R', '-/1R', '-/1R',
                                '1/2', '1/1R', '1/1R', '1/1', '2/1', '1/-', '2/1', '1/-'],
                               ['-/4R', '1/3R', '-/3R', '1/3R', '-/2', '-/2R', '1/2R', '-/1',
                                '-/1R', '-/1R', '1/2', '1/1R', '1/1', '1/1', '1/-', '2/1'],
                               ['-/4R', '1/4R', '-/3R', '1/2', '1/3R', '-/2R', '-/2', '1/2R',
                                '-/1R', '1/1', '-/1R', '1/1R', '1/1R', '1/1', '1/1', '2/1'],
                               ['-/4R', '-/4R', '1/4R', '1/3', '-/3R', '1/3R', '-/2', '-/2R',
                                '1/2R', '-/1R', '-/1', '-/1R', '1/1R', '1/1R', '1/-', '2/1']]
        terrain = self.cb.get()
        terrain_to_type = {"Flat or Flat Woods": 6, "Rough, Rough Woods, Marsh or Paddy": 7,
                           "Highlands, any Jungle, Highland Woods": 8, "Mountain": 9, "Urban": 10}
        terrain_to_shift = {"Flat or Flat Woods": 4, "Rough, Rough Woods, Marsh or Paddy": 3,
                            "Highlands, any Jungle, Highland Woods": 2, "Mountain": 1, "Urban": 0}
        shift = terrain_to_shift[terrain]
        odds_to_column = {'1:3': 1, '1:2': 2, '1:1': 3, '1.5:1': 4, '2:1': 5, '3:1': 6, '4:1': 7,
                          '5:1': 8, '6:1': 9, '7:1': 10, '8:1': 11, '9:1': 12, '10:1': 13}
        terrain_type = terrain_to_type[terrain]
        DRM_plus = int(self.t5.get())
        DRM_minus = -abs(int(self.t6.get()))
        DRM = DRM_plus + DRM_minus
        self.t7.delete(0, 'end')
        self.t8.delete(0, 'end')
        self.t9.delete(0, 'end')
        self.t10.delete(0, 'end')
        self.t11.delete(0, 'end')
        att = int(self.t1.get())
        defe = int(self.t2.get())
        mod_minus = int(self.t3.get())
        mod_plus = int(self.t4.get())
        mod = mod_plus - abs(mod_minus)
        
        frac = max(min(att / defe, terrain_type), min(defe / att, 3))
        if att < defe:
            frac = -frac

        if frac == 1.5:
            rem = 0
        else:
            if frac > 0:
                rem = frac - math.floor(frac)
            else:
                rem = 0
        if rem > 0:
            DRM -= 1

        frac_to_order = {-3: -2, -2: -1, 1: 0, 1.5: 1, 2: 2, 3: 3, 4: 4,
                         5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
        order_to_frac = {-2: 3, -1: 2, 0: 1, 1: 1.5, 2: 2, 3: 3, 4: 4,
                         5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

        if 2 > frac >= 1.5:
            att_res_pure = 1.5
            order_pure = frac_to_order[att_res_pure]
            order = order_pure + mod
            if order > terrain_type:
                order = terrain_type
            if order < -2:
                order = -2
            if order > 0:
                att_res = order_to_frac[order]
                defe_res = 1
            else:
                defe_res = order_to_frac[order]
                att_res = 1
        else:
            if frac > 0:
                att_res_pure = math.floor(frac)
            
                order_pure = frac_to_order[att_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = order_to_frac[order]
                    defe_res = 1
                else:
                    defe_res = order_to_frac[order]
                    att_res = 1
            else:
                if frac > -2:
                    defe_res_pure = -2
                else:
                    defe_res_pure = -3
                order_pure = frac_to_order[defe_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = order_to_frac[order]
                    defe_res = 1
                else:
                    defe_res = order_to_frac[order]
                    att_res = 1
        dice = randint(0, 9)
        randomness = dice + DRM
        # row normalization
        if randomness > 12:
            randomness = 12
        if randomness < -3:
            randomness = -3
        row = randomness + 3
        odds = str(att_res) + ':' + str(defe_res)
        column = odds_to_column[odds]
        column += shift
        column -= 1

        reduce_attacker_lost = 'No'
        if column > 9:
            reduce_attacker_lost = 'Yes'

        self.t7.insert(END, str(dice))
        self.t8.insert(END, odds)
        self.t9.insert(END, str(randomness))
        self.t10.insert(END, str(combat_result_table[column][row]))
        self.t11.insert(END, reduce_attacker_lost)


window = Tk()
mywin = MyWindow(window)
window.title('Combat result table')
window.geometry("500x700+10+10")
window.mainloop()
