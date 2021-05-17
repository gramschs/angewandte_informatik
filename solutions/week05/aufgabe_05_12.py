'''
Aufgabe 5.12

Schreiben Sie eine Funktion, die als Input einen Integer N entgegen nimmt und dann eine Liste von N Zufallszahlen
zwischen 1 und 100 ausgibt. Testen Sie anschließend diese Funktion.

Tipp: die Funktion randint(a,b) generiert eine Zufallszahl zwischen a und b. Allerdings müssen vorher die Zufalls-
funktionen aus dem Modul random geladen werden, also from random import * ausgeführt werden.
'''
from random import *

def generiere_zufallszahlen(anzahl):

    for i in range(anzahl):
        zufallszahl = randint(1,100)
        print(zufallszahl)
