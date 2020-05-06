from kivy.garden.mapview import MapMarkerPopup
from infos_popup import InfosPopup

#from kivy.uix.popup import Popup



class Balises(MapMarkerPopup):

	source = "icone_refuge.jpg" #retravailler sur le choix/dim des icones
	point_data=[]

	def on_release(self):
		#ouvrir menu infos
		menu = InfosPopup(self.point_data)
		menu.size_hint = [.9, .9]
		menu.open()
