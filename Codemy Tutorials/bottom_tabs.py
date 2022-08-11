from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class demo(FloatLayout):
    pass
class bottomtabs(MDApp):
    def build(self):
        Builder.load_file("bottom_tabs.kv")
        return demo()
if __name__=='__main__':
    bottomtabs().run()