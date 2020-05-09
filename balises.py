from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Balises(MapMarkerPopup):

	source = "icone_maison_mini.png" #dimensions adaptées
	#point_data=[]

	def on_release(self):
		#ouvrir menu infos
		#menu = InfosPopup(self.point_data)
		menu= CustomPopup(title="Caractéristiques du refuge")
		menu.size_hint = [.6, .7]
		menu.open()

class CustomPopup(Popup):
	
	""" Utile en fonction de la taille du popup : bouton pour fermer popup, completer aussi le .kv
	def dismiss_popup(self):
        	#femetue du popup
        	self.dismiss()"""

Builder.load_file("balises.kv")
