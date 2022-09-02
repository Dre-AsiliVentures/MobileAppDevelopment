HathawayDesign = """
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: 'vertical'
    padding: "1dp"
    spacing: "1dp"
    Image:
        id: avatar
        source: "images/teslaprueba.png"
        height: dp(30)
    MDLabel:
        text: "   Abraham Lincoln medía 1.93 m"
        pos_hint: {'center_y':0.3}
        font_size: '10'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "   Diseñadores del Control"
        pos_hint: {'center_y':0.3}
        font_style: "H6"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:
        DrawerList:
            id: md_list
            MDList:
                OneLineIconListItem:
                    text: "Lucio de la Rosa Mitre"
                    font_size: '10'
                    IconLeftWidget:
                        icon: "controller-classic-outline"
                OneLineIconListItem:
                    text: "Jesús R. Gaitán Castellanos"
                    font_size: '10'
                    IconLeftWidget:
                        icon: "controller-classic-outline"
    MDLabel:
        text: "   Diseñadores de la Interfaz"
        pos_hint: {'center_y':0.3}
        font_style: "H6"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:
        DrawerList:
            id: md_list
            MDList:
                OneLineIconListItem:
                    text: "Luis A. Marin Bello"
                    IconLeftWidget:
                        icon: "code-braces"
                OneLineIconListItem:
                    text: "Victor Hernández Manrique"
                    IconLeftWidget:
                        icon: "code-braces"

Screen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: 'menu'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: toolbar
                        title: 'HMI AGV Tec #2 by Hathaway'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    MDBottomNavigation:
                        panel_color: .15, .15, .15, 1
                        text_color_active: .9, .9, .9, 1
                        text_color_normal: 0.12, 0.58, 0.94, 1
                        MDBottomNavigationItem:
                            name: 'P1'
                            text: 'Inicio'
                            icon: 'home'
                            MDGridLayout:
                                cols: 2
                                size: root.width, root.height
                                Image:
                                    source: 'images/tec_borrego.png'
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    MDLabel:
                                        text: "INICIO"
                                        font_name: 'Roboto'
                                        bold: True
                                        font_size: "60"
                                        halign: "center"
                                        pos_hint: {'center_y':0.9}
                                        theme_text_color: "Custom"
                                        text_color: 0, 0, 0, 1
                                    MDLabel:
                                        text: "En esta página encontrarás información de las opciones del control a tu disposición."
                                        font_name: 'Roboto'
                                        font_size: "17"
                                        halign: "center"
                                        pos_hint: {'center_y':0.9}
                                        theme_text_color: "Custom"
                                    MDGridLayout:
                                        cols: 2
                                        rows: 1
                                        MDLabel:
                                            text: "INICIO DE PROGRAMA"
                                            bold: True
                                            font_size: "20"
                                            halign: "center"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                        MDBoxLayout:
                                            orientation: 'vertical'
                                            MDLabel:
                                                text: "Fecha y hora de compilación."
                                                font_size: "15"
                                                italic: True
                                            TextInput:
                                                text: app.tiempo                    #Manda a llamar a la variable "tiempo" que se encuentra en la clase HathawayInterface(MDApp):
                                                halign: "center"
                                                valign: 'middle'
                                                multiline: True
                                                pos_hint: {'center_y':0.5}
                                    MDGridLayout:
                                        cols: 2
                                        rows: 1
                                        MDLabel:
                                            text: "DIAGNÓSTICO"
                                            bold: True
                                            font_size: "20"
                                            halign: "center"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                        MDLabel:
                                            text: "Envía data de los frenos o     la aceleración al AGV."
                                            font_size: "15"
                                            halign: "left"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                    MDGridLayout:
                                        cols: 2
                                        rows: 1
                                        MDLabel:
                                            text: "MODO MANUAL"
                                            bold: True
                                            font_size: "20"
                                            halign: "center"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                        MDLabel:
                                            text: "Permite la conducción     guiada por operador."
                                            font_size: "15"
                                            halign: "left"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                    MDGridLayout:
                                        cols: 2
                                        rows: 1
                                        MDLabel:
                                            text: "RESET"
                                            bold: True
                                            font_size: "20"
                                            halign: "center"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                        MDLabel:
                                            text: "En caso de emergencia, reinicia la comunicación."
                                            font_size: "15"
                                            halign: "left"
                                            pos_hint: {'center_y':0.9}
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                        MDBottomNavigationItem:
                            name: 'P2'
                            text: 'Diagnóstico'
                            icon: 'car-cog'
                            MDGridLayout:
                                cols: 5
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'Modo Manual'
                            icon: 'steering'
                            BoxLayout:
                                MDLabel:
                                    text: "MODO MANUAL"
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: "60"
                                    halign: "center"
                                    pos_hint: {'center_y':0.9}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                            MDGridLayout:
                                pos_hint:{"top":0.9}
                                cols:2
                                MDLabel:
                                MDLabel:
                                MDLabel:
                                    text:'ACELERACIÓN'
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: "30"
                                    halign:'center'
                                    pos_hint:{'center_y': 0.9}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    text:'BATERÍA'
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: "30"
                                    halign:'center'
                                    pos_hint:{'center_y': 0.9}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    text: app.modo_manual_aceleracion_escritura
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: "60"
                                    halign:'center'
                                    pos_hint:{'center_y': 0.9}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    text: app.modo_manual_bateria_escritura
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: "60"
                                    halign:'center'
                                    pos_hint:{'center_y': 0.9}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    text:'(km/h)'
                                    font_name: 'Roboto'
                                    italic: True
                                    font_size: "30"
                                    valigh: 'top'
                                    halign:'center'
                                    pos_hint:{'center_y': 0.5}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    text:'(%)'
                                    font_name: 'Roboto'
                                    italic: True
                                    font_size: "30"
                                    valigh: 'top'
                                    halign:'center'
                                    pos_hint:{'center_y': 0.5}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                                MDLabel:
                                    md_bg_color: 0, 0, 0, 1
                        MDBottomNavigationItem:
                            name: 'screen 4'
                            text: 'Reset'
                            icon: 'reload-alert'
                            BoxLayout:
                                MDLabel:
                                    text: "RESET"
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: '60'
                                    halign: 'center'
                                    valign: 'middle'
                                    pos_hint: {'center_y':0.5}
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                Button:
                                    text: 'EMERGENCIA'
                                    font_name: 'Roboto'
                                    bold: True
                                    font_size: '40'
                                    halign: 'center'
                                    valign: 'middle'
                                    background_color: (1,0,0,1)
                                    on_release:
                                        app.Reset()
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                id: content_drawer
"""
