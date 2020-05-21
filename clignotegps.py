from kivy.garden.mapview import MapMarker 
from kivy.animation import Animation

class ClignoteGps(MapMarker):
    def clignote(self):
        #faire clignoter le point gps
        anim=Animation(opacite_ext=0, taille_clignotant=30) #on change l'opacité et la taille du cercle
        anim.bind(on_complete=self.reinit) #quand le cercle a atteint sa taille maximale, on le réinitialise
        anim.start(self) 
    def reinit(self,*args):
        self.opacite_ext=1
        self.taille_clignotant=self.taille_clignotant_defaut #réinitialisation du cercle à sa taille de départ
        self.clignote()
