"""
Dialog
======
Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher
For suggestions and questions:
<kivydevelopment@gmail.com>
This file is distributed under the terms of the same license,
as the Kivy framework.
`Material Design spec, Dialogs <https://material.io/design/components/dialogs.html>`_



Version reprise et adaptée pour MAlPes par Lucille et Sophie"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

from kivymd.uix.card import MDCard
from kivymd.material_resources import DEVICE_IOS

from kivymd import images_path



Builder.load_string(
    """
#:import images_path kivymd.images_path

<ThinLabel@MDLabel>:
    size_hint: 1, None
    valign: 'middle'
    font_size: '13sp'
    height: self.texture_size[1]
    markup: True

<ThinLabelButton@ThinLabel+MDTextButton>:
    size_hint_y: None
    valign: 'right'
    height: self.texture_size[1]

<ThinBox@BoxLayout>:
    size_hint_y: None
    height: self.minimum_height
    padding: 70, 4, 4, 20

<ListMDDialog>
    title: ""
    halign : "center"
    BoxLayout:
        orientation: 'vertical'
        padding: 0,60,0,0
        spacing: dp(10)
    
        MDLabel:
            id: title
            text: root.title
            font_style: 'H5'
            halign: 'center'
            valign: 'top'
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
    
        ScrollView:
            id: scroll
            size_hint_y: None
            height:
                root.height - (title.height + dp(48)\
                + sep.height)
    
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    #source: '{}dialog_in_fade.png'.format(images_path)
                    source: '{}transparent.png'.format(images_path)
    
            MDList:
                id: list_layout
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(15)
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    Color:
                        rgba: [1,0,0,.5]   
                
                ThinBox:
                    ThinLabel:
                        text: "[b]Id_point: [/b]"
                    ThinLabel:
                        text: root.id_point
                ThinBox:
                    ThinLabel:
                        text: "[i]Nom : [/i]"
                    ThinLabel:
                        text: root.nom
                ThinBox:
                    ThinLabel:
                        text: "[i]Catégorie : [/i]"
                    ThinLabel:
                        text: root.categorie
                ThinBox:
                    ThinLabel:
                        text: "[i]Altitude: [/i]"
                    ThinLabel:
                        text: root.altitude
                ThinBox:
                    ThinLabel:
                        text: "[i]Nb de lits: [/i]"
                    ThinLabel:
                        text: root.nombredeplace

        MDSeparator:
            id: sep
"""
)

if DEVICE_IOS:
    Heir = BoxLayout
else:
    Heir = MDCard

class ListMDDialog(ModalView):
    #modalview pour open()
    id_point = StringProperty("Missing data")
    nom = StringProperty("Missing data")
    categorie = StringProperty("Missing data")
    altitude = StringProperty("Missing data")
    nombredeplace = StringProperty("Missing data")

    background = StringProperty('{}ios_bg_mod.png'.format(images_path))

