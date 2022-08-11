
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class mainNDapp(MDApp):
    def build(self):
        return Builder.load_file("navigationDrawer.kv")


mainNDapp().run()