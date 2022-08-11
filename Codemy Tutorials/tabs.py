from kivy.app import App
from kivy.uix import widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("tabs.kv")
class myLayout(TabbedPanel):
    pass
class awesomeApp(App):
    def build(self):
        return myLayout()

if __name__ == '__main__':
    awesomeApp().run()