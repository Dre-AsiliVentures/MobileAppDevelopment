from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

class dropdown(BoxLayout):
    pass
class dropDownApp(App):
    def build(self):
        return dropdown()
if __name__ == '__main__':
    dropDownApp().run()