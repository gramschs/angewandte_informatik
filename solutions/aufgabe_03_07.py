# Aufgabe 3.7 (nach Weigend, Python 3, Kapitel 5)
#
# Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), Rubidium (Rb), Caesium (Cs). Schreiben Sie ein
# Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines chemischen Elementes an. Anschließend wird
# gemeldet, ob es sich um ein Alkalimetall handelt oder nicht.
#
# Beispieldialog:
#
# Bitte geben Sie die Formel eines chemischen Elementes an. Element: Na
# Es handelt sich um ein Alkalimetall.

# Eingabe
chemische_formel = input('Bitte geben Sie die Formel Ihres chemischen Elementes an: ')

# Ausgabe
if chemische_formel == 'Li':
    print(chemische_formel, 'ist ein Alkalimetall.')
elif chemische_formel == 'Na':
    print(chemische_formel, 'ist ein Alkalimetall.')
elif chemische_formel == 'K':
    print(chemische_formel, 'ist ein Alkalimetall.')
elif chemische_formel == 'Rb':
    print(chemische_formel, 'ist ein Alkalimetall.')
elif chemische_formel == 'Cs':
    print(chemische_formel, 'ist ein Alkalimetall.')
else:
    print(chemische_formel, 'ist *kein* Alkalimetall.')



