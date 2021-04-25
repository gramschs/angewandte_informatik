'''
Aufgabe 2.6 Hypotenuse im rechtwinkligen Dreieck

Schreiben Sie ein Programm, das den Benutzer zwei Seitenlängen für die beiden Katheten $a$ und $b$ eines rechtwinkligen
Dreiecks eingeben lässt. Anschließend berechnet das Programm die Länge der Hypotenuse nach dem Satz des Pythagoras
$a^2+b^2=c^2$ und gibt diese aus.

Bemerkung: Was passiert, wenn Sie eine negative Zahl eingeben?
'''
# Laden der notwendigen Module
from math import *

# Eingabe
a = float(input('Bitte geben Sie die Länge der Kathete a ein: '))
b = float(input('Bitte geben Sie die Länge der Kathete b ein: '))


# Verarbeitung
c = sqrt(a**2 + b**2)


# Ausgabe
print('Die Länge der Hypotenuse ist ', c)

