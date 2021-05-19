'''
Aufgabe 6.1

Wie lange muss man einen Würfel werfen, bis (zum ersten Mal) eine 6 erscheint?

1. Schreiben Sie eine *Funktion*, die so lange würfelt, bis eine 6 erschienen ist. Als Rückgabe gibt die Funktion die
Anzahl der Würfe zurück.

2. Schreiben Sie anschließend ein *Programm*, bei dem ein Benutzer eingeben darf, wie oft der Würfelversuch in Schritt 1
durchgeführt werden soll. Anschließend wird die Funktion aus Schritt 1 so oft ausgeführt, wie vom Benutzer angegeben.
Zuletzt wird der Mittelwert der Würfelversuche berechnet und ausgegeben.

Beispiel:

* Computer: "Wie oft soll der Würfelversuch durchgeführt werden?
* Benutzer: 7
* Computer: "Im Durchschnitt wurde nach 6,7 maligem Würfeln das erste Mal eine 6 gewürfelt."
'''

from random import *


# FUNKTION
def wuerfeln_bis_sechs():
    anzahl_wuerfe = 0
    wurf = randint(1, 6)
    while wurf != 6:
        anzahl_wuerfe = anzahl_wuerfe + 1
        wurf = randint(1, 6)

    return anzahl_wuerfe


# PROGRAMM
# Eingabe
anzahl_versuche = int(input('Wie oft sollen die Würfelversuche durchgeführt werden? '))

# Verarbeitung
summe_versuche = 0
for i in range(anzahl_versuche + 1):
    summe_versuche = summe_versuche + wuerfeln_bis_sechs()
mittelwert = summe_versuche / anzahl_versuche

# Ausgabe
print('Im Durchschnitt wurde nach {} maligem Würfeln eine 6 gewürfelt.'.format(mittelwert))