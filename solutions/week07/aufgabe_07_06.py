'''
Aufgabe 7.6

Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), Rubidium (Rb), Caesium (Cs). Schreiben Sie ein
Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines chemischen Elementes an. Anschließend wird gemeldet,
ob es sich um ein Alkalimetall handelt oder nicht.

Verwenden Sie diesmal eine Liste mit den Alkalimetallen.
'''
# Eingabe
eingabe = input('Bitte geben Sie Ihr chemisches Element ein: ')

# Ausgabe
if eingabe in ['Li', 'Na', 'K', 'Rb', 'Cs']:
    print('{} ist ein Alkalimetall.'.format(eingabe))
else:
    print('{} ist *kein* Alkalimetall.'.format(eingabe))

