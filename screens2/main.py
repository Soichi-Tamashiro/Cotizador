from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass

sm=Builder.load_file("mymain.kv")
# sm = Builder.load_string("""
# ScreenManager:
#     ScreenOne:
#         name: "screen1"
#         BoxLayout:
#             orientation: "vertical"
#             TextInput:
#                 id: _player_name
#                 text: _final_playername.text
#             Button:
#                 text: "Change Label on Screen 2"
#                 on_release:
#                     _final_playername.text = _player_name.text
#             Button:
#                 text: "Next Screen"
#                 on_release:
#                     root.current = "screen2"
#     ScreenTwo:
#         name: "screen2"
#         BoxLayout:
#             orientation: "vertical"
#             Label:
#                 text: "Default Text"
#                 id: _final_playername
#             Button:
#                 text: "Prev Screen"
#                 on_release:
#                     root.current = "screen1"
# """)


class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
