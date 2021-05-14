'''
Aufgabe 5.4

Schreiben Sie ein Programm, das eine minimale Zahl $a$ und eine maximale Zahl $b$ abfragt. Dann berechnet das Programm
die Quadratzahlen von a^2 bis b^2 und gibt diese aus. Ein Beispiel könnte so aussehen: Der Benutzer gibt a = 4 und
b = 8 ein. Das Programm gibt daraufhin 16, 25, 36, 49, 64 aus. Bitte verwenden Sie eine for-Schleife.
'''

# Eingabe
a = int(input('Bitte geben Sie die minimale Zahl a ein: '))
b = int(input('Bitte geben Sie das Maximum b ein: '))

# Verarbeitung und Ausgabe
for zahl in range(a, b+1):
    print(zahl**2)
