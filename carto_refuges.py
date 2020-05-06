from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.popup import Popup
#from kivy.lang.builder import Builder
from balises import Balises

class CartoRefuges(MapView):
	cairn_timer = None
	noms_points=[]	

	def debut_cairn_dans_champ(self):
		""" Apres 1 sec, fait apparaitre les markets dans fov. tres utile pour que l'app fasse pas 400 000 calculs a chaque fois qu'on bouge"""
		""" requete sql"""
		requete_sql = "SELECT * FROM points_refuges WHERE latitude > %s AND latitude< %s AND longitude< %s AND longitude> %s "%(min_lat, max_lat, max_lon, min_lon)
		app.cursor.execute(requete_sql)
		points_carto = app.cursor.fetchall() 	#on mettra d'autres balises que les refuges
		print(points_carto)
		for point in points_carto:
			nom = point[1]
			if nom in self.noms_points:
				continue
			else:
				self.affichage_cairn(point)

	def affichage_cairn(self, x):
		#creer une balise
		lat, lon = x[4],x[5]
		balise=Balises(lat=lat, lon=lon)
		balise.point_data=point
		# l'afficher
		self.add_widget(balise)		
		#Popup(title="Test", content=Label(text='x'),size_hint=(None,None), size=(200,200))
		#on ne veut pas supperposer les balises quand on bouge la carte
		nom=point[1]
		self.noms_points.append(nom) #pb si on sort du champ puis revient
