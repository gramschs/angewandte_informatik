'''
Aufgabe 7.1

Schreiben Sie Code, der Ihren Vornamen abfragt und anschließend die Länge Ihres Vornamens bestimmt. Dann gibt das
Programm den Buchstaben aus, der als erstes im Alphabet vorkommt. Schreiben Sie einmal Ihren Namen komplett klein, also
z.B. "alice" und beim zweiten Mal mit großem Anfangsbuchstaben, also z.B. "Alice". Was beobachten Sie?
'''

# Eingabe
name = input('Wie heißen Sie mit Vornamen? ')

# Ausgabe
print('Der erste Buchstabe, der im Alphabet vorkommt, ist: {}'.format(min(name)))