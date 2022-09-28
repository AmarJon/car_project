from tkinter import *

class CarListBox(Listbox):
    def __init__(self, frame, car_list):
        super().__init__(frame, width=600)
        self.car_list = car_list

    def update_listbox(self, car_list):
        self.car_list = car_list
        self.clear_listbox()
        self.refresh()

    def clear_listbox(self):
        self.pack_forget()

    def delete_car(self):
        # print cur selection, figure out how to delete car list
        del self.car_list[self.curselection()[0]: self.curselection()[1]]
        self.refresh()

    def refresh(self):
        self.delete(0, END)
        for car in self.car_list:
            self.insert(END, car.to_string())
        self.pack()

