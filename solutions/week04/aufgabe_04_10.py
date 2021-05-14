'''
Aufgabe 4.10

Schreiben Sie ein Programm, welches die folgende Ausgabe bis zu einer vom Benutzer gewählten Zahl fortsetzt:

1 *
2 **
3 ***
4 ****
5 *****
6 ******
7 *******

Zusatz: Passen Sie das Programm so an, dass es einen Weihnachtsbaum aus Sternchen zeichnet, dessen Höhe vom Benutzer
gewählt werden kann.
'''

# Eingabe
anzahl_zeilen = int(input('Wie viele Zeilen mit Sternen sollen gezeichnet werden? '))
weihnachtsbaum_zeichnen = input('Soll ein Weihnachtsbaum gezeichnet werden (j/n)? ')

# Ausgabe
zeile = 1
while zeile <= anzahl_zeilen:
    if weihnachtsbaum_zeichnen == 'j':
        print((anzahl_zeilen - zeile) * ' ', zeile * '*', zeile, zeile * '*')
    else:
        print(zeile, zeile * '*')
    zeile = zeile + 1

if weihnachtsbaum_zeichnen == 'j':
    print((anzahl_zeilen - 1) * ' ', '*****')
    print((anzahl_zeilen - 1) * ' ', '*****')