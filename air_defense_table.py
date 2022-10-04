from tkinter import Label, IntVar, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from random import randint
from constants import DETECTION_TO_COLUMN, ADVANCED_DETECTION_TABLE, SAM_VALUE_TO_COLUMN,\
    ADVANCED_SAM_TABLE, AAA_VALUE_TO_COLUMN, ADVANCED_AAA_TABLE


class AirCombatTable(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Advanced Air Warfare Calculator')
        self.geometry("650x500+10+10")

        self.weather_lbl = Label(self, text='Weather:')
        self.detection_lbl = Label(self, text='Detection:')
        self.detection_cbx = Combobox(self, values=('Local', '0-1', '2-3', '4', '5', '6', '7', '8', '9', '10'), width=5)
        self.detection_cbx.set('Local')
        self.awacs_lbl = Label(self, text='AWACS adv:')
        self.awacs_cbx = Combobox(self, values=('0-1', '2', '3', '4'), width=5)
        self.awacs_cbx.set('0-1')
        self.wild_weasel_det_lbl = Label(self, text='Wild Weasel:')
        self.wild_weasel_det_cbx = Combobox(self, values=('0', '1', '2'), width=5)
        self.wild_weasel_det_cbx.set('0')
        self.detection_drm_lbl = Label(self, text='DRMs:')
        self.detection_dice_lbl = Label(self, text='dice d10:')
        self.detection_result_lbl = Label(self, text='Result:')
        self.sam_lbl = Label(self, text='SAM value:')
        self.sam_cbx = Combobox(self, values=('Local', '0-1', '2', '3-4', '5-6', '7', '8', '9', '10'), width=5)
        self.sam_cbx.set('Local')
        self.sam_drm_lbl = Label(self, text='DRMs:')
        self.sam_dice_lbl = Label(self, text='dice d10:')
        self.sam_result_lbl = Label(self, text='Result:')
        self.aaa_value_lbl = Label(self, text='AAA value:')
        self.aaa_value_cbx = Combobox(self, values=('Local', '0-1', '2', '3'), width=5)
        self.aaa_value_cbx.set('Local')
        self.aaa_drm_lbl = Label(self, text='DRMs:')
        self.aaa_dice_lbl = Label(self, text='dice d10:')
        self.aaa_result_lbl = Label(self, text='Result:')

        self.calculate_detection_btn = Button(self, text='Calculate', command=self.calculate_detection)
        self.sam_defence_btn = Button(self, text='Calculate', command=self.sam_defence)
        self.aaa_defence_btn = Button(self, text='Calculate', command=self.aaa_defence)

        self.det_drm_ent = Entry(self, width=7)
        self.det_dice_ent = Entry(self, width=7)
        self.det_result_ent = Entry(self, width=7)
        self.sam_drm_ent = Entry(self, width=7)
        self.sam_dice_ent = Entry(self, width=7)
        self.sam_result_ent = Entry(self, width=7)
        self.aaa_drm_ent = Entry(self, width=7)
        self.aaa_dice_ent = Entry(self, width=7)
        self.aaa_result_ent = Entry(self, width=7)

        self.actual_weather = IntVar()
        self.actual_weather.set(1)

        self.actual_weather_clear_r = Radiobutton(self, text="Clear", variable=self.actual_weather, value=1)
        self.actual_weather_overcast_r = Radiobutton(self, text="Overcast", variable=self.actual_weather, value=2)
        self.actual_weather_storm_r = Radiobutton(self, text="Storm", variable=self.actual_weather, value=3)

        self.near_HQ = BooleanVar()
        self.near_HQ.set(False)
        self.near_HQ_chk = Checkbutton(self, text='Target near HQ', variable=self.near_HQ)

        self.passed_occ = BooleanVar()
        self.passed_occ.set(False)
        self.passed_occ_chk = Checkbutton(self, text='Passed through occupied hex', variable=self.passed_occ)

        self.vs_helos = BooleanVar()
        self.vs_helos.set(False)
        self.vs_helos_chk = Checkbutton(self, text='vs Attack Helos', variable=self.vs_helos)

        self.EZOC_landing = BooleanVar()
        self.EZOC_landing.set(False)
        self.EZOC_landing_chk = Checkbutton(self, text='Landing in EZOC', variable=self.EZOC_landing)

        self.vs_para = BooleanVar()
        self.vs_para.set(False)
        self.vs_para_chk = Checkbutton(self, text='vs Transport/Paradrop/CAS', variable=self.vs_para)

        self.mountain = BooleanVar()
        self.mountain.set(False)
        self.mountain_chk = Checkbutton(self, text='Mission in mountain', variable=self.mountain)

        self.cruise = BooleanVar()
        self.cruise.set(False)
        self.cruise_chk = Checkbutton(self, text='vs Cruise Missle', variable=self.cruise)

        self.stealth = BooleanVar()
        self.stealth.set(False)
        self.stealth_chk = Checkbutton(self, text='solely Stealth mission', variable=self.stealth)

        self.SAM_HQ = BooleanVar()
        self.SAM_HQ.set(False)
        self.SAM_HQ_chk = Checkbutton(self, text='Target near HQ', variable=self.SAM_HQ)

        self.helo_over_enemy = BooleanVar()
        self.helo_over_enemy.set(False)
        self.helo_over_enemy_chk = Checkbutton(self, text='Helo flew over enemy', variable=self.helo_over_enemy)

        self.sam_vs_cruise = BooleanVar()
        self.sam_vs_cruise.set(False)
        self.sam_vs_cruise_chk = Checkbutton(self, text='SAM vs Cruise Missile', variable=self.sam_vs_cruise)

        self.sam_vs_stealth = BooleanVar()
        self.sam_vs_stealth.set(False)
        self.sam_vs_stealth_chk = Checkbutton(self, text='SAM vs Stealth', variable=self.sam_vs_stealth)

        self.wild_weasel_sam_lbl = Label(self, text='Wild Weasel')
        self.wild_weasel_sam_cbx = Combobox(self, values=('0', '1', '2'), width=5)
        self.wild_weasel_sam_cbx.set('0')

        self.aaa_vs_helos = BooleanVar()
        self.aaa_vs_helos.set(False)
        self.aaa_vs_helos_chk = Checkbutton(self, text='AAA vs Helos', variable=self.aaa_vs_helos)

        self.ciws = BooleanVar()
        self.ciws.set(False)
        self.ciws_chk = Checkbutton(self, text='CIWS', variable=self.ciws)

        self.usn_ciws = BooleanVar()
        self.usn_ciws.set(False)
        self.usn_ciws_chk = Checkbutton(self, text='USN CIWS', variable=self.usn_ciws)

        self.aaa_vs_transport = BooleanVar()
        self.aaa_vs_transport.set(False)
        self.aaa_vs_transport_chk = Checkbutton(self, text='AAA vs Transport', variable=self.aaa_vs_transport)

        self.aaa_vs_stealth = BooleanVar()
        self.aaa_vs_stealth.set(False)
        self.aaa_vs_stealth_chk = Checkbutton(self, text='AAA vs Stealth', variable=self.aaa_vs_stealth)

        self.detection_lbl.place(x=50, y=30)
        self.awacs_lbl.place(x=50, y=60)
        self.near_HQ_chk.place(x=50, y=90)
        self.passed_occ_chk.place(x=50, y=120)
        self.vs_helos_chk.place(x=50, y=150)
        self.EZOC_landing_chk.place(x=50, y=180)
        self.vs_para_chk.place(x=50, y=210)
        self.mountain_chk.place(x=50, y=240)
        self.cruise_chk.place(x=50, y=270)
        self.stealth_chk.place(x=50, y=300)
        self.wild_weasel_det_lbl.place(x=50, y=330)
        self.calculate_detection_btn.place(x=50, y=360)
        self.detection_drm_lbl.place(x=50, y=390)
        self.detection_dice_lbl.place(x=50, y=420)
        self.detection_result_lbl.place(x=50, y=450)
        self.detection_cbx.place(x=150, y=30)
        self.awacs_cbx.place(x=150, y=60)
        self.wild_weasel_det_cbx.place(x=150, y=330)
        self.det_drm_ent.place(x=150, y=390)
        self.det_dice_ent.place(x=150, y=420)
        self.det_result_ent.place(x=150, y=450)
        self.weather_lbl.place(x=250, y=330)
        self.actual_weather_clear_r.place(x=250, y=360)
        self.actual_weather_overcast_r.place(x=250, y=390)
        self.actual_weather_storm_r.place(x=250, y=420)
        self.sam_lbl.place(x=250, y=30)
        self.SAM_HQ_chk.place(x=250, y=60)
        self.helo_over_enemy_chk.place(x=250, y=90)
        self.sam_vs_cruise_chk.place(x=250, y=120)
        self.sam_vs_stealth_chk.place(x=250, y=150)
        self.wild_weasel_sam_lbl.place(x=250, y=180)
        self.sam_defence_btn.place(x=250, y=210)
        self.sam_drm_lbl.place(x=250, y=240)
        self.sam_dice_lbl.place(x=250, y=270)
        self.sam_result_lbl.place(x=250, y=300)
        self.sam_cbx.place(x=350, y=30)
        self.wild_weasel_sam_cbx.place(x=350, y=180)
        self.sam_drm_ent.place(x=350, y=240)
        self.sam_dice_ent.place(x=350, y=270)
        self.sam_result_ent.place(x=350, y=300)
        self.aaa_value_lbl.place(x=450, y=30)
        self.aaa_vs_helos_chk.place(x=450, y=60)
        self.ciws_chk.place(x=450, y=90)
        self.usn_ciws_chk.place(x=450, y=120)
        self.aaa_vs_transport_chk.place(x=450, y=150)
        self.aaa_vs_stealth_chk.place(x=450, y=180)
        self.aaa_defence_btn.place(x=450, y=210)
        self.aaa_drm_lbl.place(x=450, y=240)
        self.aaa_dice_lbl.place(x=450, y=270)
        self.aaa_result_lbl.place(x=450, y=300)
        self.aaa_value_cbx.place(x=550, y=30)
        self.aaa_drm_ent.place(x=550, y=240)
        self.aaa_dice_ent.place(x=550, y=270)
        self.aaa_result_ent.place(x=550, y=300)

    def calculate_detection(self):

        self.det_drm_ent.delete(0, 'end')
        self.det_dice_ent.delete(0, 'end')
        self.det_result_ent.delete(0, 'end')
        detection_value = self.detection_cbx.get()
        column = DETECTION_TO_COLUMN[detection_value]

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
            awacs = awacs_to_num[self.awacs_cbx.get()]
            DRM += awacs
        weasel = int(self.wild_weasel_det_cbx.get())
        DRM += weasel
        row = d10 + DRM
        if row < 0:
            row = 0
        if row > 9:
            row = 9
        result = ADVANCED_DETECTION_TABLE[column][row]
        self.det_drm_ent.insert(END, str(DRM))
        self.det_dice_ent.insert(END, str(d10))
        self.det_result_ent.insert(END, result)

    def sam_defence(self):

        self.sam_drm_ent.delete(0, 'end')
        self.sam_dice_ent.delete(0, 'end')
        self.sam_result_ent.delete(0, 'end')

        column = SAM_VALUE_TO_COLUMN[self.sam_cbx.get()]

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
        weasel = int(self.wild_weasel_sam_cbx.get())
        DRM += 2 * weasel
        row = d10 + DRM
        if row < 0:
            row = 0
        if row > 10:
            row = 10
        result = ADVANCED_SAM_TABLE[column][row]
        self.sam_drm_ent.insert(END, str(DRM))
        self.sam_dice_ent.insert(END, str(d10))
        self.sam_result_ent.insert(END, result)

    def aaa_defence(self):

        self.aaa_drm_ent.delete(0, 'end')
        self.aaa_dice_ent.delete(0, 'end')
        self.aaa_result_ent.delete(0, 'end')

        column = AAA_VALUE_TO_COLUMN[self.aaa_value_cbx.get()]

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

        result = ADVANCED_AAA_TABLE[column][row]

        self.aaa_drm_ent.insert(END, str(DRM))
        self.aaa_dice_ent.insert(END, str(d10))
        self.aaa_result_ent.insert(END, result)
