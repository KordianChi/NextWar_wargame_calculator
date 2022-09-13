from tkinter import Toplevel, BooleanVar, IntVar, END
from tkinter.ttk import Combobox, Label, Checkbutton, Radiobutton, Entry
from tkinter import Button
from random import randint
from constants import NAVAL_ATTACK_TYPE_TO_ROW, ADVANCED_STRIKE_TABLE, NAVAL_ATTACK_TYPE, AIR_ADV_SEA


class NavalWarfare(Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title('Advanced Naval Warfare Calculator')
        self.geometry("820x600+10+10")

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
        self.naval_strike_d10_ent.insert(END, '0')

        self.naval_strike_drm_lbl = Label(self, text='Strike DRM:')
        self.naval_strike_drm_ent = Entry(self, width=7)
        self.naval_strike_drm_ent.insert(END, '0')

        self.naval_strike_result_lbl = Label(self, text='Strike Result:')
        self.naval_strike_result_ent = Entry(self, width=7)
        self.naval_strike_result_ent.insert(END, '0')

        self.non_allied_cv_sag_lbl = Label(self, text='Non-allied CV/SAG:')
        self.non_allied_cv_sag_ent = Entry(self, width=7)
        self.non_allied_cv_sag_ent.insert(END, '0')

        self.allied_sag_lbl = Label(self, text='Allied Naval/non-CVN:')
        self.allied_sag_ent = Entry(self, width=7)
        self.allied_sag_ent.insert(END, '0')

        self.allied_cv_lbl = Label(self, text='Allied CVN BG:')
        self.allied_cv_ent = Entry(self, width=7)
        self.allied_cv_ent.insert(END, '0')

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
        self.sea_control_d10_ent.insert(END, '0')

        self.sea_control_drm_lbl = Label(self, text='Sea control DRM:')
        self.sea_control_drm_ent = Entry(self, width=7)
        self.sea_control_drm_ent.insert(END, '0')

        self.sea_control_result_lbl = Label(self, text='Sea control result:')
        self.sea_control_result_ent = Entry(self, width=10)
        self.sea_control_result_ent.insert(END, '0')

        self.own_cv_sag_lbl = Label(self, text='Own CV/SAG:')
        self.own_cv_sag_ent = Entry(self, width=7)
        self.own_cv_sag_ent.insert(END, '0')

        self.enemy_cv_sag_lbl = Label(self, text='Enemy CV/SAG:')
        self.enemy_cv_sag_ent = Entry(self, width=7)
        self.enemy_cv_sag_ent.insert(END, '0')

        self.air_supremacy_lbl = Label(self, text='Air Supremacy:')
        self.air_supremacy_cbx = Combobox(self, values=('-', 'Enemy', 'Own'), width=7)
        self.air_supremacy_cbx.set('-')

        self.cruise_contested_prc = BooleanVar()
        self.cruise_contested_prc.set(False)
        self.cruise_contested_prc_chk = Checkbutton(self, text='PRC cruise', variable=self.cruise_contested_prc)

        self.cruise_contested_ph = BooleanVar()
        self.cruise_contested_ph.set(False)
        self.cruise_contested_ph_chk = Checkbutton(self, text='PH cruise', variable=self.cruise_contested_ph)

        self.own_sub_move = BooleanVar()
        self.own_sub_move.set(False)
        self.own_sub_move_chk = Checkbutton(self, text='Allied submarine', variable=self.own_sub_move)

        self.enemy_sub_move = BooleanVar()
        self.enemy_sub_move.set(False)
        self.enemy_sub_move_chk = Checkbutton(self, text='Non-allied submarine', variable=self.enemy_sub_move)

        self.inshore_control_lbl = Label(self, text='Inshore Control:')
        self.inshore_control_cbx = Combobox(self, values=('-', 'Enemy', 'Own'), width=7)
        self.inshore_control_cbx.set('-')

        self.naval_move_result_btn = Button(self, text='Move', command=self.contested_sea)

        self.naval_move_d10_lbl = Label(self, text='d10:')
        self.naval_move_d10_ent = Entry(self, width=7)
        self.naval_move_d10_ent.insert(END, '0')

        self.naval_move_drm_lbl = Label(self, text='Move DRM:')
        self.naval_move_drm_ent = Entry(self, width=7)
        self.naval_move_drm_ent.insert(END, '0')

        self.naval_move_result_lbl = Label(self, text='Move Result:')
        self.naval_move_result_ent = Entry(self, width=12)
        self.naval_move_result_ent.insert(END, '0')

        self.naval_detection_lbl = Label(self, text='Naval detection')

        self.map_drm_detection_lbl = Label(self, text='Map DRM:')
        self.map_drm_detection_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=4)
        self.map_drm_detection_cbx.set('0')

        self.awacs_adv_detection_lbl = Label(self, text='PRC AWACS advantage:')
        self.awacs_adv_detection_ent = Entry(self, width=7)
        self.awacs_adv_detection_ent.insert(END, '0')

        self.inshore_at_sea_detection = BooleanVar()
        self.inshore_at_sea_detection.set(False)
        self.inshore_at_sea_detection_chk = Checkbutton(self, text='Friendly in inshore',
                                                        variable=self.inshore_at_sea_detection)

        self.air_advantage_detection = BooleanVar()
        self.air_advantage_detection.set(False)
        self.air_advantage_detection_chk = Checkbutton(self, text='Any air advantage',
                                                       variable=self.air_advantage_detection)

        self.friendly_unit_in_loc_lbl = Label(self, text='Per friendly unit in location:')
        self.friendly_unit_in_loc_ent = Entry(self, width=7)
        self.friendly_unit_in_loc_ent.insert(END, '0')

        self.usn_cvn = BooleanVar()
        self.usn_cvn.set(False)
        self.usn_cvn_chk = Checkbutton(self, text='USN CVN BG', variable=self.usn_cvn)

        self.naval_detection_btn = Button(self, text='Detection', command=self.naval_detection)

        self.naval_detection_d10_lbl = Label(self, text='d10 Detection:')
        self.naval_detection_d10_ent = Entry(self, width=7)
        self.naval_detection_d10_ent.insert(END, '0')

        self.naval_detection_drm_lbl = Label(self, text='DRM Detection:')
        self.naval_detection_drm_ent = Entry(self, width=7)
        self.naval_detection_drm_ent.insert(END, '0')

        self.naval_detection_result_lbl = Label(self, text='Detection Result:')
        self.naval_detection_result_ent = Entry(self, width=15)
        self.naval_detection_result_ent.insert(END, '0')

        self.sub_survival_lbl = Label(self, text='Survival value:')
        self.sub_survival_cbx = Combobox(self, values=('7', '6', '5', '4'), width=4)
        self.sub_survival_cbx.set('0')

        self.enemy_unit_in_loc_lbl = Label(self, text='Per enemy SAG/CV:')
        self.enemy_unit_in_loc_ent = Entry(self, width=7)
        self.enemy_unit_in_loc_ent.insert(END, '0')

        self.enemy_cvn_in_loc_lbl = Label(self, text='Per enemy CVN:')
        self.enemy_cvn_in_loc_ent = Entry(self, width=7)
        self.enemy_cvn_in_loc_ent.insert(END, '0')

        self.enemy_air_supremacy = BooleanVar()
        self.enemy_air_supremacy.set(False)
        self.enemy_air_supremacy_chk = Checkbutton(self, text='Enemy air supremacy', variable=self.enemy_air_supremacy)

        self.marker_revealed = BooleanVar()
        self.marker_revealed.set(False)
        self.marker_revealed_chk = Checkbutton(self, text='Unit is revealed', variable=self.marker_revealed)

        self.enemy_sub_vs_sub = BooleanVar()
        self.enemy_sub_vs_sub.set(False)
        self.enemy_sub_vs_sub_chk = Checkbutton(self, text='Enemy sub at box', variable=self.enemy_sub_vs_sub)

        self.enemy_map_drm_detection_lbl = Label(self, text='Enemy Map DRM:')
        self.enemy_map_drm_detection_cbx = Combobox(self, values=('-2', '-1', '0', '1', '2'), width=4)
        self.enemy_map_drm_detection_cbx.set('0')

        self.asw_survival_result_btn = Button(self, text='Survival', command=self.asw_survival)

        self.asw_survival_d10_lbl = Label(self, text='d10:')
        self.asw_survival_d10_ent = Entry(self, width=7)
        self.asw_survival_d10_ent.insert(END, '0')

        self.asw_survival_drm_lbl = Label(self, text='Survival DRM:')
        self.asw_survival_drm_ent = Entry(self, width=7)
        self.asw_survival_drm_ent.insert(END, '0')

        self.asw_survival_result_lbl = Label(self, text='Survival result:')
        self.asw_survival_result_ent = Entry(self, width=10)
        self.asw_survival_result_ent.insert(END, '0')

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
        self.naval_strike_result_btn.place(x=20, y=280)
        self.naval_strike_d10_lbl.place(x=20, y=310)
        self.naval_strike_d10_ent.place(x=110, y=310)
        self.naval_strike_drm_lbl.place(x=20, y=340)
        self.naval_strike_drm_ent.place(x=110, y=340)
        self.naval_strike_result_lbl.place(x=20, y=370)
        self.naval_strike_result_ent.place(x=110, y=370)
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

        self.naval_detection_lbl.place(x=600, y=10)
        self.map_drm_detection_lbl.place(x=600, y=40)
        self.map_drm_detection_cbx.place(x=750, y=40)
        self.awacs_adv_detection_lbl.place(x=600, y=70)
        self.awacs_adv_detection_ent.place(x=750, y=70)
        self.inshore_at_sea_detection_chk.place(x=600, y=100)
        self.air_advantage_detection_chk.place(x=600, y=130)
        self.friendly_unit_in_loc_lbl.place(x=600, y=160)
        self.friendly_unit_in_loc_ent.place(x=750, y=160)
        self.usn_cvn_chk.place(x=600, y=190)
        self.naval_detection_btn.place(x=600, y=220)
        self.naval_detection_d10_lbl.place(x=600, y=250)
        self.naval_detection_d10_ent.place(x=700, y=250)
        self.naval_detection_drm_lbl.place(x=600, y=280)
        self.naval_detection_drm_ent.place(x=700, y=280)
        self.naval_detection_result_lbl.place(x=600, y=310)
        self.naval_detection_result_ent.place(x=700, y=310)

        self.own_cv_sag_lbl.place(x=410, y=10)
        self.own_cv_sag_ent.place(x=500, y=10)
        self.enemy_cv_sag_lbl.place(x=410, y=40)
        self.enemy_cv_sag_ent.place(x=500, y=40)
        self.air_supremacy_lbl.place(x=410, y=70)
        self.air_supremacy_cbx.place(x=500, y=70)
        self.cruise_contested_prc_chk.place(x=410, y=100)
        self.cruise_contested_ph_chk.place(x=410, y=130)
        self.own_sub_move_chk.place(x=410, y=160)
        self.enemy_sub_move_chk.place(x=410, y=190)
        self.inshore_control_lbl.place(x=410, y=220)
        self.inshore_control_cbx.place(x=500, y=220)
        self.naval_move_result_btn.place(x=410, y=250)
        self.naval_move_d10_lbl.place(x=410, y=280)
        self.naval_move_d10_ent.place(x=500, y=280)
        self.naval_move_drm_lbl.place(x=410, y=310)
        self.naval_move_drm_ent.place(x=500, y=310)
        self.naval_move_result_lbl.place(x=410, y=340)
        self.naval_move_result_ent.place(x=500, y=340)

        self.weather_lbl.place(x=200, y=370)
        self.clear_weather_rb.place(x=200, y=400)
        self.overcast_weather_rb.place(x=200, y=430)
        self.storm_weather_rb.place(x=200, y=460)

        self.sub_survival_lbl.place(x=600, y=370)
        self.sub_survival_cbx.place(x=710, y=370)
        self.enemy_map_drm_detection_lbl.place(x=600, y=400)
        self.enemy_map_drm_detection_cbx.place(x=710, y=400)
        self.enemy_unit_in_loc_lbl.place(x=600, y=430)
        self.enemy_unit_in_loc_ent.place(x=710, y=430)
        self.enemy_cvn_in_loc_lbl.place(x=600, y=460)
        self.enemy_cvn_in_loc_ent.place(x=710, y=460)
        self.enemy_air_supremacy_chk.place(x=600, y=490)
        self.marker_revealed_chk.place(x=600, y=520)
        self.enemy_sub_vs_sub_chk.place(x=600, y=520)

        self.asw_survival_result_btn.place(x=410, y=400)
        self.asw_survival_d10_lbl.place(x=410, y=430)
        self.asw_survival_d10_ent.place(x=500, y=430)
        self.asw_survival_drm_lbl.place(x=410, y=460)
        self.asw_survival_drm_ent.place(x=500, y=460)
        self.asw_survival_result_lbl.place(x=410, y=490)
        self.asw_survival_result_ent.place(x=500, y=490)

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

        if self.actual_weather.get() == 3:
            drm_strike += 3

        if self.actual_weather.get() == 2:
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

    def contested_sea(self):

        self.naval_move_d10_ent.delete(0, 'end')
        self.naval_move_drm_ent.delete(0, 'end')
        self.naval_move_result_ent.delete(0, 'end')

        drm_move = 0
        drm_move -= int(self.own_cv_sag_ent.get())
        drm_move += int(self.enemy_cv_sag_ent.get())
        
        if self.cruise_contested_prc.get():
            drm_move += 1
        if self.cruise_contested_ph.get():
            drm_move += 1
        if self.own_sub_move.get():
            drm_move -= 1
        if self.enemy_sub_move.get():
            drm_move += 1
        if self.inshore_control_cbx.get() == 'Own':
            drm_move -= 1
        if self.inshore_control_cbx.get() == 'Enemy':
            drm_move += 1
        if self.air_supremacy_cbx.get() == 'Own':
            drm_move -= 1
        if self.air_supremacy_cbx.get() == 'Enemy':
            drm_move += 1

        d10_move = randint(0, 9)
        move = d10_move + drm_move

        if move > 8:
            result = 'Abort/Strike 2'
        elif move > 5:
            result = 'Abort/Strike 1'
        else:
            result = '-'

        self.naval_move_d10_ent.insert(END, str(d10_move))
        self.naval_move_drm_ent.insert(END, str(drm_move))
        self.naval_move_result_ent.insert(END, str(result))

    def naval_detection(self):

        self.naval_detection_d10_ent.delete(0, 'end')
        self.naval_detection_drm_ent.delete(0, 'end')
        self.naval_detection_result_ent.delete(0, 'end')

        drm_detection = 0

        if self.actual_weather.get() == 3:
            drm_detection += 3

        if self.actual_weather.get() == 2:
            drm_detection += 1

        drm_detection += int(self.map_drm_detection_cbx.get())
        drm_detection -= int(self.awacs_adv_detection_ent.get())

        if self.air_advantage_detection.get():
            drm_detection -= 1

        drm_detection -= int(self.awacs_adv_detection_ent.get())

        if self.inshore_at_sea_detection.get():
            drm_detection -= 1

        if self.air_advantage_detection.get():
            drm_detection -= 1

        drm_detection -= int(self.friendly_unit_in_loc_ent.get())

        if self.usn_cvn.get():
            drm_detection -= 2

        d10_detection = randint(0, 9)

        number = d10_detection + drm_detection

        if number < 3:
            result = 'Point detection'

        elif number > 6:
            result = 'No detection'

        else:
            result = 'Area detection'

        self.naval_detection_d10_ent.insert(END, str(d10_detection))
        self.naval_detection_drm_ent.insert(END, str(drm_detection))
        self.naval_detection_result_ent.insert(END, str(result))

    def asw_survival(self):

        self.asw_survival_d10_ent.delete(0, 'end')
        self.asw_survival_drm_ent.delete(0, 'end')
        self.asw_survival_result_ent.delete(0, 'end')

        drm_survival = 0

        drm_survival += int(self.enemy_unit_in_loc_ent.get())
        drm_survival += 2 * int(self.enemy_cvn_in_loc_ent.get())

        if self.marker_revealed.get():
            drm_survival += 1

        if self.enemy_air_supremacy.get():
            drm_survival += 1

        if self.enemy_sub_vs_sub.get():
            drm_survival += 2

        drm_survival -= int(self.enemy_map_drm_detection_cbx.get())

        d10_sub = randint(0, 9)

        number = d10_sub + drm_survival
        asw_value = int(self.sub_survival_cbx.get())

        if asw_value == number:
            result = 'Strike 1'
        elif asw_value < number and 2 * asw_value > number:
            result = 'Strike 2'
        elif 2 * asw_value < number:
            result = 'Destroyed'
        else:
            result = '-'

        self.asw_survival_d10_ent.insert(END, str(d10_sub))
        self.asw_survival_drm_ent.insert(END, str(drm_survival))
        self.asw_survival_result_ent.insert(END, str(result))



