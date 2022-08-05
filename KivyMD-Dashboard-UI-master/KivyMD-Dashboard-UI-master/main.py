from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.title=' GreHiDeLKivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"


MainApp().run()
