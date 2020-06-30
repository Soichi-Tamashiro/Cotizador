import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class MainWindow(Screen):
    # global rend_tarifa_1
    # altura= ObjectProperty()
    # gsd= ObjectProperty()
    # espaciamiento= ObjectProperty()
    tarifa=ObjectProperty()
    # tarifa_text=StringProperty()
    # zona_plana=ObjectProperty()
    # cerros=ObjectProperty()
    # rend_estd=ObjectProperty()
    # rend_redc=ObjectProperty()
    # peso=ObjectProperty(None)

    def btn(self):
        if(self.tarifa.text!=""):
            self.rend_tarifa.text = str(float(self.tarifa.text)/40)
    #         self.espaciamiento.text = str(float(self.altura.text)*9/10)
    #         rend_tarifa_1 = str(float(self.altura.text)/40)
    #         print(rend_tarifa_1)
    #     if(self.zona_plana.text!=""):
    #         self.cerros.text = str(100-int(self.zona_plana.text))
    #     if(self.rend_estd.text!=""):
    #         self.rend_redc.text = str(100-int(self.rend_estd.text))
    pass

class SecondWindow(Screen):
    # global rend_tarifa_1
    # tarifa_text=StringProperty()
    # rend_tarifa= ObjectProperty()
    # semanas= ObjectProperty(None)
    # hectareas_min= ObjectProperty(None)
    # hectareas_max= ObjectProperty(None)
    # km_lineales= ObjectProperty(None)
    # dias= ObjectProperty(None)
    # costo= ObjectProperty(None)
    # costo_ha= ObjectProperty(None)
    pass

kv = Builder.load_file("mymain.kv")

class MyMainApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
