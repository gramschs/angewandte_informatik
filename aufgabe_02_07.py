'''
Aufgabe 2.7 Fläche und Umfang eines Kreises

Schreiben Sie ein Programm, das den Benutzer nach dem Radius eines Kreises fragt und anschließend Fläche und Umfang des
Kreises ausgibt.
'''
from math import pi
# Eingabe
radius = input('Bitte geben Sie den Radius des Kreises an: ')

# Verarbeitung
A = pi * radius * radius
U = 2 * pi * radius

# Ausgabe
print('Die Fläche ist: ', A)
print('Der Umfang ist: ', U)
