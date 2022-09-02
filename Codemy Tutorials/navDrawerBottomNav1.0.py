from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.icon_definitions import md_icons
from kivy.config import Config
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.text import LabelBase


import time
# Date time module
from datetime import date

#Import window
from kivy.core.window import Window
Window.size=(800, 480)
class ContentNavigationDrawer(BoxLayout):
    #screen_manager=ObjectProperty()
    #nav_drawer=ObjectProperty()
    pass
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

class DrawerList(ThemableBehavior,MDList):
    pass
class irrigationApp(MDApp):
    def build(self):
        return Builder.load_file("navDrawerBottomNav1.0.kv")
    def on_start(self):
        self.theme_cls.primary_palette = "Indigo"
        self.root.ids.toolbar.ids.label_title.font_style = 'H5'

if __name__=='__main__':
    irrigationApp().run()