from tkinter import Label, BooleanVar
from tkinter import Entry
from tkinter import Button
from tkinter import END
from tkinter import Toplevel
from tkinter.ttk import Combobox, Checkbutton
from random import randint


class ClearingOperation(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Clearing Operation')
        self.geometry("400x270+10+10")

        self.terrain_type_lbl = Label(self, text='Terrain:')
        self.terrain_type_cbx = Combobox(self, values=('Urban', 'City', 'Instalation'), width=10)
        self.terrain_type_cbx.set('Urban')
        self.efficiency_lbl = Label(self, text='Efficiency:')
        self.efficiency_cbx = Combobox(self, values=('1', '2', '3', '4', '5', '6', '7', '8'), width=4)
        self.efficiency_cbx.set('1')
        self.clearing_number_lbl = Label(self, text='Clearing:')
        self.clearing_number_cbx = Combobox(self, values=('3', '4', '5', '6'), width=4)
        self.clearing_number_cbx.set('3')
        self.stack_points_lbl = Label(self, text='Stack points:')
        self.stack_points_ent = Entry(self, width=7)
        self.stack_points_ent.insert(END, '0')
        self.installation_per_hex = Combobox(self, values=('0', '1', '2', '3'), width=4)
        self.installation_per_hex.set('0')
        self.clearing_btn = Button(self, text='Clearing', command=self.clearing)
        self.clearing_d10_lbl = Label(self, text='d10:')
        self.clearing_d10_ent = Entry(self, width=7)
        self.clearing_result_lbl = Label(self, text='Clearing result:')
        self.clearing_result_ent = Entry(self, width=7)
        self.loss_result_lbl = Label(self, text='Loss')
        self.loss_result_ent = Entry(self, width=7)

        self.paradrop = BooleanVar()
        self.paradrop.set(False)
        self.paradrop_chk = Checkbutton(self, text='Clearing from paradrop', variable=self.paradrop)

        self.combined_arms = BooleanVar()
        self.combined_arms.set(False)
        self.combined_arms_chk = Checkbutton(self, text='Leg and mechanized/armored', variable=self.combined_arms)

        self.terrain_type_lbl.place(x=10, y=20)
        self.terrain_type_cbx.place(x=100, y=20)
        self.efficiency_lbl.place(x=10, y=50)
        self.efficiency_cbx.place(x=100, y=50)
        self.clearing_number_lbl.place(x=10, y=80)
        self.clearing_number_cbx.place(x=100, y=80)
        self.stack_points_lbl.place(x=10, y=110)
        self.stack_points_ent.place(x=100, y=110)
        self.clearing_btn.place(x=10, y=140)
        self.clearing_d10_lbl.place(x=10, y=170)
        self.clearing_d10_ent.place(x=100, y=170)
        self.clearing_result_lbl.place(x=10, y=200)
        self.clearing_result_ent.place(x=100, y=200)
        self.loss_result_lbl.place(x=10, y=230)
        self.loss_result_ent.place(x=100, y=230)
        self.paradrop_chk.place(x=200, y=20)
        self.combined_arms_chk.place(x=200, y=50)

    def clearing(self):
        self.clearing_d10_ent.delete(0, 'end')
        self.clearing_result_ent.delete(0, 'end')
        self.loss_result_ent.delete(0, 'end')
        d10 = randint(0, 9)

        terrain_to_points = {'Urban': 4, 'City': 3, 'Installation': 2}
        minimum_safe_stack = terrain_to_points[self.terrain_type_cbx.get()]
        drm = int(self.efficiency_cbx.get()) - int(self.clearing_number_cbx.get())
        stack_diff = int(self.stack_points_ent.get()) - minimum_safe_stack

        if stack_diff < 0:
            drm += stack_diff

        effect = d10 + drm
        if effect < int(self.clearing_number_cbx.get()):
            result = 'Fail'
        else:
            result = 'Clear'
        if result == 'Fail' and stack_diff < 0:
            loss = 'Yes'
        else:
            loss = 'No'
        self.clearing_d10_ent.insert(END, str(d10))
        self.clearing_result_ent.insert(END, result)
        self.loss_result_ent.insert(END, loss)
