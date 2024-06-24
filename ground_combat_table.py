from tkinter import Label, BooleanVar, Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter.ttk import Combobox, Checkbutton
from math import ceil, floor
from random import randint
from constants import COMBAT_RESULT_TABLE, TERRAIN_TO_TYPE, TERRAIN_TO_SHIFT, FRAC_TO_ORDER,\
    ORDER_TO_FRAC, ODDS_TO_COLUMN, DEFENDER_RETREAT_CHANCE, ATTACKER_LOSS_TABLE, DEFENDER_LOSS_TABLE


class CombatResultTable(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Combat Result Table')
        self.geometry("940x670+10+10")

        self.attacker_number = 1
        self.defender_number = 1
        self.y_for_attacker = 280
        self.y_for_defender = 40
        self.attacker_data = []
        self.defender_data = []
        self.clear_all_btn = Button(self, text='Clear all', command=self.clear)
        self.add_attacker_btn = Button(self, text='Add attacker', command=self.add_attacker)
        self.attacker_efficiency_lbl = Label(self, text='Attacker efficiency:')
        self.attacker_efficiency_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6', '7', '8'), width=4)
        self.attacker_efficiency_cbx.set('1')
        self.add_defender_btn = Button(self, text='Add defender', command=self.add_defender)
        self.defender_efficiency_lbl = Label(self, text='Defender efficiency:')
        self.defender_efficiency_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6', '7', '8'), width=4)
        self.defender_efficiency_cbx.set('1')

        self.attacker_hq_lbl = Label(self, text='Attacker HQ:')
        self.attacker_hq_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), width=4)
        self.attacker_hq_cbx.set('0')

        self.defender_hq_lbl = Label(self, text='Defender HQ:')
        self.defender_hq_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5'), width=4)
        self.defender_hq_cbx.set('0')

        self.calculate_power_btn = Button(self, text='Combat values', command=self.calculate)

        self.calculate_att_lbl = Label(self, text='Att value:')
        self.calculate_att_ent = Entry(self, width=5)
        self.calculate_att_ent.insert(END, '0')

        self.calculate_def_lbl = Label(self, text='Def value:')
        self.calculate_def_ent = Entry(self, width=5)
        self.calculate_def_ent.insert(END, '0')

        self.calculate_col_shift_lbl = Label(self, text='Shift:')
        self.calculate_col_shift_ent = Entry(self, width=5)
        self.calculate_col_shift_ent.insert(END, '0')

        self.calculate_drm_lbl = Label(self, text='DRM:')
        self.calculate_drm_ent = Entry(self, width=5)
        self.calculate_drm_ent.insert(END, '0')
        

        self.terrain_cbx = Combobox(self, values=('Flat', 'Flat Woods', 'Rough', 'Rough Woods', 'Marsh',
                                                  'Highlands', 'Jungle', 'Highland Woods',
                                                  'Mountain', 'Urban'), width=15)
        self.terrain_cbx.set('Flat')

        self.in_city = BooleanVar()
        self.in_city.set(False)
        self.in_city_chk = Checkbutton(self, text='Defender in city', variable=self.in_city)


        self.is_fortified = BooleanVar()
        self.is_fortified.set(False)
        self.is_fortified_chk = Checkbutton(self, text='Defender is fortified', variable=self.is_fortified)

        self.amphibious_assault = BooleanVar()
        self.amphibious_assault.set(False)
        self.amphibious_assault_chk = Checkbutton(self, text='Amphibious assault', variable=self.amphibious_assault)

        self.exploit_combat = BooleanVar()
        self.exploit_combat.set(False)
        self.exploit_combat_chk = Checkbutton(self, text='Exploit combat', variable=self.exploit_combat)

        self.surprise_lbl = Label(self, text='Surprise:')
        self.surprise_cbx = Combobox(self, values=('0', '1', '2'), width=4)
        self.surprise_cbx.set('0')

        self.attacker_arty_lbl = Label(self, text='Attacker artillery:')
        self.attacker_arty_cbx = Combobox(self, values=('0', '1', '2'), width=4)
        self.attacker_arty_cbx.set('0')

        self.defender_arty_lbl = Label(self, text='Defender artillery:')
        self.defender_arty_cbx = Combobox(self, values=('0', '1'), width=4)
        self.defender_arty_cbx.set('0')

        self.attacker_helos_lbl = Label(self, text='Attacker Helos:')
        self.attacker_1_helos_cbx = Combobox(self, values=('0', '1', '2'), width=4)
        self.attacker_1_helos_cbx.set('0')
        self.attacker_2_helos_cbx = Combobox(self, values=('0', '1', '2'), width=4)
        self.attacker_2_helos_cbx.set('0')
        self.defender_helos_lbl = Label(self, text='Defender Helos:')
        self.defender_helos_cbx = Combobox(self, values=('0', '1', '2'), width=4)
        self.defender_helos_cbx.set('0')

        self.attacker_aircraft_lbl = Label(self, text='Attacker Aircraft:')
        self.attacker_1_aircraft_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6'), width=4)
        self.attacker_1_aircraft_cbx.set('0')
        self.attacker_2_aircraft_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6'), width=4)
        self.attacker_2_aircraft_cbx.set('0')
        self.defender_aircraft_lbl = Label(self, text='Defender Aircraft:')
        self.defender_aircraft_cbx = Combobox(self, values=('0', '1', '2', '3', '4', '5', '6'), width=4)
        self.defender_aircraft_cbx.set('0')
        self.attacker_navy_lbl = Label(self, text='Attacker Navy:')
        self.attacker_navy_ent = Entry(self, width=7)
        self.attacker_navy_ent.insert(END, '0')

        self.defender_navy_lbl = Label(self, text='Defender Navy:')
        self.defender_navy_ent = Entry(self, width=7)
        self.defender_navy_ent.insert(END, '0')

        self.attacking_5_6_side = BooleanVar()
        self.attacking_5_6_side.set(False)
        self.attacking_5_6_side_chk = Checkbutton(self, text='Attack from 5 or 6 hex', variable=self.attacking_5_6_side)

        self.attacking_3_4_side = BooleanVar()
        self.attacking_3_4_side.set(False)
        self.attacking_3_4_side_chk = Checkbutton(self, text='Attack from 3 or 4 hex', variable=self.attacking_3_4_side)

        self.defender_in_installation = BooleanVar()
        self.defender_in_installation.set(False)
        self.defender_in_installation_chk = Checkbutton(self, text='Defender in installation/airfield/town',
                                                        variable=self.defender_in_installation)

        self.multi_formation_lbl = Label(self, text='Multi-formation:')
        self.multi_formation_ent = Entry(self, width=7)
        self.multi_formation_ent.insert(END, '0')

        self.multi_nation_attack = BooleanVar()
        self.multi_nation_attack.set(False)
        self.multi_nation_attack_chk = Checkbutton(self, text='Multination attack', variable=self.multi_nation_attack)

        self.irop_prc_attack = BooleanVar()
        self.irop_prc_attack.set(False)
        self.irop_prc_attack_chk = Checkbutton(self, text='IROP & PRC attack', variable=self.irop_prc_attack)

        self.attacker_cyber_shift = BooleanVar()
        self.attacker_cyber_shift.set(False)
        self.attacker_cyber_shift_chk = Checkbutton(self, text='Attacker Cyber Warfare',
                                                    variable=self.attacker_cyber_shift)

        self.defender_cyber_shift = BooleanVar()
        self.defender_cyber_shift.set(False)
        self.defender_cyber_shift_chk = Checkbutton(self, text='Defender Cyber Warfare',
                                                    variable=self.defender_cyber_shift)


        self.combat_result_btn = Button(self, text='Combat Result', command=self.combat_result)

        self.combat_odds_lbl = Label(self, text='Combat odds:')
        self.combat_odds_ent = Entry(self, width=7)

        self.combat_result_lbl = Label(self, text='Combat result:')
        self.combat_result_ent = Entry(self, width=7)

        self.reduce_attacker_loss_lbl = Label(self, text='Reduce loss:')
        self.reduce_attacker_loss_ent = Entry(self, width=7)

        self.result_dice_lbl = Label(self, text='Dice:')
        self.result_dice_ent = Entry(self, width=7)

        self.predict_btn = Button(self, text='Predict', command=self.combat_result_predict)

        self.attacker_pred_loss_lbl = Label(self, text='Predict att loss:')
        self.attacker_pred_loss_ent = Entry(self, width=7)
        self.defender_pred_loss_lbl = Label(self, text='Predict def loss:')
        self.defender_pred_loss_ent = Entry(self, width=7)
        self.defender_pred_retreat_lbl = Label(self, text='Retreat chance:')
        self.defender_pred_retreat_ent = Entry(self, width=7)
        
        
        self.defender_aircraft_lbl.place(x=20, y=430)
        self.defender_aircraft_cbx.place(x=130, y=430)
        self.attacker_navy_lbl.place(x=20, y=460)
        self.attacker_navy_ent.place(x=130, y=460)
        self.defender_navy_lbl.place(x=20, y=490)
        self.defender_navy_ent.place(x=130, y=490)
        self.attacking_5_6_side_chk.place(x=200, y=10)
        self.attacking_3_4_side_chk.place(x=200, y=40)
        self.multi_formation_lbl.place(x=200, y=100)
        self.multi_formation_ent.place(x=300, y=100)
        self.multi_nation_attack_chk.place(x=200, y=130)
        self.irop_prc_attack_chk.place(x=200, y=160)
        self.attacker_cyber_shift_chk.place(x=200, y=190)
        self.defender_cyber_shift_chk.place(x=200, y=220)
        self.combat_result_btn.place(x=200, y=280)
        self.combat_odds_lbl.place(x=200, y=320)
        self.combat_odds_ent.place(x=300, y=320)
        self.combat_result_lbl.place(x=200, y=360)
        self.combat_result_ent.place(x=300, y=360)
        self.reduce_attacker_loss_lbl.place(x=200, y=400)
        self.reduce_attacker_loss_ent.place(x=300, y=400)
        self.result_dice_lbl.place(x=200, y=440)
        self.result_dice_ent.place(x=300, y=440)
        self.predict_btn.place(x=20, y=580)
        self.attacker_pred_loss_lbl.place(x=70, y=580)
        self.attacker_pred_loss_ent.place(x=160, y=580)
        self.defender_pred_loss_lbl.place(x=70, y=610)
        self.defender_pred_loss_ent.place(x=160, y=610)
        self.defender_pred_retreat_lbl.place(x=70, y=640)
        self.defender_pred_retreat_ent.place(x=160, y=640)
        self.attacker_2_aircraft_cbx.place(x=130, y=400)
        self.attacker_1_aircraft_cbx.place(x=130, y=370)
        self.attacker_aircraft_lbl.place(x=20, y=370)
        self.defender_helos_cbx.place(x=130, y=340)
        self.defender_helos_lbl.place(x=20, y=340)
        self.attacker_2_helos_cbx.place(x=130, y=310)
        self.attacker_1_helos_cbx.place(x=130, y=280)
        self.attacker_helos_lbl.place(x=20, y=280)
        self.defender_arty_cbx.place(x=130, y=250)
        self.defender_arty_lbl.place(x=20, y=250)
        self.attacker_arty_lbl.place(x=20, y=220)
        self.surprise_cbx.place(x=130, y=190)
        self.surprise_lbl.place(x=20, y=190)
        self.exploit_combat_chk.place(x=20, y=160)
        self.amphibious_assault_chk.place(x=20, y=130)
        self.is_fortified_chk.place(x=20, y=100)
        self.defender_in_installation_chk.place(x=20, y=70)
        self.in_city_chk.place(x=20, y=40)
        self.terrain_cbx.place(x=20, y=10)
        self.clear_all_btn.place(x=20, y=550)
        self.add_attacker_btn.place(x=420, y=250)
        self.attacker_efficiency_lbl.place(x=510, y=250)
        self.attacker_efficiency_cbx.place(x=625, y=250)
        self.add_defender_btn.place(x=420, y=10)
        self.defender_efficiency_lbl.place(x=510, y=10)
        self.defender_efficiency_cbx.place(x=625, y=10)
        self.attacker_hq_lbl.place(x=675, y=250)
        self.attacker_hq_cbx.place(x=755, y=250)
        self.defender_hq_lbl.place(x=675, y=10)
        self.defender_hq_cbx.place(x=755, y=10)
        self.calculate_power_btn.place(x=20, y=520)
        self.calculate_att_lbl.place(x=120, y=520)
        self.calculate_att_ent.place(x=190, y=520)
        self.calculate_def_lbl.place(x=230, y=520)
        self.calculate_def_ent.place(x=300, y=520)
        self.calculate_col_shift_lbl.place(x=120, y=550)
        self.calculate_col_shift_ent.place(x=190, y=550)
        self.calculate_drm_lbl.place(x=230, y=550)
        self.calculate_drm_ent.place(x=300, y=550)

        

    def add_attacker(self):
        attacker_lbl = Label(self, text=f'Attacker #{self.attacker_number}')
        attack_value_ent = Entry(self, width=5)
        attack_value_ent.insert(END, '0')
        attacker_type_cbx = Combobox(self, values=('Leg', 'Mechanized', 'Armored', 'Mtn', 'Light'), width=12)
        attacker_type_cbx.set('Leg')
        attacker_supply_cbx = Combobox(self, values=('In-supply', 'Out-supply', 'Isolated'), width=10)
        attacker_supply_cbx.set('In-supply')
        attacker_strike_cbx = Combobox(self, values=('No Strike', 'Strike 1', 'Strike 2'), width=8)
        attacker_strike_cbx.set('No strike')
        
        across_river = BooleanVar()
        across_river.set(False)
        across_river_chk = Checkbutton(self, text='Across river', variable=across_river)
    
        
        self.attacker_data.append([attacker_lbl, attack_value_ent, attacker_type_cbx,
                                   attacker_supply_cbx, attacker_strike_cbx, across_river])
        
        attacker_lbl.place(x=420, y=self.y_for_attacker)
        attack_value_ent.place(x=495, y=self.y_for_attacker)
        attacker_type_cbx.place(x=555, y=self.y_for_attacker)
        attacker_supply_cbx.place(x=655, y=self.y_for_attacker)
        attacker_strike_cbx.place(x=755, y=self.y_for_attacker)
        across_river_chk.place(x=830, y=self.y_for_attacker)
        
        self.attacker_number += 1
        self.y_for_attacker += 30

    def add_defender(self):
        defender_lbl = Label(self, text=f'Defender #{self.defender_number}')
        defender_value_ent = Entry(self, width=5)
        defender_value_ent.insert(END, '0')
        defender_type_cbx = Combobox(self, values=('Leg', 'Mechanized', 'Armored', 'Mtn', 'Light'), width=12)
        defender_type_cbx.set('Leg')
        defender_supply_cbx = Combobox(self, values=('In-supply', 'Out-supply', 'Isolated'), width=10)
        defender_supply_cbx.set('In-supply')
        defender_strike_cbx = Combobox(self, values=('No Strike', 'Strike 1', 'Strike 2'), width=8)
        defender_strike_cbx.set('No strike')
        self.defender_data.append([defender_lbl, defender_value_ent, defender_type_cbx,
                                   defender_supply_cbx, defender_strike_cbx])
        
        defender_lbl.place(x=420, y=self.y_for_defender)
        defender_value_ent.place(x=495, y=self.y_for_defender)
        defender_type_cbx.place(x=555, y=self.y_for_defender)
        defender_supply_cbx.place(x=655, y=self.y_for_defender)
        defender_strike_cbx.place(x=755, y=self.y_for_defender)
        
        self.defender_number += 1
        self.y_for_defender += 30

    def clear(self):
        self.y_for_defender = 40
        self.y_for_attacker = 280
        self.calculate_att_ent.delete(0, 'end')
        self.calculate_att_ent.insert(END, '0')
        self.calculate_def_ent.delete(0, 'end')
        self.calculate_def_ent.insert(END, '0')
        self.calculate_col_shift_ent.delete(0, 'end')
        self.calculate_col_shift_ent.insert(END, '0')
        self.calculate_drm_ent.delete(0, 'end')
        self.calculate_drm_ent.insert(END, '0')

        self.combat_result_ent.delete(0, 'end')
        self.combat_odds_ent.delete(0, 'end')
        self.reduce_attacker_loss_ent.delete(0, 'end')
        self.result_dice_ent.delete(0, 'end')

        for widgets in self.attacker_data:
            for widget in widgets:
                widget.destroy()
        for widgets in self.defender_data:
            for widget in widgets:
                widget.destroy()
        self.attacker_data = []
        self.defender_data = []
        self.attacker_number = 1
        self.defender_number = 1

    def calculate(self):
        self.calculate_drm_ent.delete(0, 'end')
        self.calculate_att_ent.delete(0, 'end')
        self.calculate_def_ent.delete(0, 'end')
        self.calculate_col_shift_ent.delete(0, 'end')
        att_sum = 0
        for widgets in self.attacker_data:
            att = int(widgets[1].get())
            if widgets[4].get() == 'Strike 1':
                att -= 1
                if att < 1:
                    att = 1
            if widgets[4].get() == 'Strike 2':
                att -= 2
                if att < 1:
                    att = 1
            if widgets[3].get() != 'In-supply':
                att = att / 2
                att = ceil(att)
            defender_type_list = []
            for element in self.defender_data:
                defender_type_list.append(element[2].get())
            armored_advantage = self.terrain_cbx.get() in ['Flat', 'Rough'] and 'Armored' not in defender_type_list and\
                                'Mechanized' not in defender_type_list \
                                and not self.in_city.get() and not self.is_fortified.get()
            if armored_advantage:
                if widgets[2].get() == 'Armored':
                    att = att * 2
                if widgets[2].get() == 'Mechanized':
                    att = ceil(att * 1.5)
            armored_disadvantage = self.terrain_cbx.get() in ['Marsh', 'Highlands', 'Jungle',
                                                              'Highland Woods', 'Mountain']
            if armored_disadvantage:
                if widgets[2].get() == 'Armored' or widgets[2].get() == 'Mechanized':
                    att = ceil(att / 2)

            if widgets[5].get():
                att = ceil(att / 2)

            att_sum += att
        att_sum += int(self.attacker_hq_cbx.get())

        def_sum = 0
        for widgets in self.defender_data:
            defe = int(widgets[1].get())
            if widgets[4].get() == 'Strike 1':
                defe -= 1
                if defe < 1:
                    defe = 1
            if widgets[4].get() == 'Strike 2':
                defe -= 2
                if defe < 1:
                    defe = 1
            if widgets[3].get() == 'Isolated':
                defe = defe / 2
                defe = ceil(defe)
            if self.terrain_cbx.get() == 'Urban':
                if widgets[2].get() in ['Leg', 'Mtn', 'Light']:
                    defe = defe * 2
            def_sum += defe
        def_sum += int(self.defender_hq_cbx.get())

        col_shift = int(self.attacker_efficiency_cbx.get()) - int(self.defender_efficiency_cbx.get())
        if self.is_fortified.get():
            col_shift -= 2
        if self.in_city.get():
            col_shift -= 2
        if self.amphibious_assault.get():
            col_shift -= 1
        if self.exploit_combat.get():
            col_shift -= 2
        if self.attacker_cyber_shift.get():
            col_shift += 1
        if self.defender_cyber_shift.get():
            col_shift -= 1
        col_shift += int(self.surprise_cbx.get())
        col_shift += int(self.attacker_arty_cbx.get())
        col_shift -= int(self.defender_arty_cbx.get())

        drm = 0
        support_defender_drm = 0
        support_defender_drm -= int(self.defender_helos_cbx.get())
        support_defender_drm -= int(self.defender_aircraft_cbx.get())
        support_defender_drm -= int(self.defender_navy_ent.get())
        if support_defender_drm < -6:
            support_defender_drm = -6

        defender_type_list = []
        for element in self.defender_data:
            defender_type_list.append(element[2].get())
        elite_infantry_defender_drm = 0
        if 'Light' in defender_type_list and self.terrain_cbx.get() in ['Rough', 'Rough Woods', 'Marsh', 'Highlands',
                                                                        'Jungle', 'Highland Woods',
                                                                        'Mountain', 'Urban']:
            elite_infantry_defender_drm -= 1

        if 'Mtn' in defender_type_list and self.terrain_cbx.get() in ['Highlands', 'Highland Woods', 'Mountain']:
            elite_infantry_defender_drm -= 1

        if elite_infantry_defender_drm < -1:
            elite_infantry_defender_drm = -1

        support_attacker_drm = 0
        support_attacker_drm += int(self.attacker_1_helos_cbx.get())
        support_attacker_drm += int(self.attacker_2_helos_cbx.get())
        support_attacker_drm += int(self.attacker_1_aircraft_cbx.get())
        support_attacker_drm += int(self.attacker_2_aircraft_cbx.get())
        support_attacker_drm += int(self.attacker_navy_ent.get())
        if support_attacker_drm > 6:
            support_attacker_drm = 6

        elite_infantry_attacker_drm = 0
        attacker_type_list = []
        for element in self.attacker_data:
            attacker_type_list.append(element[2].get())
        if 'Light' in attacker_type_list and self.terrain_cbx.get() in ['Rough', 'Rough Woods', 'Marsh', 'Highlands',
                                                                        'Jungle', 'Highland Woods',
                                                                        'Mountain', 'Urban']:
            elite_infantry_attacker_drm += 1

        if 'Mtn' in attacker_type_list and self.terrain_cbx.get() in ['Highlands', 'Highland Woods', 'Mountain']:
            elite_infantry_attacker_drm += 1
        if elite_infantry_attacker_drm > 1:
            elite_infantry_attacker_drm = 1

        drm += support_defender_drm
        drm += support_attacker_drm
        drm += elite_infantry_defender_drm
        if not self.amphibious_assault:
            drm += elite_infantry_attacker_drm

        if self.attacking_5_6_side.get():
            drm -= 2
        if self.attacking_3_4_side.get():
            drm -= 1
        if self.defender_in_installation.get():
            drm += 1
        drm += int(self.multi_formation_ent.get())
        if self.multi_nation_attack.get():
            drm += 1
        if self.irop_prc_attack.get():
            drm += 2

        self.calculate_att_ent.insert(END, str(att_sum))
        self.calculate_def_ent.insert(END, str(def_sum))
        self.calculate_col_shift_ent.insert(END, str(col_shift))
        self.calculate_drm_ent.insert(END, str(drm))

    def combat_result(self):

        terrain = self.terrain_cbx.get()
        shift = TERRAIN_TO_SHIFT[terrain]
        terrain_type = TERRAIN_TO_TYPE[terrain]
        self.combat_result_ent.delete(0, 'end')
        self.combat_odds_ent.delete(0, 'end')
        self.reduce_attacker_loss_ent.delete(0, 'end')
        self.result_dice_ent.delete(0, 'end')
        att = int(self.calculate_att_ent.get())
        defe = int(self.calculate_def_ent.get())
        mod = int(self.calculate_col_shift_ent.get())
        drm = int(self.calculate_drm_ent.get())

        frac = max(min(att / defe, terrain_type), min(defe / att, 3))
        if att < defe:
            frac = -frac

        if frac == 1.5:
            rem = 0
        else:
            if frac > 0:
                rem = frac - floor(frac)
            else:
                rem = 0
        if rem > 0:
            drm -= 1

        if 2 > frac >= 1.5:
            att_res_pure = 1.5
            order_pure = FRAC_TO_ORDER[att_res_pure]
            order = order_pure + mod
            if order > terrain_type:
                order = terrain_type
            if order < -2:
                order = -2
            if order > 0:
                att_res = ORDER_TO_FRAC[order]
                defe_res = 1
            else:
                defe_res = ORDER_TO_FRAC[order]
                att_res = 1
        else:
            if frac > 0:
                att_res_pure = floor(frac)

                order_pure = FRAC_TO_ORDER[att_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = ORDER_TO_FRAC[order]
                    defe_res = 1
                else:
                    defe_res = ORDER_TO_FRAC[order]
                    att_res = 1
            else:
                if frac >= -2:
                    defe_res_pure = -2
                else:
                    defe_res_pure = -3
                order_pure = FRAC_TO_ORDER[defe_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = ORDER_TO_FRAC[order]
                    defe_res = 1
                else:
                    defe_res = ORDER_TO_FRAC[order]
                    att_res = 1
        dice = randint(0, 9)
        row = dice + int(self.calculate_drm_ent.get())
        # row normalization
        if row > 12:
            row = 12
        if row < -3:
            row = -3
        row = row + 3
        odds = str(att_res) + ':' + str(defe_res)
        column = ODDS_TO_COLUMN[odds]
        column += shift
        column -= 1

        reduce_attacker_lost = 'No'
        if column > 9:
            reduce_attacker_lost = 'Yes'

        self.result_dice_ent.insert(END, str(dice))
        self.combat_odds_ent.insert(END, odds)
        self.combat_result_ent.insert(END, str(COMBAT_RESULT_TABLE[column][row]))
        self.reduce_attacker_loss_ent.insert(END, reduce_attacker_lost)

    def combat_result_predict(self):

        terrain = self.terrain_cbx.get()
        shift = TERRAIN_TO_SHIFT[terrain]
        terrain_type = TERRAIN_TO_TYPE[terrain]
        self.combat_result_ent.delete(0, 'end')
        self.combat_odds_ent.delete(0, 'end')
        self.reduce_attacker_loss_ent.delete(0, 'end')
        self.result_dice_ent.delete(0, 'end')
        att = int(self.calculate_att_ent.get())
        defe = int(self.calculate_def_ent.get())
        mod = int(self.calculate_col_shift_ent.get())
        drm = int(self.calculate_drm_ent.get())

        frac = max(min(att / defe, terrain_type), min(defe / att, 3))
        if att < defe:
            frac = -frac

        if frac == 1.5:
            rem = 0
        else:
            if frac > 0:
                rem = frac - floor(frac)
            else:
                rem = 0
        if rem > 0:
            drm -= 1

        if 2 > frac >= 1.5:
            att_res_pure = 1.5
            order_pure = FRAC_TO_ORDER[att_res_pure]
            order = order_pure + mod
            if order > terrain_type:
                order = terrain_type
            if order < -2:
                order = -2
            if order > 0:
                att_res = ORDER_TO_FRAC[order]
                defe_res = 1
            else:
                defe_res = ORDER_TO_FRAC[order]
                att_res = 1
        else:
            if frac > 0:
                att_res_pure = floor(frac)

                order_pure = FRAC_TO_ORDER[att_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = ORDER_TO_FRAC[order]
                    defe_res = 1
                else:
                    defe_res = ORDER_TO_FRAC[order]
                    att_res = 1
            else:
                if frac > -2:
                    defe_res_pure = -2
                else:
                    defe_res_pure = -3
                order_pure = FRAC_TO_ORDER[defe_res_pure]
                order = order_pure + mod
                if order > terrain_type:
                    order = terrain_type
                if order < -2:
                    order = -2
                if order > 0:
                    att_res = ORDER_TO_FRAC[order]
                    defe_res = 1
                else:
                    defe_res = ORDER_TO_FRAC[order]
                    att_res = 1

        drm = int(self.calculate_drm_ent.get())
        min_random_result = drm
        max_random_result = drm + 9
        # row normalization
        if max_random_result > 12:
            max_random_result = 12
        if min_random_result < -3:
            min_random_result = -3
        min_row = min_random_result + 3
        max_row = max_random_result + 3

        odds = str(att_res) + ':' + str(defe_res)
        column = ODDS_TO_COLUMN[odds]
        column += shift
        column -= 1

        defender_loss = sum(DEFENDER_LOSS_TABLE[column][min_row:max_row]) / 10
        attacker_loss = sum(ATTACKER_LOSS_TABLE[column][min_row:max_row]) / 10
        defender_retreat = sum(DEFENDER_RETREAT_CHANCE[column][min_row:max_row]) / 10

        self.attacker_pred_loss_ent.delete(0, 'end')
        self.defender_pred_loss_ent.delete(0, 'end')
        self.defender_pred_retreat_ent.delete(0, 'end')

        self.attacker_pred_loss_ent.insert(END, str(attacker_loss))
        self.defender_pred_loss_ent.insert(END, str(defender_loss))
        self.defender_pred_retreat_ent.insert(END, str(defender_retreat))
