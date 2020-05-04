from kivy.garden.mapview import MapMarker 
from kivy.animation import Animation

class ClignoteGps(MapMarker):
    def clignote(self):
        #faire clignoter le point gps
        anim=Animation(opacite_ext=0, taille_clignotant=30)
        anim.bind(on_complete=self.reinit)
        anim.start(self)
    def reinit(self,*args):
        self.opacite_ext=1
        self.taille_clignotant=self.taille_clignotant_defaut
        self.clignote()