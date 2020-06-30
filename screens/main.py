import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import mainthread
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

rend_tarifa_1=""

class MainWindow(Screen):
    global rend_tarifa_1
    # ObjectProperty()
    altura= ObjectProperty()
    gsd= ObjectProperty()
    espaciamiento= ObjectProperty()
    tarifa=ObjectProperty()

    zona_plana=ObjectProperty()
    cerros=ObjectProperty()
    rend_estd=ObjectProperty()
    rend_redc=ObjectProperty()
    peso=ObjectProperty()
    rend_tarifa=ObjectProperty()
    semanas=ObjectProperty()
    hectareas_min=ObjectProperty()
    hectareas_max=ObjectProperty()
    km_lineales=ObjectProperty()
    dias=ObjectProperty()
    costo=ObjectProperty()
    costo_ha=ObjectProperty()
    # StringProperty()
    tarifa_text=StringProperty()
    rend_tarifa_text=StringProperty()
    semanas_text=StringProperty()
    hectareas_min_text=StringProperty()
    hectareas_max_text=StringProperty()
    km_lineales_text=StringProperty()
    dias_text=StringProperty()

    def btn(self):
        if(self.altura.text!=""):
            self.gsd.text = str(float(self.altura.text)/40)
            self.espaciamiento.text = str(float(self.altura.text)*7/10)
            ha=float(self.altura.text)
        if(self.zona_plana.text!=""):
            self.cerros.text = str(100-int(self.zona_plana.text))
            z_plana=
        if(self.rend_estd.text!=""):
            self.rend_redc.text = str(100-int(self.rend_estd.text))
        if(self.peso.text!=""):
            p=float(self.peso.text)
        if(self.altura.text!="" and self.zona_plana.text!="" and self.rend_estd.text!=""):
            self.rend_tarifa.text=str((float(self.zona_plana.text)+float(self.cerros.text))*(float(self.rend_redc.text)+float(self.rend_estd.text))*float(self.altura.text)/200)
            ha=float(self.rend_tarifa.text)
            if(ha<=300):
                cant_dias=1
                cant_sem=1
                h_min=1
                h_max=300
            elif(ha>300 and ha<=1200):
                cant_dias=2
                cant_sem=1
                h_min=301
                h_max=1200
            elif(ha>1200):
                ha_new=ha-1200
                if((ha_new%693)>0):
                    c_dias=1+(ha_new//693)
                else:
                    c_dias=ha_new//693
                cant_dias=2+round(c_dias)
                h_max=1200+693*round(c_dias)
                h_min=h_max-692
                if((cant_dias%6)>0):
                    cant_sem=1+(cant_dias//6)
                else:
                    cant_sem=cant_dias//6
            else:
                cant_dias=0

        # if(self.peso.text!="" and )
        #     km=ha/12*cant_dias*p/100

            self.dias.text=str(cant_dias)
            self.semanas.text=str(cant_sem)
            self.hectareas_min.text=str(h_min)
            self.hectareas_max.text=str(h_max)
            self.km_lineales.text=str(km)


class SecondWindow(Screen,Widget):
    global rend_tarifa_1
    tarifa_text=StringProperty()
    rend_tarifa_text= StringProperty()
    dias_text=StringProperty()
    semanas_text=StringProperty()
    hectareas_min_text=StringProperty()
    hectareas_max_text=StringProperty()
    km_lineales_text=StringProperty()
    # semanas= ObjectProperty(None)
    # hectareas_min= ObjectProperty(None)
    # hectareas_max= ObjectProperty(None)
    # km_lineales= ObjectProperty(None)
    # dias= ObjectProperty(None)
    # costo= ObjectProperty(None)
    # costo_ha= ObjectProperty(None)


class WindowManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super(WindowManager, self).__init__(*args, **kwargs)

        @mainthread
        def delayed():
            mainwindow = self.get_screen('main')
            secondwindow = self.get_screen('second')
            mainwindow.bind(tarifa_text=secondwindow.setter('tarifa_text'))
            mainwindow.bind(rend_tarifa_text=secondwindow.setter('rend_tarifa_text'))
            mainwindow.bind(dias_text=secondwindow.setter('dias_text'))
            mainwindow.bind(semanas_text=secondwindow.setter('semanas_text'))
            mainwindow.bind(hectareas_min_text=secondwindow.setter('hectareas_min_text'))
            mainwindow.bind(hectareas_max_text=secondwindow.setter('hectareas_max_text'))
            mainwindow.bind(km_lineales_text=secondwindow.setter('km_lineales_text'))
        delayed()


kv = Builder.load_file("mymain.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
