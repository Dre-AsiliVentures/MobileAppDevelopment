from kivymd.app import MDApp
from kivy.core.window import Window

class InstagramApp(MDApp):
    def build(self):
        #Window.size=[300,600]
        return super().build()
if __name__=="__main__":
    #InstagramApp().build()
    InstagramApp().run()
    #InstagramApp().build()