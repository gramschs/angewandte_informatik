'''
Aufgabe 6.4 Zahlenraten

Schreiben Sie ein Programm, bei dem der Computer sich eine Zahl zwischen 1 und 100 ausdenkt (d.h. eine Zufallszahl
zieht). Anschließend wird der Benutzer aufgefordert, die Zahl zu raten. Wenn die Zahl des Benutzers kleiner als die
Zufallszahl des Computer ist, so gibt er den Hinweis: "Meine Zahl ist größer.". Wenn die Zahl des Benutzers größer
ist als die Zufallszahl des Computers, so gibt er den Hinweis "Meine Zahl ist kleiner." Sobald der Benutzer die Zahl
richtig geraten hat, gibt der Computer den Hinweis "Gratulation, die Zahl xx ist richtig! Sie haben xx Versuche
gebraucht, um meine Zahl zu raten.", wobei 'xx' jeweils durch die richtigen Zahlen ersetzt wird.
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

