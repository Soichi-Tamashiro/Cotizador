import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class MyGrid(Widget):
    altura= ObjectProperty(None)
    gsd= ObjectProperty(None)
    espaciamiento= ObjectProperty(None)
    tarifa=ObjectProperty(None)
    zona_plana=ObjectProperty(None)
    cerros=ObjectProperty(None)
    rend_estd=ObjectProperty(None)
    rend_redc=ObjectProperty(None)
    peso=ObjectProperty(None)

    def btn(self):
        if(self.altura.text!=""):
            self.gsd.text = str(float(self.altura.text)/40)
            self.espaciamiento.text = str(float(self.altura.text)*9/10)
        if(self.zona_plana.text!=""):
            self.cerros.text = str(100-int(self.zona_plana.text))
        if(self.rend_estd.text!=""):
            self.rend_redc.text = str(100-int(self.rend_estd.text))


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
