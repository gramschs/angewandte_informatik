'''
Aufgabe 11.4

Schreiben Sie ein Programm, bei dem der Benutzer über zwei Drop-Down-Listen den Tag und den Monat seines Geburtstages
auswählt. Lassen Sie den Computer danach feststellen, ob der Benutzer dieses Jahr schon Geburtstag hatte, heute gerade
Gebutstag hat (Gratulation) oder noch Geburtstag haben wird. Geben Sie eine entsprechende Meldung aus.
'''
from ipywidgets import interact
import ipywidgets as widgets

def berechne_geburtstag(tag, monat):
    heutiger_tag = 24
    heutiger_monat = 6
    if monat < heutiger_monat:
        print('Sie hatten schon Geburtstag.')
    elif monat == heutiger_monat:
        if tag < heutiger_tag:
            print('Sie hatten schon Geburtstag.')
        elif tag == heutiger_tag:
            print('Happy Birthday :-)')
        else:
            print('Sie werden dieses Jahr noch Geburtstag haben...')
    else:
        print('Sie werden dieses Jahr noch Geburtstag haben...')


interact(berechne_geburtstag,
         tag=widgets.Dropdown(
             options=range(1, 32),
             value=1,
             description='Tag:'),
         monat=widgets.Dropdown(
             options=range(1, 13),
             value=1,
             description='Monat:'
         ));