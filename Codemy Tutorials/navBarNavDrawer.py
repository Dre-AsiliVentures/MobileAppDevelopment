from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBody
from kivymd.uix.button import MDIconButton
from kivy.lang.builder import  Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager

import time


Window.size = (320, 600)


class ItemScreenDrawer(GridLayout):

    """
    Ժեստի մասին ավելի մանրամասն ինֆորմացիա, յա խզ ոնց , բայց աշխատում ա
    """

    text = StringProperty()
    source = StringProperty()


class ContentNavigationDrawer(BoxLayout):
    """
    Նավիգացիան ա նկարում, թե ոնց ա աշխատում, մենակ աստված գիտի
    """
    pass

class CardsDrawer(GridLayout):

    """
    Գլխավոր էկրանն ա, նախատեսվում ա որպես այբուբենի էկրան, առայժմ ռանդոմ վիդջթներ են քցած
    """

    instance = ObjectProperty()
    source = StringProperty()
    text = StringProperty()
    method = ObjectProperty()


class MainWindow(MDBoxLayout):
    
    pass


class Database:
    dictionary = {
    'instagram': 'img/giphy.gif',
    'twitter' : 'img/twitter.gif',
    'test' : 'img/twitter.gif',
    }



class CallBacks(Database):

    def change_to_favorite_screen(self, instance):

        """Սոբստվեննո, կանչում ա են մանրամասն ինֆո նկարող կլասսը, տալիս ա ինչ իրան պետք ա, առայժմ մենակ գիֆն ա ու տեքստ"""

        text = instance.text
        source = self.dictionary[text]

        self.root.ids.item_3_manager.current = 'favorite_more'

        self.root.ids.favorite_more_screen.add_widget(ItemScreenDrawer(text = text, source = source))

    def change_to_item_screen(self, instance):

        """Լրիվ նույն ֆունկցիան ա, բացառությամբ, որ ֆավորտների էջում ա նկարում, աշխատում ա մի կերպ"""

        print("********************************************",'\n' ,instance)

        text = instance.text
        source = self.dictionary[text]

        self.root.ids.first_screen_manager.current = 'item_screen'

        screen = ItemScreenDrawer(text = text, source = source)
        button = Button(text = 'favorite')
        button.bind(on_release = lambda x: self.favorite(instance))
        screen.add_widget(button)

        self.root.ids.more_screen.add_widget(screen)

        

class MainApp(MDApp, CallBacks):

    def favorite(self, instance):

        """Նկարում ա օբշի ֆավորիտների էջը"""

        print(instance)
        return self.root.ids.favorites.add_widget(CardsDrawer(instance = self, source = instance.source, text = instance.text, method = self.change_to_favorite_screen))

    def on_start(self):

        """Պռոստը սկիզբն ա"""

        prkeq = """

        Կոդը ռան անելուց առաջ համոզվեք, որ աղոթել եք

            ************

        Հայր մեր որ յերկինս ես,
        սուրբ եղիցի անուն Քո։
        Եկեսցէ արքայութիւն Քո։
        Եղիցին կամք Քո
        որպէս յերկինս եւ յերկրի։
        Զհաց մեր հանապազորդ
        տուր մեզ այսօր։
        Եւ թող մեզ զպարտիս մեր,
        որպէս եւ մեք թողումք մերոց պարտապանաց։
        Եւ մի տանիր զմեզ ի փորձութիւն
        այլ փրկեա զմեզ ի չարէ։
        Զի քո է արքայութիւն
        եւ զօրութիւն եւ փառք յաւիտեանս
        Ամէն
        """

        print(prkeq)

        for item in self.dictionary:

            source = self.dictionary[item]

            self.root.ids.images.add_widget(CardsDrawer(instance = self, source = source, text= item, method = self.change_to_item_screen))




    def build(self):
        self.title = 'LearnApp'
        self.theme_cls.primary_palette = "BlueGray"  # "Purple", "Red"
        self.icon = 'Mobile-icon.png'
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()