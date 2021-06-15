'''
Aufgabe 9.2

Hier ist eine Tabelle mit den Zugriffszahlen auf das MATLAB Live Script in der Vorlesung angewandte Informatik im
Sommersemester 2021. Bitte stellen Sie die Daten als Balkendiagramm inklusive Beschriftungen dar.

Woche	Anzahl Nutzer/innen
3	9
4	17
5	15
6	10
7	11

'''
from matplotlib.pylab import *

# Eingabe der Daten
x = [3, 4, 5, 6, 7]
y = [9, 17, 15, 10, 11]

# Ausgabe als Balkendiagramm
bar(x,y)
xlabel('Woche')
ylabel('Anzahl Nutzer/innen')
title('Zugriffszahlen MATLAB Live Script SoSe 2021')
show()