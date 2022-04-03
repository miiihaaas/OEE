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

new_extruder_parameters = ["0-ndf ID", "1-ndf RN", "2-ndf vreme", "3-ndf oprema", "4-ndf T1", "5-ndf T2", "6-ndf T3", "7-ndf T4", "8-ndf T5", "9-ndf tip šneka", "10-ndf rpm", "11-ndf torzija min", "12-ndf torzija max", "13-ndf T premiksa", "14-ndf komentar", "15-ndf RadnikID"]
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

        # trenutno vreme
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
        self.last_input.text = f"Vreme: {new_record[0]}, \nID-RN: {new_record[1]} - {new_record[2]}, \nAktivnost - Količina: {new_record[8]} - {new_record[6]}kg, \nOprema - Radnik: {new_record[7]} - {new_record[9]}"


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

# funkcije za Ekstruder parametre
# funkcije za Ekstruder parametre
# funkcije za Ekstruder parametre

    def spinner_clicked(self, value):
        new_extruder_parameters[3] = self.ids.spinner_oprema.text
        new_extruder_parameters[9] = self.ids.spinner_sneke.text
        print(f'{new_extruder_parameters[3]=}, {new_extruder_parameters[9]=}')
        print(new_extruder_parameters)
        pass

    def btn_scan_parameters(self):
        id_, rn, slovo, sarza, naziv = scan()
        print(f"{id_=}, {rn=}, {slovo=}, {sarza=}, {naziv=}")
        new_extruder_parameters[0] = id_
        new_extruder_parameters[1] = rn
        print(new_extruder_parameters)
        self.ids.sanned_label.text = f'{id_} - {rn} - ({slovo}) \n{naziv}'

    def minus_clicked(self, value1, value2):
        button_detection = "prazan podatak"
        button_detection = value2
        if button_detection == "T1:":
            self.ids.T1_input.text = str(int(self.ids.T1_input.text) - 10)
        elif button_detection == "T2:":
            self.ids.T2_input.text = str(int(self.ids.T2_input.text) - 10)
        elif button_detection == "T3:":
            self.ids.T3_input.text = str(int(self.ids.T3_input.text) - 10)
        elif button_detection == "T4:":
            self.ids.T4_input.text = str(int(self.ids.T4_input.text) - 10)
        elif button_detection == "T5:":
            self.ids.T5_input.text = str(int(self.ids.T5_input.text) - 10)
        print(button_detection)

    def plus_clicked(self, value1, value2):
        button_detection = "prazan podatak"
        button_detection = value2
        if button_detection == "T1:":
            self.ids.T1_input.text = str(int(self.ids.T1_input.text) + 10)
            # new_extruder_parameters[4] = self.ids.T1_input.text
            # print(f'{new_extruder_parameters[4]}°C')
            # print(new_extruder_parameters)
        elif button_detection == "T2:":
            self.ids.T2_input.text = str(int(self.ids.T2_input.text) + 10)
        elif button_detection == "T3:":
            self.ids.T3_input.text = str(int(self.ids.T3_input.text) + 10)
        elif button_detection == "T4:":
            self.ids.T4_input.text = str(int(self.ids.T4_input.text) + 10)
        elif button_detection == "T5:":
            self.ids.T5_input.text = str(int(self.ids.T5_input.text) + 10)
        print(button_detection)

    def x_to_y(self, value):
        self.ids.T1_input.text = value
        self.ids.T2_input.text = value
        self.ids.T3_input.text = value
        self.ids.T4_input.text = value
        self.ids.T5_input.text = value

    def send_record_parameters(self):
        new_extruder_parameters[2] = datetime.datetime.now()
        # pretvara ga u string koji excel može da poročita kao datum vreme
        new_extruder_parameters[2] = new_extruder_parameters[2].strftime("%x %X")
        new_extruder_parameters[4] = self.ids.T1_input.text
        new_extruder_parameters[5] = self.ids.T2_input.text
        new_extruder_parameters[6] = self.ids.T3_input.text
        new_extruder_parameters[7] = self.ids.T4_input.text
        new_extruder_parameters[8] = self.ids.T5_input.text
        new_extruder_parameters[10] = self.ids.rpm_input.text
        new_extruder_parameters[11] = self.ids.torzija_min_input.text
        new_extruder_parameters[12] = self.ids.torzija_max_input.text
        new_extruder_parameters[13] = self.ids.doziranje_input.text
        new_extruder_parameters[14] = self.ids.T_premiksa_input.text
        new_extruder_parameters[15] = self.ids.RadnikID_input.text
        print(new_extruder_parameters)
        #dodati kod koji će da resetuje određene parametre kako bi dugme bilo crvenos
        #dodati kod koji će da resetuje određene parametre kako bi dugme bilo crvenos
        #dodati kod koji će da resetuje određene parametre kako bi dugme bilo crvenos
        #dodati kod koji će da resetuje određene parametre kako bi dugme bilo crvenos
        
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

class EkstruderParametersWindow(Screen, Potvrdi):
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
