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

        self.mission_type = IntVar()
        self.mission_type.set(0)
        self.mission_type_rbtn_1 = Radiobutton(win, text='Recon', variable=self.mission_type, value=0,
                                               command=partial(self.raid_recon_active, self.mission_type))
        self.mission_type_rbtn_2 = Radiobutton(win, text='Raid', variable=self.mission_type, value=1,
                                               command=partial(self.raid_recon_active, self.mission_type))

        terrain_types = ('Flat/Rough/Marsh', 'Flat Woods/Rough Wds',
                         'Highland/Highland Wds', 'Mountain/Urban/Jungle')
        self.terrain_type_cbx = Combobox(win, values=terrain_types, width=30)
        self.terrain_type_cbx.set('Flat/Rough/Marsh')

        recon_types = ('HQ', 'SAM', 'Supply Depot', 'MSU','Ground Unit', 'Targeting')
        self.recon_mission_target_cbx = Combobox(win, values=recon_types, width=30)
        self.recon_mission_target_cbx.set('HQ')

        raid_types = ('HQ','Supply Depot', 'Interdiction', 'Instalation','Naval', 'Airfield', 'Helo',
                      'MSU', 'Detection/SAM/Theater Weapon')
        self.raid_mission_target_cbx = Combobox(win, values=raid_types, width=30)
        self.raid_mission_target_cbx.set('HQ')
        self.raid_mission_target_cbx.config(state='disabled')

        self.raid_drms_lbl = Label(win, text='Raid DRMs:')

        self.storm = BooleanVar()
        self.storm.set(False)
        self.storm_chk = Checkbutton(win, text='Storm', variable=self.storm, state='disabled')

        self.bridge = BooleanVar()
        self.bridge.set(False)
        self.bridge_chk = Checkbutton(win, text='vs bridge', variable=self.bridge, state='disabled')

        self.city = BooleanVar()
        self.city.set(False)
        self.city_chk = Checkbutton(win, text='hex contain city', variable=self.city, state='disabled')

        self.naval = BooleanVar()
        self.naval.set(False)
        self.naval_chk = Checkbutton(win, text='vs Naval unit', variable=self.naval, state='disabled')

        self.less_brigade = BooleanVar()
        self.less_brigade.set(False)
        self.less_brigade_chk = Checkbutton(win, text='occupied less than brigade',
                                            variable=self.less_brigade, state='disabled')

        self.least_brigade = BooleanVar()
        self.least_brigade.set(False)
        self.least_brigade_chk = Checkbutton(win, text='occupied at least brigade',
                                             variable=self.least_brigade, state='disabled')
        self.sam_or_theater = BooleanVar()
        self.sam_or_theater.set(False)
        self.sam_or_theater_chk = Checkbutton(win, text='vs SAM or theater',
                                              variable=self.sam_or_theater, state='disabled')

        self.us_uk = BooleanVar()
        self.us_uk.set(False)
        self.us_uk_chk = Checkbutton(win, text='US/UK unit', variable=self.us_uk)

        self.allied = BooleanVar()
        self.allied.set(False)
        self.allied_chk = Checkbutton(win, text='non-US/UK allied unit', variable=self.allied)

        self.surprise_lbl = Label(win, text='Surprise')
        self.surprise_cbx = Combobox(win, values=('0', '1', '2'), width=5)
        self.surprise_cbx.set('0')
        self.survive_drm_lbl = Label(win, text='Survive DRMs')

        self.calculate_btn = Button(win, text='Calculate', command=self.calculate_result)
        self.result_d10_lbl = Label(win, text='Result d10:')
        self.result_d10_ent = Entry(width=8)
        self.result_lbl = Label(win, text='Result:')
        self.result_ent = Entry(width=8)
        self.survive_d10_lbl = Label(win, text='Survive d10:')
        self.survive_d10_ent = Entry(width=8)
        self.survive_lbl = Label(win, text='Survive:')
        self.survive_ent = Entry(width=8)

        self.mission_type_rbtn_1.place(x=50, y=40)
        self.mission_type_rbtn_2.place(x=150, y=40)
        self.recon_mission_target_cbx.place(x=50, y=80)
        self.raid_mission_target_cbx.place(x=50, y=120)
        self.terrain_type_cbx.place(x=50, y=160)

        self.raid_drms_lbl.place(x=50, y=200)
        self.storm_chk.place(x=150, y=200)
        self.bridge_chk.place(x=150, y=240)
        self.city_chk.place(x=150, y=280)
        self.naval_chk.place(x=150, y=320)
        self.sam_or_theater_chk.place(x=150, y=360)
        self.less_brigade_chk.place(x=150, y=400)
        self.least_brigade_chk.place(x=150, y=440)


        self.survive_drm_lbl.place(x=300, y=40)
        self.us_uk_chk.place(x=300, y=80)
        self.allied_chk.place(x=300, y=120)
        self.surprise_lbl.place(x=300, y=160)
        self.surprise_cbx.place(x=380, y=160)
        self.calculate_btn.place(x=300, y=200)
        self.result_d10_lbl.place(x=300, y=240)
        self.result_d10_ent.place(x=380, y=240)
        self.result_lbl.place(x=300, y=280)
        self.result_ent.place(x=380, y=280)
        self.survive_d10_lbl.place(x=300, y=320)
        self.survive_d10_ent.place(x=380, y=320)
        self.survive_lbl.place(x=300, y=360)
        self.survive_ent.place(x=380, y=360)

    def raid_recon_active(self, mission_type):
        mission_type = mission_type.get()
        if mission_type == 0:
            self.raid_mission_target_cbx.config(state='disabled')
            self.recon_mission_target_cbx.config(state='normal')
            self.storm_chk.config(state='disabled')
            self.bridge_chk.config(state='disabled')
            self.city_chk.config(state='disabled')
            self.naval_chk.config(state='disabled')
            self.less_brigade_chk.config(state='disabled')
            self.least_brigade_chk.config(state='disabled')
            self.sam_or_theater_chk.config(state='disabled')
        else:
            self.recon_mission_target_cbx.config(state='disabled')
            self.raid_mission_target_cbx.config(state='normal')
            self.storm_chk.config(state='normal')
            self.bridge_chk.config(state='normal')
            self.city_chk.config(state='normal')
            self.naval_chk.config(state='normal')
            self.less_brigade_chk.config(state='normal')
            self.least_brigade_chk.config(state='normal')
            self.sam_or_theater_chk.config(state='normal')

    def calculate_result(self):

        self.survive_d10_ent.delete(0, 'end')
        self.survive_ent.delete(0, 'end')




# Check survive
        d10_survive = randint(0, 9)
        drm_survive = 0
        if self.us_uk.get():
            drm_survive -= 3
        if self.allied.get():
            drm_survive -= 1
        if int(self.surprise_cbx.get()) != 0:
            mod_surprise = int(self.surprise_cbx.get()) + 1
            drm_survive -= mod_surprise
        if self.mission_type.get() == 1:
            drm_survive += 1
            if self.raid_mission_target_cbx.get() == 'Interdiction':
                drm_survive += 1
        d10_survive += drm_survive

        if d10_survive < 7:
            survive = 'Yes'
        else:
            survive = 'No'

        self.survive_d10_ent.insert(END, d10_survive)
        self.survive_ent.insert(END, survive)




window = Tk()
mywin = MyWindow(window)
window.title('SOF Calculator')
window.geometry("500x500+10+10")
window.mainloop()
