'''
Aufgabe 6.2 Training Einmaleins

1. Schreiben Sie eine *Funktion*, mit der das kleine Einmaleins geübt werden kann. Die Funktion soll als Eingabe die
Anzahl der gewünschten Aufgaben haben und als Ausgabe die Anzahl der richtigen Antworten. Innerhalb der Funktion sollen
dem Benutzer zufällige Einmaleins-Aufgaben gestellt werden. Es soll gleich eine Rückmeldung gegeben werden, ob das
Ergebnis richtig oder falsch ist und ggf. was das richtige Ergebnis gewesen wäre.

2. Schreiben Sie anschließend ein *Programm*, das den Benutzer fragt, wie viele 1x1-Aufgaben trainiert werden sollen.
Anschließend wird die Funktion aus Schritt 1 aufgerufen. Am Ende soll der Benutzer darüber informiert werden, wie viel
Prozent der Aufgaben richtig gelöst wurden.
'''

from random import randint


# FUNKTION
def stelle_einmaleins_aufgaben(anzahl_aufgaben):
    anzahl_richtigen_antworten = 0

    for i in range(anzahl_aufgaben):
        # Eingabe
        a = randint(1, 10)
        b = randint(1, 10)
        ergebnis = int(input('Was ist {} x {} ??? '.format(a, b)))

        # Verarbeitung
        if ergebnis == a * b:
            anzahl_richtigen_antworten += 1
            print('Richtig!')
        else:
            print('Leider falsch, das richtige Ergebnis wäre ', a * b)

    # Ausgabe bzw. Rückgabe
    return anzahl_richtigen_antworten


# PROGRAMM
# Eingabe
anzahl_aufgaben = int(input('Wie viele Aufgaben sollen gestellt werden? '))

# Verarbeitung
anzahl_richtige_aufgaben = stelle_einmaleins_aufgaben(anzahl_aufgaben)
prozent = anzahl_richtige_aufgaben / anzahl_aufgaben * 100

# Ausgabe
print('Sie haben {} von {} Aufgaben richtig gelöst, das sind {} %.'.format(anzahl_richtige_aufgaben, anzahl_aufgaben,
                                                                           prozent))