'''
Aufgabe 6.3
Schreiben Sie ein Programm, bei dem der Benutzer zuerst nach einer Funktion gefragt wird und dann danach, wie oft sie
abgeleitet werden soll. Lassen Sie anschließend Sympy die gewünschte Ableitung der Funktion berechnen und geben Sie das
Ergebnis auf dem Bildschirm aus.

Beispiel:

Welche Funktion soll abgeleitet werden?  7*x*sin(x)
Wie oft soll die Funktion abgeleitet werden? 1
7*x*cos(x) + 7*sin(x)
'''

from sympy import *

x = symbols('x')

funktion = input('Welche Funktion soll abgeleitet werden? ')
ordnung = int(input('Wie oft soll die Funktion abgeleitet werden?'))

if ordnung == 1:
    print(diff(funktion, x))
elif ordnung == 2:
    print(diff(funktion, x, x))
elif ordnung == 3:
    print(diff(funktion, x, x, x))
else:
    print('Höher als 3 geht nicht...')
