'''
Aufgabe 7.6

Schreiben Sie das Lotto-Programm (Aufgabe 5.14) neu. Lassen Sie das Programm zuerst sechs Zufallszahlen ziehen, die in
einer Liste gespeichert werden. Sobald die zweite, dritte Zufallszahl usw. in die Liste gespeichert werden soll, wird
erst überprüft, ob sie in der Liste schon vorhanden ist, damit keine Zahl doppelt vorkommt.

Tipp: wenn die Liste nach dem dritten Ziehen z.B. `l = [17, 3, 6]` lautet, kann durch den logischen Ausdruck `x in l`
überprüft werden, ob `x`schon in der Liste vorkommt (True) oder nicht (False).

Danach schreiben Sie eine Funktion, die sechs Wunsch-Zahlen vom Benutzer abfragt und in einer Liste speichert (auch hier
sind gleiche Zahlen nicht erlaubt). Zuletzt soll das Programm die Anzahl der richtigen Lottozahlen berechnen. Können Sie
dazu eine for-Schleife benutzen?
'''
from random import *

# Eingabe
def waehle_zahlen():
    zahlenliste = []
    for i in range(6):
        zahl = int(input('Bitte wählen Sie eine Lottozahl: '))
        while (zahl < 1) or (49 < zahl) or (zahl in zahlenliste):
            if zahl < 1:
                zahl = int(input('Die Zahl muss zwischen 1 und 49 liegen, bitte versuchen Sie es erneut: '))
            elif zahl > 49:
                zahl = int(input('Die Zahl muss zwischen 1 und 49 liegen, bitte versuchen Sie es erneut: '))
            else:
                print('Diese Zahlen haben Sie schon gewählt {}'.format(zahlenliste))
                zahl = int(input('Bitte wählen Sie eine andere Zahl: '))

        zahlenliste.append(zahl)

    return zahlenliste

def ziehe_lottozahlen():
    lottozahlen_liste = []
    for i in range(6):
        zahl = randint(1,49)
        while zahl in lottozahlen_liste:
            zahl = randint(1,49)
        lottozahlen_liste.append(zahl)

    return lottozahlen_liste

def berechne_anzahl_richtige(benutzerzahlen, lottozahlen):
    anzahl_richtige = 0
    for z in benutzerzahlen:
        if z in lottozahlen:
            anzahl_richtige = anzahl_richtige + 1

    return anzahl_richtige

# HAUPTPROGRAMM

# Eingabe
benutzerzahlen = waehle_zahlen()

# Verarbeitung
lottozahlen = ziehe_lottozahlen()
anzahl_richtige = berechne_anzahl_richtige(benutzerzahlen, lottozahlen)

# Ausgabe
print('Sie haben die Zahlen {} gewählt. '.format(benutzerzahlen))
print('Der Computer hat die Lottozahlen {} gezogen.'.format(lottozahlen))
print('Das ist/sind {} richtige Zahl(en).'.format(anzahl_richtige))
