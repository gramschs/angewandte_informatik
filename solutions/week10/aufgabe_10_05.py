'''

'''
from random import randint

def bestimme_anzahl_aufgaben():
    antwort = input('Wie viele Aufgaben sollen gestellt werden? ')
    # Die Antwort muss eine positive ganze Zahl sein => wir benutzen die String-Methode .isdigit()
    while not antwort.isdigit():
        antwort = input('Bitte geben Sie eine positive ganze Zahl ein. Wie viele Aufgaben sollen gestellt werden? ')
    return int(antwort)


def stelle_einmaleins_aufgaben(anzahl_aufgaben):
    anzahl_richtige_aufgaben = 0
    for i in range(anzahl_aufgaben):
        # Eingabe
        a = randint(1, 10)
        b = randint(1, 10)
        ergebnis = int(input('Was ist {} x {} ??? '.format(a, b)))

        # Verarbeitung
        if ergebnis == a * b:
            print('Richtig!')
            anzahl_richtige_aufgaben += 1
        else:
            print('Leider falsch, das richtige Ergebnis wäre ', a * b)

        print('anzahl_richtige_aufgaben = ', anzahl_richtige_aufgaben)

    return anzahl_richtige_aufgaben


# main
# Eingabe
anzahl_aufgaben = bestimme_anzahl_aufgaben()

# Verarbeitung
anzahl_richtige_aufgaben = stelle_einmaleins_aufgaben(anzahl_aufgaben)
prozent = anzahl_richtige_aufgaben / anzahl_aufgaben * 100

# Ausgabe
print('Sie haben {} von {} Aufgaben richtig gelöst, das sind {} %.'.format(anzahl_richtige_aufgaben, anzahl_aufgaben, prozent))
