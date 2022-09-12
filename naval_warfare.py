from tkinter import Toplevel, BooleanVar, IntVar, END
from tkinter.ttk import Combobox, Label, Checkbutton, Radiobutton, Button, Entry
from random import randint
from constants import NAVAL_ATTACK_TYPE_TO_ROW, ADVANCED_STRIKE_TABLE, NAVAL_ATTACK_TYPE, AIR_ADV_SEA


class NavalWarfare(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Advanced Naval Warfare Calculator')
        self.geometry("620x550+10+10")

        self.attack_type_lbl = Label(self, text='Naval attack type:')
        self.attack_type_cbx = Combobox(self, values=NAVAL_ATTACK_TYPE, width=7)
        self.attack_type_cbx.set('Naval 1')

        self.non_us_cruise = BooleanVar()
        self.non_us_cruise.set(False)
        self.non_us_cruise_chk = Checkbutton(self, text='non-US cruise strike', variable=self.non_us_cruise)

        self.pilot_skills_lbl = Label(self, text='Pilot skills:')
        self.pilot_skills_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=5)
        self.pilot_skills_cbx.set('0')

        self.aa_result_lbl = Label(self, text='AA result:')
        self.aa_result_cbx = Combobox(self, values=('0', '1', '2', '3', '4'), width=5)
        self.aa_result_cbx.set('0')

        self.naval_air_unit = BooleanVar()
        self.naval_air_unit.set(False)
        self.naval_air_unit_chk = Checkbutton(self, text='Naval air unit strike', variable=self.naval_air_unit)

        self.point_detection = BooleanVar()
        self.point_detection.set(False)
        self.point_detection_chk = Checkbutton(self, text='Point detected', variable=self.point_detection)

        self.non_stand_off = BooleanVar()
        self.non_stand_off.set(False)
        self.non_stand_off_chk = Checkbutton(self, text='non-stand-off air strike', variable=self.non_stand_off)

        self.cruise_attack = BooleanVar()
        self.cruise_attack.set(False)
        self.cruise_attack_chk = Checkbutton(self, text='Cruise strike', variable=self.cruise_attack)

        self.striker_marker_lbl = Label(self, text='Strike marker:')
        self.striker_marker_cbx = Combobox(self, values=('0', '1', '2'), width=5)
        self.striker_marker_cbx.set('0')

        self.weather_lbl = Label(self, text='Weather:')
        self.actual_weather = IntVar()
        self.actual_weather.set(1)
        self.clear_weather_rb = Radiobutton(self, text="Clear", variable=self.actual_weather, value=1)
        self.overcast_weather_rb = Radiobutton(self, text="Overcast", variable=self.actual_weather, value=2)
        self.storm_weather_rb = Radiobutton(self, text="Storm", variable=self.actual_weather, value=3)

        self.naval_strike_result_btn = Button(self, text='Strike!', command=self.naval_strike)

        self.naval_strike_d10_lbl = Label(self, text='d10:')
        self.naval_strike_d10_ent = Entry(self, width=7)

        self.naval_strike_drm_lbl = Label(self, text='Strike DRM:')
        self.naval_strike_drm_ent = Entry(self, width=7)

        self.naval_strike_result_lbl = Label(self, text='Strike Result:')
        self.naval_strike_result_ent = Entry(self, width=7)

        self.non_allied_cv_sag_lbl = Label(self, text='Non-allied CV/SAG:')
        self.non_allied_cv_sag_ent = Entry(self, width=7)

        self.allied_sag_lbl = Label(self, text='Allied Naval/non-CVN:')
        self.allied_sag_ent = Entry(self, width=7)

        self.allied_cv_lbl = Label(self, text='Allied CVN BG:')
        self.allied_cv_ent = Entry(self, width=7)

        self.allied_sub = BooleanVar()
        self.allied_sub.set(False)
        self.allied_sub_chk = Checkbutton(self, text='Allied submarine', variable=self.allied_sub)

        self.non_allied_sub = BooleanVar()
        self.non_allied_sub.set(False)
        self.non_allied_sub_chk = Checkbutton(self, text='Non-allied submarine', variable=self.non_allied_sub)

        self.air_adv_lbl = Label(self, text='Air advantage:')
        self.air_adv_cbx = Combobox(self, values=('-', 'Allied Air Superiority', 'Allied Air Supremacy',
                                                  'Non-allied Air Superiority', 'Non-allied Air Supremacy'), width=15)
        self.air_adv_cbx.set('-')

        self.prc_cruise_lbl = Label(self, text='PRC cruise:')
        self.prc_cruise_cbx = Combobox(self, values=('0', '-1', '-2'), width=7)
        self.prc_cruise_cbx.set('0')
        self.island_land_lbl = Label(self, text='Island control:')
        self.island_land_cbx = Combobox(self, values=('-', 'Allied', 'Non-allied'), width=7)
        self.island_land_cbx.set('-')

        self.sea_control_result_btn = Button(self, text='Control', command=self.sea_control)

        self.sea_control_d10_lbl = Label(self, text='d10:')
        self.sea_control_d10_ent = Entry(self, width=7)

        self.sea_control_drm_lbl = Label(self, text='Sea control DRM:')
        self.sea_control_drm_ent = Entry(self, width=7)

        self.sea_control_result_lbl = Label(self, text='Sea control result:')
        self.sea_control_result_ent = Entry(self, width=10)

        self.attack_type_cbx.place(x=120, y=10)
        self.attack_type_lbl.place(x=20, y=10)
        self.non_us_cruise_chk.place(x=20, y=40)
        self.naval_air_unit_chk.place(x=20, y=70)
        self.point_detection_chk.place(x=20, y=100)
        self.non_stand_off_chk.place(x=20, y=130)
        self.cruise_attack_chk.place(x=20, y=160)
        self.striker_marker_lbl.place(x=20, y=190)
        self.striker_marker_cbx.place(x=110, y=190)
        self.pilot_skills_lbl.place(x=20, y=220)
        self.pilot_skills_cbx.place(x=110, y=220)
        self.aa_result_lbl.place(x=20, y=250)
        self.aa_result_cbx.place(x=110, y=250)
        self.weather_lbl.place(x=20, y=280)
        self.clear_weather_rb.place(x=110, y=280)
        self.overcast_weather_rb.place(x=110, y=310)
        self.storm_weather_rb.place(x=110, y=340)
        self.naval_strike_result_btn.place(x=20, y=370)
        self.naval_strike_d10_lbl.place(x=20, y=400)
        self.naval_strike_d10_ent.place(x=110, y=400)
        self.naval_strike_drm_lbl.place(x=20, y=430)
        self.naval_strike_drm_ent.place(x=110, y=430)
        self.naval_strike_result_lbl.place(x=20, y=460)
        self.naval_strike_result_ent.place(x=110, y=460)
        self.allied_sag_lbl.place(x=200, y=10)
        self.allied_sag_ent.place(x=330, y=10)
        self.non_allied_cv_sag_lbl.place(x=200, y=40)
        self.non_allied_cv_sag_ent.place(x=330, y=40)
        self.allied_cv_lbl.place(x=200, y=70)
        self.allied_cv_ent.place(x=330, y=70)
        self.allied_sub_chk.place(x=200, y=100)
        self.non_allied_sub_chk.place(x=200, y=130)
        self.air_adv_lbl.place(x=200, y=160)
        self.air_adv_cbx.place(x=280, y=160)
        self.prc_cruise_lbl.place(x=200, y=190)
        self.prc_cruise_cbx.place(x=280, y=190)
        self.island_land_lbl.place(x=200, y=220)
        self.island_land_cbx.place(x=280, y=220)
        self.sea_control_result_btn.place(x=200, y=250)
        self.sea_control_d10_lbl.place(x=200, y=280)
        self.sea_control_d10_ent.place(x=300, y=280)
        self.sea_control_drm_lbl.place(x=200, y=310)
        self.sea_control_drm_ent.place(x=300, y=310)
        self.sea_control_result_lbl.place(x=200, y=340)
        self.sea_control_result_ent.place(x=300, y=340)

    def naval_strike(self):

        self.naval_strike_d10_ent.delete(0, 'end')
        self.naval_strike_drm_ent.delete(0, 'end')
        self.naval_strike_result_ent.delete(0, 'end')

        column = NAVAL_ATTACK_TYPE_TO_ROW[self.attack_type_cbx.get()]

        d10_strike = randint(0, 9)
        drm_strike = 0

        if self.non_us_cruise.get():
            drm_strike += 1

        if self.cruise_attack.get():
            drm_strike += 1

        if self.naval_air_unit.get():
            drm_strike -= 1

        if self.non_stand_off.get():
            drm_strike -= 1

        if self.point_detection.get():
            drm_strike -= 1

        if self.actual_weather == 3:
            drm_strike += 3

        if self.actual_weather == 2:
            drm_strike += 2

        drm_strike += int(self.striker_marker_cbx.get())
        drm_strike += int(self.pilot_skills_cbx.get())
        drm_strike += int(self.aa_result_cbx.get())

        row = d10_strike + drm_strike
        if row > 7:
            row = 7
        if row < -2:
            row = -2
        row += 2
        result = ADVANCED_STRIKE_TABLE[column][row]

        self.naval_strike_d10_ent.insert(END, str(d10_strike))
        self.naval_strike_drm_ent.insert(END, str(drm_strike))
        self.naval_strike_result_ent.insert(END, str(result))

    def sea_control(self):

        self.sea_control_d10_ent.delete(0, 'end')
        self.sea_control_drm_ent.delete(0, 'end')
        self.sea_control_result_ent.delete(0, 'end')

        drm_control = 0
        drm_control -= int(self.non_allied_cv_sag_ent.get())
        drm_control += 2 * int(self.allied_cv_ent.get())
        drm_control += int(self.allied_sag_ent.get())

        if self.non_allied_sub.get():
            drm_control -= 2

        if self.allied_sub.get():
            drm_control += 2

        drm_control += int(self.prc_cruise_cbx.get())
        drm_control += AIR_ADV_SEA[self.air_adv_cbx.get()]
        if self.island_land_cbx.get() == 'Allied':
            drm_control += 1
        if self.island_land_cbx.get() == 'Non-allied':
            drm_control -= 1
        d10_control = randint(0, 9)
        if d10_control + drm_control < 3:
            result = 'Non-allied'
        elif d10_control + drm_control > 5:
            result = 'Allied'
        else:
            result = 'Contested'

        self.sea_control_d10_ent.insert(END, str(d10_control))
        self.sea_control_drm_ent.insert(END, str(drm_control))
        self.sea_control_result_ent.insert(END, str(result))
