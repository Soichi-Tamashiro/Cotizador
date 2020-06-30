from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import mainthread
from kivy.lang import Builder

gui = '''
MyScreenManager

    HomeScreen
        name: 'home'

    LoginScreen
        name: 'login'


<HomeScreen>
    nickname_input: nickname_input
    nickname: nickname_input.text

    BoxLayout:
        TextInput
            id: nickname_input
        Button
            on_press: root.manager.current = 'login'

<LoginScreen>

    BoxLayout:
        Label
            text: root.nickname
        Button
            on_press: root.manager.current = 'home'
'''


class HomeScreen(Screen):
    nickname_input = ObjectProperty()
    nickname = StringProperty()


class LoginScreen(Screen):
    nickname = StringProperty()


class MyScreenManager(ScreenManager):

    def __init__(self, *args, **kwargs):
        super(MyScreenManager, self).__init__(*args, **kwargs)

        @mainthread
        def delayed():
            home_screen = self.get_screen('home')
            login_screen = self.get_screen('login')

            home_screen.bind(nickname=login_screen.setter('nickname'))
        delayed()


class Test(App):

    def build(self):
        return Builder.load_string(gui)

Test().run()
