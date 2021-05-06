'''
Aufgabe 4.12

Aufgabe 3.7 lautete:

Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), Rubidium (Rb), Caesium (Cs). Schreiben Sie ein
Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines chemischen Elementes an. Anschließend wird gemeldet,
ob es sich um ein Alkalimetall handelt oder nicht.

Schreiben Sie Ihr Programm aus Aufgabe 3.7 so um, dass nur noch _eine_ if - else - Struktur ohne elif verwendet wird,
indem Sie logische Operatoren einsetzen.
'''

# Eingabe
chemische_formel = input('Bitte geben Sie die Formel Ihres chemischen Elementes an: ')

# Ausgabe
if (chemische_formel == 'Li') or (chemische_formel == 'Na') or (chemische_formel == 'K') or (chemische_formel == 'Rb') \
        or (chemische_formel == 'Cs'):
    print(chemische_formel, 'ist ein Alkalimetall.')
else:
    print(chemische_formel, 'ist *kein* Alkalimetall.')



