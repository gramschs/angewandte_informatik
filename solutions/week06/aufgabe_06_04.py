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

computer_zahl = randint(1, 100)

zahl = int(input('Raten Sie: '))
anzahl_versuche = 1
while zahl != computer_zahl:
    if zahl < computer_zahl:
        print('Meine Zahl ist größer. ')
        zahl = int(input('Raten Sie: '))
    else:
        print('Meine Zahl ist kleiner. ')
        zahl = int(input('Raten Sie: '))
    anzahl_versuche = anzahl_versuche + 1

print('Gratulation, die Zahl {} ist richtig. Sie haben {} Versuche gebraucht.'.format(zahl, anzahl_versuche))

