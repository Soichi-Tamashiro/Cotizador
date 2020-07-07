from kivy.app import App
from kivy.clock import mainthread
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

from kivymd.app import MDApp

class MainWindow(Screen):
    cargo_fijo = ObjectProperty()

    def btn(self, instance):
        # Interaction between Kivy widgets in Python
        # Use a dictionary to pass values between Classes
        b = App.get_running_app()
        # Populate dictionary keys
        b.big_dict = dict.fromkeys(self.ids.keys(), 1)
        b.big_dict['botonazo'] = "Cotizar"
        # b.big_dict['cargo_fijo']=float(self.cargo_fijo.text)
        # b.big_dict['cargo_fijo'] = str(float(self.cargo_fijo.text)*5)
        # print(self.ids.keys())
        print(b.big_dict)
    pass


class SecondWindow(Screen, Widget):
    cargo_fijo_2 = ObjectProperty()

    def on_enter(self, *args):
        c = App.get_running_app()
        # self.cargo_fijo_2.text = c.big_dict["cargo_fijo"]
        # print(c.big_dict["cargo_fijo"])
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
