from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class AssistanceGps():
    has_centered_map= False 
    def run(self):
        #on lance le point qui clignote 
        clignotant_gps=App.get_running_app().root.ids.cairn.ids.clignotant
        clignotant_gps.clignote()
        #on demande permission d'activer le gps
        if platform == 'android': 
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Toutes autorisations obtenues")
                else:
                    print("pas toutes les autorisations")
            request_permissions([Permission.ACCES_COARSE_LOCATION, Permission.ACCES_FINE_LOCATION],callback)
        #Configurer le GPS
        if platform == 'android' or platform == 'ios':
            from plyer import gps 
            gps.configure(on_location=self.maj_pos_clignotant,on_status=self.autorise)
            gps.start(minTime=1000,minDistance=0)
    def maj_pos_clignotant(self,*args,**kwargs):
        ma_lat= kwargs['lat'] #les coordonnées du point GPS 
        ma_lon= kwargs['lon']
        print("GPS POSITION", ma_lat, ma_lon)
        clignotant_gps=App.get_running_app().root.ids.cairn.ids.clignotant
        clignotant_gps.lat=ma_lat #on met le point clignotant au bon endroit sur la carte 
        clignotant_gps.lon=ma_lon
        if not self.has_centered_map:
            map= App.get_running_app().root.ids.cairn
            map.center_on(ma_lat,ma_lon) # si ce n'est pas déjà fait, on centre la carte sur la localisation GPS 
            self.has_centered_map= True 
    def autorise(self, status, status_message):
        if status == 'provider-enabled':
            pass
        else:
            self.ouvrir_gps()
    def ouvrir_gps(self):
        dialog= MDDialog(title="Erreur GPS", text="Vous devez autoriser l'acces GPS") #fenêtre de dialogue qui demande l'activation GPS
        dialog.size_hint= [.8, .8]
        dialog.pos_hint= {'center_x':.5,'center_y':.5}
        dialog.open()
