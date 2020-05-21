from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App 
from epingle import Epingle

epingles=[]

class PopupMenuRecherche(MDInputDialog):
    title= 'Recherche depuis une adresse' #on paramètre la fenêtre popup de recherche
    text_button_ok= 'Rechercher'

    def __init__(self):
        super().__init__()
        self.size_hiny= [0.5,0.5]
        self.events_callback= self.callback 
    def callback(self, *args): #permet a l'utilisateur de rentrer sa recherche dans la barre 
        adresse= self.text_field.text #adresse=ce que l'utilisateur rentre dans la barre de recherche
        self.geocode_lat_lon(adresse)

    def geocode_lat_lon(self,adresse): #obtenir les coordonnees gps a partir de l'adresse 
        app_key="GseeKMRgPOhTra4f20ebIPP8z1cFrxzIBKnINSFNoXs" #paramètres fournies par HERE, propre à notre application
        app_id="nT0wI2ChLX2pRB9H9PVE"
        adresse=parse.quote(adresse)
        url= "https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=%s"%(adresse, app_key) #la requête de HERE
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)
    
    def success(self,urlrequest,result): #lorsque l'url est bien lu  
        if (len(result['items'])==0):
            return ("Erreur de saisie") #si le geocoder ne trouve pas de lieu correspondant à l'adresse, on ne fait rien
        latitude=result['items'][0]['position']['lat'] #positions de lat et lon dans la réponse de HERE
        longitude=result['items'][0]['position']['lng']
        app=App.get_running_app()
        mapview = app.root.ids.cairn 
        mapview.center_on(latitude,longitude) # on centre la carte sur le résultat de recherche
        epingle=Epingle(lat=latitude,lon=longitude) #on crée le widget de l'épingle 
        epingles.append(epingle)
        if len(epingles)>1: #on s'assure de ne pas garder les epingles des recherches precedentes 
            mapview.remove_widget(epingles[0])
            del epingles[0]
        epingle=epingles[0]
        mapview.add_widget(epingle) #on ajoute l'épingle sur la carte 
        print("Success")
        print(result)

    def failure(self,urlrequest,result):
        print("Failure")
        print(result)

    def error(self,urlrequest,result):
        print("Error")
        print(result)
