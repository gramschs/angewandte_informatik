'''
Aufgabe 4.11

Unter https://www.frankfurt-university.de/de/hochschule/fachbereich-2-informatik-und-ingenieurwissenschaften/corona-faqs-fuer-fb-2/
finden Sie die Erklärungen, bei welchen Krankheitssymptoman man an die Hochschule kommen darf.

Schreiben Sie ein Programm, dass dem Benutzer mehrere Fragen nach Symptomen stellt, z.B. "Haben Husten?" und auf die
Antworten reagiert. Wenn z.B. die Frage nach dem Husten mit "Ja" beantwortet wird, fragt das Programm nach, ob der
Husten trocken ist oder nur gelegenlich auftritt. Am Ende soll das Programm entscheiden, ob der Benutzer an die
Hochschule kommen darf oder nicht.
'''

hat_fieber = False
ist_fieber_hoch = False
hat_husten = False
ist_husten_trocken = False
hat_stoerung_sinne = False
hat_schnupfen = False
hat_keine_weiteren_symptome = False

# Eingabe
antwort = input('Haben Sie Fieber (j(n)?')
if antwort == 'j':
    antwort = input('Ist das Fieber höher als 38,0 °C (j/n)? ')
    if antwort == 'j':
        ist_fieber_hoch = True

antwort = input('Haben Sie Husten (j/n)? ')
if antwort == 'j':
    hat_husten = True
    antwort = input('Ist der Husten trocken (j/n)? ')
    if antwort == 'j':
        ist_husten_trocken = True

antwort = input('Ist Ihr Geruchssinn oder Ihr Geschmackssinn gestört (j/n)?')
if antwort == 'j':
    hat_stoerung_sinne = True

antwort = input('Haben Sie weitere Krankheitssymptome (j/n)? ')
if antwort != 'j':
    hat_keine_weiteren_symptome = True

# Verarbeitung
darf_kommen = (not ist_fieber_hoch) and (not ist_husten_trocken) and (not hat_stoerung_sinne) and hat_keine_weiteren_symptome

if darf_kommen == True:
    print('Sie dürfen zur Hochschule kommen.')
else:
    print('Sie fürfen NICHT zur Hochschule kommen.')