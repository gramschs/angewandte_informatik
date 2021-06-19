'''
Aufgabe 10.6

Was könnte folgender Code für einen Zweck haben?

siege_computer = 0
if wahl_computer == 'Stein':
    if wahl_benutzer == 'Stein':
        print('Unentschieden, ich hatte ebenfalls Stein.')
    elif wahl_benutzer == 'Schere':
        print('Punkt für mich, Stein schleift Schere.')
        siege_computer += 1
    else # wahl_benutzer == 'Papier'
        print('Punkt für Sie, Papier umwickelt Stein.')
        siege_benutzer +=1
Korrigieren sie die 4 Fehler.
'''

siege_computer = 0
siege_benutzer = 0
wahl_computer = 'Stein'
wahl_benutzer = 'Stein'
if wahl_computer == 'Stein':
    if wahl_benutzer == 'Stein':
        print('Unentschieden, ich hatte ebenfalls Stein.')
    elif wahl_benutzer == 'Schere':
        print('Punkt für mich, Stein schleift Schere.')
        siege_computer += 1
    else: # wahl_benutzer == 'Papier'
        print('Punkt für Sie, Papier umwickelt Stein.')
        siege_benutzer +=1

