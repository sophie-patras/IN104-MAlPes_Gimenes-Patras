
from kivy.garden.mapview import MapMarkerPopup
from menudialog import ListMDDialog

class Balises(MapMarkerPopup):

	source = "icone_maison_mini.png" #dim fixes, voir dans MapMarkerPopup pour moduler
	data=[]

	def on_release(self):
		menu= Caracteristiques(self.data)
		menu.title="Caractéristiques du refuge"
		menu.size_hint = [.5, .8]
		menu.open()

class Caracteristiques(ListMDDialog):
	

	def __init__(self, data):
		super().__init__()

		intitules=["id_point","nom","categorie","altitude","latitude","longitude","etat","nombredeplace"]
		setattr(self,"nombredeplace", data[-1])
		
		for i in range(len(intitules)-2):
            		attribute_name = intitules[i]
            		attribute_value = data[i]
            		setattr(self, attribute_name, attribute_value)
