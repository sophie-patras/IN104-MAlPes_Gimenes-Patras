
import kivy
kivy.require('1.0.6')
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty,ObjectProperty

from carto_refuges import CartoRefuges
from assistancegps import AssistanceGps
from popupmenurecherche import PopupMenuRecherche
import sqlite3

class ItemDrawer(OneLineIconListItem):
    icon=StringProperty()

class ContentNavigationDrawer(BoxLayout):
    screen_manager=ObjectProperty()
    nav_drawer=ObjectProperty()

class DrawerList(ThemableBehavior,MDList):
    def set_color_item(self,instance_item):
        #appelée quand on appuie sur un item du menu 
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break 
        instance_item.text_color=self.theme_cls.primary_color

class MalpesApp(MDApp):
	connection = None
	cursor= None
	menu_recherche = None 

	def on_start(self):
		#Initialisation du GPS
		AssistanceGps().run()
		# Connection la base de donnee
		self.connection= sqlite3.connect("points_refuges.db")
		self.cursor= self.connection.cursor()

		# Initialiser le menu de recherche
		self.menu_recherche= PopupMenuRecherche()


if __name__ == "__main__":
	MalpesApp().run()
