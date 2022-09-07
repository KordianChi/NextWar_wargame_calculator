from tkinter import Label, IntVar, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint
from functools import partial
from sof_constants import raid_result_table, recon_result_table, targeting_result, detection_result, terrain_types, \
    recon_types, raid_types, recon_table, raid_table


class SofTable(Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title('SOF Calculator')
        self.geometry("500x500+10+10")

        self.mission_type = IntVar()
        self.mission_type.set(0)
        self.mission_type_rbtn_1 = Radiobutton(self, text='Recon', variable=self.mission_type, value=0,
                                               command=partial(self.raid_recon_active, self.mission_type))
        self.mission_type_rbtn_2 = Radiobutton(self, text='Raid', variable=self.mission_type, value=1,
                                               command=partial(self.raid_recon_active, self.mission_type))

        self.terrain_type_cbx = Combobox(self, values=terrain_types, width=30)
        self.terrain_type_cbx.set('Flat/Rough/Marsh')

        self.recon_mission_target_cbx = Combobox(self, values=recon_types, width=30)
        self.recon_mission_target_cbx.set('HQ')

        self.raid_mission_target_cbx = Combobox(self, values=raid_types, width=30)
        self.raid_mission_target_cbx.set('HQ')
        self.raid_mission_target_cbx.config(state='disabled')

        self.raid_drms_lbl = Label(self, text='Raid DRMs:')

        self.storm = BooleanVar()
        self.storm.set(False)
        self.storm_chk = Checkbutton(self, text='Storm', variable=self.storm, state='disabled')

        self.bridge = BooleanVar()
        self.bridge.set(False)
        self.bridge_chk = Checkbutton(self, text='vs bridge', variable=self.bridge, state='disabled')

        self.city = BooleanVar()
        self.city.set(False)
        self.city_chk = Checkbutton(self, text='hex contain city', variable=self.city, state='disabled')

        self.naval = BooleanVar()
        self.naval.set(False)
        self.naval_chk = Checkbutton(self, text='vs Naval unit', variable=self.naval, state='disabled')

        self.less_brigade = BooleanVar()
        self.less_brigade.set(False)
        self.less_brigade_chk = Checkbutton(self, text='occupied less than brigade',
                                            variable=self.less_brigade, state='disabled')

        self.least_brigade = BooleanVar()
        self.least_brigade.set(False)
        self.least_brigade_chk = Checkbutton(self, text='occupied at least brigade',
                                             variable=self.least_brigade, state='disabled')
        self.sam_or_theater = BooleanVar()
        self.sam_or_theater.set(False)
        self.sam_or_theater_chk = Checkbutton(self, text='vs SAM or theater',
                                              variable=self.sam_or_theater, state='disabled')

        self.us_uk = BooleanVar()
        self.us_uk.set(False)
        self.us_uk_chk = Checkbutton(self, text='US/UK unit', variable=self.us_uk)

        self.allied = BooleanVar()
        self.allied.set(False)
        self.allied_chk = Checkbutton(self, text='non-US/UK allied unit', variable=self.allied)

        self.surprise_lbl = Label(self, text='Surprise')
        self.surprise_cbx = Combobox(self, values=('0', '1', '2'), width=5)
        self.surprise_cbx.set('0')
        self.survive_drm_lbl = Label(self, text='Survive DRMs')

        self.calculate_btn = Button(self, text='Calculate', command=self.calculate_result)
        self.result_d10_lbl = Label(self, text='Result d10:')
        self.result_d10_ent = Entry(self, width=8)
        self.result_lbl = Label(self, text='Result:')
        self.result_ent = Entry(width=8)
        self.survive_d10_lbl = Label(self, text='Survive d10:')
        self.survive_d10_ent = Entry(self, width=8)
        self.survive_lbl = Label(self, text='Survive:')
        self.survive_ent = Entry(self, width=8)

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
        self.result_d10_ent.delete(0, 'end')
        self.result_ent.delete(0, 'end')

        d10_result = randint(0, 9)
        if self.mission_type.get() == 0:
            row = d10_result
            if row > 8:
                row = 8
            if self.recon_mission_target_cbx.get() == 'Targeting':
                result = targeting_result[row]
            else:
                target = recon_table[self.recon_mission_target_cbx.get()]
                column = target[self.terrain_type_cbx.get()]
                result = recon_result_table[column][row]

        else:
            drm_raid = 0
            if self.storm.get():
                drm_raid -= 1
            if self.bridge.get():
                drm_raid -= 1
            if self.city.get():
                drm_raid -= 1
            if self.naval.get():
                drm_raid += 1
            if self.less_brigade.get():
                drm_raid += 1
            if self.least_brigade.get():
                drm_raid += 2
            if self.sam_or_theater.get():
                drm_raid += 1
            row = d10_result + drm_raid
            if row < 0:
                row = 0
            if row > 8:
                row = 8
            if self.raid_mission_target_cbx.get() == 'Detection/SAM/Theater Weapon':
                result = detection_result[row]
            else:
                target = raid_table[self.raid_mission_target_cbx.get()]
                column = target[self.terrain_type_cbx.get()]

                result = raid_result_table[column][row]

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

        self.survive_d10_ent.insert(END, str(d10_survive))
        self.survive_ent.insert(END, survive)
        self.result_d10_ent.insert(END, str(d10_result))
        self.result_ent.insert(END, result)