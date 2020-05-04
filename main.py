import kivy
kivy.require('1.0.6')
import sqlite3
from kivymd.app import MDApp
from carto_refuges import CartoRefuges
from assistancegps import AssistanceGps

class MainApp(MDApp):
    connection=None
    cursor=None 
    def on_start(self):
        #on initialisele GPS
        AssistanceGps().run()
        #On se connecte a la base de donnees 
        self.connection=sqlite3.connect("points_refuges.db")
        self.cursor=self.connection.cursor()

        #initialiser la recherche 
        pass 


MainApp().run()
