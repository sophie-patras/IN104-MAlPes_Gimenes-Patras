from kivy.app import App

class AssistanceGps():
    def run(self): #lance le gps 
        #on fait clignoter le marqueur gps
        clignotant_gps=App.get_running_app().root.ids.cairn.ids.clignotant
        clignotant_gps.clignote()
        #on demande permission d'activer le gps
        pass 
