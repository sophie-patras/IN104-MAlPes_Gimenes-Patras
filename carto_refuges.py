
from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App

class CartoRefuges(MapView):
	cairn_timer = None

	def debut_cairn_dans_champ(self):
		""" Apres 1 sec, fait apparaitre les markets dans fov. tres utile pour que l'app fasse pas 400 000 calculs a chaque fois qu'on bouge"""
		try:
			self.cairn_timer.cancel()
		except:
			pass
	
		"""TRES IMPORTANT : fonction appelée après 1sec / gors parametre qui conditionne l'efficacite de notre App"""
		self.cairn_timer=Clock.schedule_once(self.cairn_dans_champ, 1)

	def cairn_dans_champ(self, *args):
		""" get_bbox donne long/lat des bords de la carte affichée, utile pour 	déterminer les 	marqueurs a afficher"""
		min_lat, min_lon, max_lat, max_lon= self.get_bbox()		
		""" reference au main et database cursor"""
		app=App.get_running_app()
		""" requete sql"""
		requete_sql = "SELECT * FROM points_refuges WHERE latitude > %s AND latitude< %s AND longitude< %s AND longitude> %s "%(min_lat, max_lat, max_lon, min_lon)
		app.cursor.execute(requete_sql)
		points_refuges = app.cursor.fetchall()
		print(points_refuges)

   

