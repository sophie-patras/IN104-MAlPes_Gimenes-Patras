from kivymd.uix.dialog import ListMDDialog

"""
from kivy.uix.popup import Popup
from kivy.uix.label import Label
popup = Popup(title='Test popup', content=Label(text='Hello world'), size_hint=(None, None), size=(400, 400))
"""

class InfosPopup(ListMDDialog):


    def __init__(self, point_data):
        super().__init__()


        # définir les infos dispos
        headers= "id_point;nom;type;altitude;latitude;longitude;etat;nombredeplace"
        headers= headers.split(';')



        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = point_data[i]
            setattr(self, attribute_name, attribute_value)
