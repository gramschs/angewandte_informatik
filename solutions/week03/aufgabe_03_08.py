# Aufgabe 3.8
#
# Schreiben Sie ein Programm, welches eine Zeitangabe in Stunden, Minuten und Sekunden in die Anzahl Sekunden insgesamt
# umrechnet und ausgibt.


# Eingabe
print('Bitte geben Sie im folgenden die Stunden, Minuten und Sekunden ein.')
stunden  = int(input('Stunden: '))
minuten  = int(input('Minuten: '))
sekunden = int(input('Sekunden: '))

# Verarbeitung
zeit_in_sekunden = 3600 *  stunden + 60 * minuten + sekunden

# Ausgabe
print('Das entspricht {} Sekunden.'.format(zeit_in_sekunden))