from kivy.app import App
from kivy.clock import mainthread
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

from kivymd.app import MDApp

from math import ceil

class MainWindow(Screen):
    # ObjectProperty()
    altura = ObjectProperty()
    gsd = ObjectProperty()
    espaciamiento = ObjectProperty()
    tarifa = ObjectProperty()
    zona_plana = ObjectProperty()
    cerros = ObjectProperty()
    rend_estd = ObjectProperty()
    rend_redc = ObjectProperty()
    peso = ObjectProperty()

    def btn(self, instance):

        # Interaction between Kivy widgets in Python
        # Use a dictionary to pass values between Classes
        b = App.get_running_app()
        # Populate dictionary keys
        b.big_dict = dict.fromkeys(self.ids.keys(), 1)
        b.big_dict['altura'] = self.altura.text
        b.big_dict['gsd'] = self.gsd.text
        b.big_dict['espaciamiento'] = self.espaciamiento.text
        b.big_dict['tarifa'] = self.tarifa.text
        b.big_dict['zona_plana'] = self.zona_plana.text
        b.big_dict['cerros'] = self.cerros.text
        b.big_dict['rend_estd'] = self.rend_estd.text
        b.big_dict['rend_redc'] = self.rend_redc.text
        b.big_dict['peso'] = self.peso.text
        if(b.big_dict['altura'] != ""):
            b.big_dict['gsd'] = str(float(b.big_dict['altura']) / 40)
            b.big_dict['espaciamiento'] = str(
                float(b.big_dict['altura']) * 7 / 10)
        if(b.big_dict['zona_plana'] != ""):
            b.big_dict['cerros'] = str(100 - float(b.big_dict['zona_plana']))
        if(b.big_dict['rend_estd'] != ""):
            b.big_dict['rend_redc'] = str(100 - float(b.big_dict['rend_estd']))

        # b.big_dict['cargo_fijo']=float(self.cargo_fijo.text)
        # b.big_dict['cargo_fijo'] = str(float(self.cargo_fijo.text)*5)
        # print(self.ids.keys())
        self.gsd.text = b.big_dict['gsd']
        self.espaciamiento.text = b.big_dict['espaciamiento']
        self.cerros.text = b.big_dict['cerros']
        self.rend_redc.text = b.big_dict['rend_redc']
        print(b.big_dict)
    pass


class SecondWindow(Screen, Widget):
    # ObjectProperty()
    tarifa = ObjectProperty()
    rend_tarifa = ObjectProperty()
    semanas = ObjectProperty()
    hectareas_min = ObjectProperty()
    hectareas_max = ObjectProperty()
    km_lineales = ObjectProperty()
    dias = ObjectProperty()
    costo = ObjectProperty()
    costo_ha = ObjectProperty()

    def on_enter(self, *args):
        c = App.get_running_app()

        self.tarifa.text = "S/."+c.big_dict['tarifa']
        if(c.big_dict['zona_plana'] != ""):
            z_plana = 1200 * float(c.big_dict['zona_plana']) / 100
            z_cerros = 600 * float(c.big_dict['cerros']) / 100
            geo = 1
        else:
            geo = 0
        if(c.big_dict['rend_estd'] != ""):
            rend_3_menos = 1 * float(c.big_dict['rend_estd']) / 100
            rend_3_mas = 0.65 * float(c.big_dict['rend_redc']) / 100
            rend_3 = 1
        else:
            rend_3 = 0
        if(geo * rend_3 and c.big_dict['peso'] != "" and c.big_dict['altura']!=""):
            C12=z_plana
            D12=z_cerros
            E12=rend_3_menos
            F12=rend_3_mas
            C3=float(c.big_dict['altura'])
            G12=float(c.big_dict['peso'])
            ha=((((C12+D12)*(E12+F12)*C3/250)-((1600+(C3*C3*C3*C3/10000))/400000*((C12+D12)*(E12+F12)*C3/250))/100)*G12/100)

            self.rend_tarifa.text=str(ceil(ha))+" "+ "ha"

            if(ha <= 336):
                cant_dias = 1
                cant_sem = 1
                h_min = 1
                h_max = 336
            elif(ha > 336 and ha <= 648):
                cant_dias = 2
                cant_sem = 1
                h_min = 337
                h_max = 648
            elif(ha > 648 and ha <= 958):
                cant_dias = 2
                cant_sem = 1
                h_min = 649
                h_max = 958
            elif(ha > 958):
                ha_new = ha - 958
                if((ha_new % 311) > 0):
                    c_dias = 1 + (ha_new // 311)
                else:
                    c_dias = ha_new // 311
                cant_dias = 2 + round(c_dias)
                h_max = 958 + 311 * round(c_dias)
                h_min = h_max - 310
                if((cant_dias % 6) > 0):
                    cant_sem = 1 + (cant_dias // 6)
                else:
                    cant_sem = cant_dias // 6
            else:
                cant_dias = 0
                cant_sem = 0
                h_min = 1
                h_max = 300

            km=ha/12*cant_dias*G12/100

            costo_total=float(c.big_dict['tarifa'])*cant_dias
            costo_por_ha =costo_total*2/(h_min+h_max)
            if (cant_dias==1):
                self.dias.text = str(cant_dias) +" " + "dia"
            else:
                self.dias.text = str(cant_dias) +" " + "dias"
            if (cant_dias==1):
                self.semanas.text = str(cant_sem) + " " + "semana"
            else:
                self.semanas.text = str(cant_sem) + " " + "semanas"
            self.hectareas_min.text = str(h_min)
            self.hectareas_max.text = str(h_max)
            self.km_lineales.text = str(round(km,2))+ " "+ "Km"
            self.costo.text = str(round(costo_total,2))
            self.costo_ha.text = str(round(costo_por_ha,3))

        # if(self.peso.text!="" and )
        #     km=ha/12*cant_dias*p/100
        # print("Gear Secondo")

    # cargo_fijo_2=StringProperty()
    # @mainthread
    # def update(self):
    #     # Populate dictionary keys
    #     c = App.get_running_app()
    #     # c.big_dict = self.ids.keys()
    #     self.cargo_fijo_2.text = c.big_dict["cargofijo"]
    #     print(c.big_dict)
    #
    pass


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # @mainthread
    # def update(self,instance):
    #     mainwindow = self.get_screen('main')
    #     secondwindow = self.get_screen('second')
    #     # self.cargo_fijo_2.text = "hqy"
    #     # cargofijo=self.ids.WindowManager.MainWindow.cargo_fijo.text
    #     # self.cargo_fijo_2.text = cargofijo
    #     # print(cargofijo)
    #     pass


class MainApp(MDApp):
    # Interaction between Kivy widgets in Python
    # Use a dictionary to pass values between Classes
    big_dict = {'cargo_fijo': '', 'botonazo': ''}

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = "Dark"
        return WindowManager()


if __name__ == "__main__":
    MainApp().run()
