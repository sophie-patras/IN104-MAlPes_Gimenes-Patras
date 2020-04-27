
from kivymd.app import MDApp
from carto_refuges import CartoRefuges
import sqlite3

class MainApp(MDApp):
	connection = None
	cursor= None

	def on_start(self):
		#Initialisation du GPS

		# Connection la base de donnee
		self.connection= sqlite3.connect("points_refuges.db")
		self.cursor= self.connection.cursor()

		# Paramétrage du SearchPopupMenu
		pass

MainApp().run()
