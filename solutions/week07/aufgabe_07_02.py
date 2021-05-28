'''
Aufgabe 7.2 Vokale zählen

Schreiben Sie ein Programm, das den Benutzer bittet, ein Wort oder einen ganzen Satz einzugeben. Dann berechnet das
Programm, wie häufig Vokale (also A,E,I,O und U) darin vorkommen und gibt diese Anzahl aus.

Testen Sie Ihr Programm. Beispielablauf:


Computer: Bitte geben Sie ein Wort oder einen Satz ein:
Benutzer: Dies ist ein Test.
Computer: In Ihrer Eingabe sind 6 Vokale.

Funktioniert Ihr Programm auch bei dem Wort dem Wort Oase und gibt drei Vokale zurück?
'''

# Eingabe
eingabe = input('Bitte geben Sie ein Wort oder einen Satz ein: ')

# Verarbeitung
anzahl_vokale = 0
for zeichen in eingabe:
    if zeichen in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        anzahl_vokale = anzahl_vokale + 1

# Ausgabe
print('In Ihrer Eingabe kommen {} Vokale vor.'.format(anzahl_vokale))