from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp

Builder.load_string(
    """
<ExampleTextFields@BoxLayout>:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: "Primary"
        elevation: 10
        left_action_items: [["menu", lambda x: None]]

    ScrollView:

    GridLayout:
        cols: 2
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: dp(48)
            spacing: dp(10)

            MDLabel:
                text: "No helper text"

            MDLabel:
                text: "Helper text on focus"

        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: dp(48)
            spacing: 10

            MDTextField:
                hint_text: "No helper text"

            MDTextField:
                hint_text: "Helper text on focus"
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"


"""
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "KivyMD Examples - Text Fields"
        self.theme_cls.primary_palette = "Blue"

    def build(self):
        self.root = Factory.ExampleTextFields()


if __name__ == "__main__":
    MainApp().run()
