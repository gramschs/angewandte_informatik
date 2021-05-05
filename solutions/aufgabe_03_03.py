# Aufgabe 3.3
# Schreiben Sie ein Programm, das nach dem 7-Tage-Inzidenzwert Ihrer Heimatstadt fragt. Wenn die Inzidenz größer als
# 100 ist, soll das Programm ausgeben: "Leider gibt es in Ihrer Stadt Ausgangsbeschränkungen". Wenn die Inzidenz größer
# als 165 ist, soll das Programm ausgeben "Zusätzlich müssen die Schulen schließen".

# Eingabe
inzidenz = float(input('Geben Sie bitte die 7-Tagesinzidenz Ihrer Heimatstadt an: '))

# Ausgabe
if inzidenz > 100:
    print('Leider gibt es in Ihrer Stadt Ausgangsbeschränkungen.')

if inzidenz > 165:
    print('Zusätzlich müssen die Schulen schließen.')