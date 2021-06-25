'''
Aufgabe 11.3

Schreiben Sie eine Funktion, die das Geburtsjahr eines Benutzers über ein Edit Field abfragt und danch das Alter
berechnet und ausgibt.
'''
from ipywidgets import interact
import ipywidgets as widgets

def berechne_alter(geburtsjahr):
    alter = 2021 - geburtsjahr
    print('Sie sind {} Jahre alt.'.format(alter))

interact(berechne_alter,
         geburtsjahr = widgets.IntText(value=2000, description='Geburtsjahr:' ));