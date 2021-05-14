'''
Aufgabe 2.7 Fläche und Umfang eines Kreises

Schreiben Sie ein Programm, das den Benutzer nach dem Radius eines Kreises fragt und anschließend Fläche und Umfang des
Kreises ausgibt.
'''

# Module nachladen
from math import *


# Eingabe
radius = float(input('Bitte geben Sie den Radius in mm an: '))

# Verarbeitung
A = pi * radius**2
U = 2 * pi * radius

# Ausgabe
print('Die Fläche des Kreise ist {0:.2f} mm^2.'.format(A))
print('Der Umfang des Kreises ist {0:.4f} mm. '.format(U))


