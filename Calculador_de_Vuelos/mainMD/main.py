from kivy.app import App
from kivy.clock import mainthread
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

from kivymd.app import MDApp

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
        if(b.big_dict['altura']!=""):
            b.big_dict['gsd'] =str(float(b.big_dict['altura'])/40)
            b.big_dict['espaciamiento'] =str(float(b.big_dict['altura'])*7/10)
        if(b.big_dict['zona_plana']!=""):
            b.big_dict['cerros'] =str(100-float(b.big_dict['zona_plana']))
        if(b.big_dict['rend_estd']!=""):
            b.big_dict['rend_redc'] =str(100-float(b.big_dict['rend_estd']))
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
        # self.cargo_fijo_2.text = c.big_dict["cargo_fijo"]
        # print(c.big_dict["cargo_fijo"])
        self.tarifa.text = c.big_dict['tarifa']
        print("Gear Secondo")

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
