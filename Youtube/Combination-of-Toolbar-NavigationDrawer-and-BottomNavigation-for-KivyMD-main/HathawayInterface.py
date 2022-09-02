from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.properties import StringProperty, ListProperty
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

#Librería de fecha y hora
from datetime import date

#Tamaño de la ventana
from kivy.core.window import Window
Window.size=(800, 480)

#Manda a llamar al archivo que tiene el diseño
from HathawayDesign import HathawayDesign

#Clases para el menú de Navegación y la Botonera
class ContentNavigationDrawer(BoxLayout):
	pass

class DrawerList(ThemableBehavior, MDList):
	pass

#Clase que construye el diseño
class HathawayInterface(MDApp):
	#SCREEN DE INICIO
	#Variable que contiene la fecha y hora a la que se corre el programa
	tiempo = time.asctime()

	#SCREEN DE DIAGNÓSTICO

	#SCREEN DE MODO MANUAL
	#Variable entera para la aceleración
	modo_manual_aceleracion = 55
	#Variable string para escribir en la pantalla
	modo_manual_aceleracion_escritura = str(modo_manual_aceleracion)
	#Variable entera para la batería
	modo_manual_bateria = 10
	#Variable string para escribir en la pantalla
	modo_manual_bateria_escritura = str(modo_manual_bateria)

	#SCREEN DE RESET
	def Reset(self):
		print('Valor aceleración',self.modo_manual_aceleracion)

	#Construye el diseño
	def build(self):
		return Builder.load_string(HathawayDesign)

	#Cambia el estilo del Toolbar
	def on_start(self):
		self.theme_cls.primary_palette = "Indigo"
		self.root.ids.toolbar.ids.label_title.font_style = 'H5'

#Compila ambos códigos
HathawayInterface().run()
