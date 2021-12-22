import datetime
import csv
from qr_scanner import scan

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window


new_record = ["0- ndf vreme", "1 -ndf ID", "2 -ndf RN", "3- ndf slovo", "4- ndf šarža", "5- ndf naziv", 0, "7- ndf oprema!", "8- ndf aktivnost", "9- ndf radnik", "10- ndf pomoćnik", "11- ndf komentar", "12- ndf ID kvara"]
file_path = "D:\Mihas\Programming\Python\Projects\OEE\OEE\CollectedData\\"
# file_path = "https://helgrp-my.sharepoint.com/:f:/r/personal/mihailo_panic_helios_rs/Documents/01%20Proizvodnja/01%20OEE/Python/"
file_name = ""

class Potvrdi():
    Window.size = (360, 640) # povećati na 720, 1280 kada se bude instaliralo na android
    id_ = ObjectProperty(None)
    rn = ObjectProperty(None)
    slovo = ObjectProperty(None) #
    sarza = ObjectProperty(None) #
    naziv = ObjectProperty(None) #
    quantity = ObjectProperty(None)
    worker_id = ObjectProperty(None)
    worker_id_pomocnik = ObjectProperty(None) #
    komentar = ObjectProperty(None) #
    kvar_id = ObjectProperty(None) #
    equipment = ObjectProperty(None) #
    activity = ObjectProperty(None) #
    last_input = ObjectProperty(None)


    def update_equipment_labels(self):
        self.equipment.text = new_record[7]


    def update_activity_labels(self):
        self.activity.text = new_record[7] + " / " + new_record[8]
        self.last_input.text = f"Vreme: {new_record[0]}, \nID-RN: {new_record[1]} - {new_record[2]}, \nOprema - Radnik: {new_record[7]} - {new_record[8]}"


    def btn_eqpmnt_press(self):
        new_record[7] = self.equipment.text
        print(new_record)


    def btn_activity_press(self):
        new_record[8] = self.activity.text
        print(new_record)


    def btn_press(self):
        if new_record[8] == "Ekstrudiranje":
            new_record[6] = self.quantity.text
        elif new_record[8] == "Mlevenje":
            new_record[6] = self.quantity.text
        else:
            new_record[6] = 0
        new_record[9] = self.worker_id.text
        new_record[10] = self.worker_id_pomocnik.text
        new_record[11] = self.komentar.text
        if new_record[8] == "Kvar":
            new_record[12] = self.kvar_id.text
        else:
            new_record[12] = ""

        # trentno vreme
        new_record[0] = datetime.datetime.now()
        # pretvara ga u string koji excel može da poročita kao datum vreme
        new_record[0] = new_record[0].strftime("%x %X")
        print(new_record)
        file_name = f"{new_record[7]}.csv"
        print(file_path + file_name)
        # append new_record to .csv file
        with open(file_path + file_name, "a", encoding='UTF8', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(new_record)
        # reset input values
        self.id_.text = "ID: "
        self.rn.text = "RN: "
        self.slovo.text = "??"
        self.sarza.text = "??"
        self.naziv.text = "Naziv: Skeniraj QR Kod"
        if new_record[8] == "Ekstrudiranje":
            self.quantity.text = ""
        elif new_record[8] == "Mlevenje":
            self.quantity.text = ""
        self.worker_id.text = ""
        self.worker_id_pomocnik.text = ""
        self.komentar.text = ""
        self.last_input.text = f"Vreme: {new_record[0]}, \nID-RN: {new_record[1]} - {new_record[2]}, \nAktivnost - Količina: {new_record[7]} - {new_record[5]}kg, \nOprema - Radnik: {new_record[6]} - {new_record[8]}"


    def btn_scan(self):
        id_, rn, slovo, sarza, naziv = scan()
        print(f"{id_=}, {rn=}, {slovo=}, {sarza=}, {naziv=}")
        new_record[1] = id_
        new_record[2] = rn
        new_record[3] = slovo
        new_record[4] = sarza
        new_record[5] = naziv
        print(new_record)
        self.id_.text = id_
        self.rn.text = rn
        self.slovo.text = f"({slovo})"
        self.sarza.text = sarza
        self.naziv.text = naziv
        pass


class AktivnostUniverzalnaWindow(Screen, Potvrdi):
    pass


class MainWindow(Screen):
    pass


class SarziranjeWindow(Screen):
    pass


class EkstrudiranjeWindow(Screen, Potvrdi):
    pass


class EkstruderAktivnostiWindow(Screen, Potvrdi):
    pass


class AktivnostEktrurdiranjeWindow(Screen, Potvrdi):
    pass


class AktivnostKvarWindow(Screen, Potvrdi):
    pass


class MlevenjeWindow(Screen, Potvrdi):
    pass


class MlinAktivnostiWindow(Screen, Potvrdi):
    pass


class AktivnostMlevenjeWindow(Screen, Potvrdi):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
