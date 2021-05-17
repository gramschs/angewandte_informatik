'''
Aufgabe 5.14 Lotto

Schreiben Sie ein Programm, das zuerst den Benutzer sechs Zahlen zwischen 1 und 49 wählen lässt. Dabei soll das Programm
überprüfen, dass keine Zahl mehrfach eingegeben wird. Lassen Sie dann den Zufallszahlengenerator sechs Lottozahlen
zwischen 1 und 49 ziehen (Hinweis: randint(a,b) aus dem Modul random). Dabei darf ebenfalls keine Zufallszahl mehrfach
gezogen werden. Teilen Sie dem Benutzer anschließend mit, wie viele richtige Zahlen getippt wurden.
'''
from random import *

# Eingabe
def zahl_abfragen():
    zahl = int(input('Bitte geben Sie eine Zahl zwischen 1 und 49 ein: '))
    while zahl < 1 or zahl > 49:
        zahl = int(input('Bitte geben Sie eine Zahl zwischen 1 und 49 ein: '))
    return zahl

zahl1 = zahl_abfragen()
zahl2 = zahl_abfragen()
while zahl2 == zahl1:
    print('Sie haben die Zahl {} schon gewählt. Bitte wählen Sie eine andere Zahl. '.format(zahl1))
    zahl2 = zahl_abfragen()

zahl3 = zahl_abfragen()
while zahl3 == zahl2 or zahl3 == zahl1:
    print('Sie haben bereits die Zahlen {} und {} gewählt. Bitte wählen Sie eine andere Zahl. '.format(zahl1, zahl2))
    zahl3 = zahl_abfragen()

zahl4 = zahl_abfragen()
while zahl4 == zahl3 or zahl4 == zahl2 or zahl4 == zahl1:
    print('Sie haben bereits die Zahlen {}, {} und {} gewählt. Bitte wählen Sie eine andere Zahl. '.format(zahl1, zahl2, zahl3))
    zahl4 = zahl_abfragen()

zahl5 = zahl_abfragen()
while zahl5 == zahl4 or zahl5 == zahl3 or zahl5 == zahl2 or zahl5 == zahl1:
    print('Sie haben bereits die Zahlen {}, {}, {} und {} gewählt. Bitte wählen Sie eine andere Zahl. '.format(zahl1, zahl2, zahl3, zahl4))
    zahl5 = zahl_abfragen()

zahl6 = zahl_abfragen()
while zahl6 == zahl5 or zahl6 == zahl4 or zahl6 == zahl3 or zahl6 == zahl2 or zahl6 == zahl1:
    print('Sie haben bereits die Zahlen {}, {}, {}, {} und {} gewählt. Bitte wählen Sie eine andere Zahl. '.format(zahl1, zahl2, zahl3, zahl4, zahl5))
    zahl6 = zahl_abfragen()

# Verarbeitung

zufallszahl1 = randint(1, 49)
zufallszahl2 = randint(1, 49)
while zufallszahl2 == zufallszahl1:
    zufallszahl2 = randint(1, 49)
zufallszahl3 = randint(1, 49)
while zufallszahl3 == zufallszahl2 or zufallszahl3 == zufallszahl1:
    zufallszahl3 = randint(1, 49)
zufallszahl4 = randint(1, 49)
while zufallszahl4 == zufallszahl3 or zufallszahl4 == zufallszahl2 or zufallszahl4 == zufallszahl1:
    zufallszahl4 = randint(1, 49)
zufallszahl5 = randint(1, 49)
while zufallszahl5 == zufallszahl4 or zufallszahl5 == zufallszahl3 or zufallszahl5 == zufallszahl2 or zufallszahl5 == zufallszahl1:
    zufallszahl5 = randint(1, 49)
zufallszahl6 = randint(1, 49)
while zufallszahl6 == zufallszahl5 or zufallszahl6 == zufallszahl4 or zufallszahl6 == zufallszahl3 or zufallszahl6 == zufallszahl2 or zufallszahl6 == zufallszahl1:
    zufallszahl6 = randint(1, 49)

# Ausgabe
anzahl_richtige = 0
if zahl1 == zufallszahl1 or zahl1 == zufallszahl2 or zahl1 == zufallszahl3 or zahl1 == zufallszahl4 or zahl1 == zufallszahl5 or zahl1 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1
if zahl2 == zufallszahl1 or zahl2 == zufallszahl2 or zahl2 == zufallszahl3 or zahl2 == zufallszahl4 or zahl2 == zufallszahl5 or zahl2 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1
if zahl3 == zufallszahl1 or zahl3 == zufallszahl2 or zahl3 == zufallszahl3 or zahl3 == zufallszahl4 or zahl3 == zufallszahl5 or zahl3 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1
if zahl4 == zufallszahl1 or zahl4 == zufallszahl2 or zahl4 == zufallszahl3 or zahl4 == zufallszahl4 or zahl4 == zufallszahl5 or zahl4 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1
if zahl5 == zufallszahl1 or zahl5 == zufallszahl2 or zahl5 == zufallszahl3 or zahl5 == zufallszahl4 or zahl5 == zufallszahl5 or zahl5 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1
if zahl6 == zufallszahl1 or zahl6 == zufallszahl2 or zahl6 == zufallszahl3 or zahl6 == zufallszahl4 or zahl6 == zufallszahl5 or zahl6 == zufallszahl6:
    anzahl_richtige = anzahl_richtige + 1

print('Sie haben {} richtige Lottozahlen.'.format(anzahl_richtige))
print('Die 1. Lottozahl ist: {}'.format(zufallszahl1))
print('Die 2. Lottozahl ist: {}'.format(zufallszahl2))
print('Die 3. Lottozahl ist: {}'.format(zufallszahl3))
print('Die 4. Lottozahl ist: {}'.format(zufallszahl4))
print('Die 5. Lottozahl ist: {}'.format(zufallszahl5))
print('Die 6. Lottozahl ist: {}'.format(zufallszahl6))
