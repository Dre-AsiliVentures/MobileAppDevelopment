import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myGridLayoutness(GridLayout):
    def __init__(self,**kwargs):
        # Call init
        super(myGridLayoutness,self).__init__(*kwargs)

        # Set columns
        self.cols=2

        # Adding the widget1
        self.add_widget(Label(text="Name:" ))
        # Adding input Box
        self.name=TextInput(multiline=False) # For multline =False Presenting Enter doesn't work
        self.add_widget(self.name)

         # Adding the widget 2
        self.add_widget(Label(text="Favourite:" ))
        # Adding input Box
        self.fav_color=TextInput(multiline=False)
        self.add_widget(self.fav_color)

        # Adding Button
        self.submitButton=Button(text="Submitt")
        self.add_widget(self.submitButton)
        # Adding Bind the button - what the buttons does
        self.submitButton.bind(on_press=self.press) # Calls def press() funtion

        self.labels=Label(text="Geek unadate sasa!!",font_size=32)
        self.add_widget(self.labels)

    def press(self,instance):
        name=self.name.text # The text input from name 
        favoriteColor=self.fav_color.text # The text input from self.color
        self.labels=Label(text=f'Hello {name}, you love {favoriteColor}',font_size=32)
        self.add_widget(self.labels)
class testApp(App):
    def build(self):
        self.awesomeGrid=myGridLayoutness()
        return self.awesomeGrid
if __name__=='__main__':
    testApp().run()

