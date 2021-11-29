import datetime
import csv

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
from kivy.properties import ListProperty


new_record = ["nedefinisano vreme", "nedefinisan ID", "nedefinisan RN", 0, "nedefinisana oprema", "nedefinisana aktivnost", "nedefinisan radnik"]
file_path = "D:\Mihas\Programming\Python\Projects\OEE\OEE\CollectedData\\"
file_name = ""

class Potvrdi():
    id_ = ObjectProperty(None)
    rn = ObjectProperty(None)
    quantity = ObjectProperty(None)
    worker_id = ObjectProperty(None)
    equipment = ObjectProperty(None)
    activity = "nedefinisana aktivnost"


    def btn_eqpmnt_press(self):
        new_record[4] = self.equipment
        print(new_record)

    def btn_activity_press(self):
        new_record[5] = self.activity
        print(new_record)


    def btn_press(self):
        new_record[1] = self.id_.text
        new_record[2] = self.rn.text
        if new_record[5] == ("Ekstrudiranje" or "Mlevenje"):
            new_record[3] = self.quantity.text
        else:
            new_record[3] = 0
        new_record[6] = self.worker_id.text
        # trentno vreme
        new_record[0] = datetime.datetime.now()
        # pretvara ga u string koji excel može da poročita kao datum vreme
        new_record[0] = new_record[0].strftime("%x %X")
        print(new_record)
        file_name = f"{new_record[4]}.csv"
        print(file_path + file_name)
        with open(file_path + file_name, "a", encoding='UTF8', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(new_record)
        self.id_.text = ""
        self.rn.text = ""
        if new_record[5] == ("Ekstrudiranje" or "Mlevenje"):
            self.quantity.text = ""
        self.worker_id.text = ""



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

class AktivnostCiscenjeWindow(Screen, Potvrdi):
    pass


class AktivnostCiscenjeRadnogMestaWindow(Screen, Potvrdi):
    pass


class AktivnostCekanjeProbeSaMlinaWindow(Screen, Potvrdi):
    pass


class AktivnostKontrolaWindow(Screen, Potvrdi):
    pass


class AktivnostKvarWindow(Screen, Potvrdi):
    pass


class AktivnostNemaPremiksaWindow(Screen, Potvrdi):
    pass


class AktivnostZagrevanjeWindow(Screen, Potvrdi):
    pass


class AktivnostNemaOperateraWindow(Screen, Potvrdi):
    pass




class MlevenjeWindow(Screen):
    equipment = "nedefinisana oprema sa mlina"
    def btn_press(self):
        new_record[4] = self.equipment
        print(new_record)
    pass

class MlinAktivnostiWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
